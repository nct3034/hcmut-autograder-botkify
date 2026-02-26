// --- LOGIC KÉO THẢ VÀ QUẢN LÝ FILE ---
let selectedFiles = []; 
const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileListContainer = document.getElementById('fileList');

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

function preventDefaults(e) { e.preventDefault(); e.stopPropagation(); }

['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => dropZone.classList.add('dragover'), false);
});
['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, () => dropZone.classList.remove('dragover'), false);
});

dropZone.addEventListener('drop', (e) => handleFiles(e.dataTransfer.files), false);
fileInput.addEventListener('change', (e) => handleFiles(e.target.files));

function handleFiles(files) {
    selectedFiles = Array.from(files); 
    renderFileList();
}

function renderFileList() {
    fileListContainer.innerHTML = ''; 
    selectedFiles.forEach(file => {
        const item = document.createElement('div');
        item.className = 'file-item';
        item.innerHTML = `
            <svg class="file-icon" viewBox="0 0 24 24">
                <path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2h12c1.1 0 2-.9 2-2V8l-6-6zm-1.75 14v-1.5c0-.28-.22-.5-.5-.5H11.5v-1.5h.25c.28 0 .5-.22.5-.5v-1.5c0-.28-.22-.5-.5-.5h-.25v-1.5H10.5v1.5h-.25c-.28 0-.5.22-.5.5v1.5c0 .28.22.5.5.5h.25v1.5H11.5v1.5h-.25c-.28 0-.5.22-.5.5v1.5c0 .28.22.5.5.5h.25v1.5h1v-1.5h.25c.28 0 .5-.22.5-.5zM13 9V3.5L18.5 9H13z"/>
            </svg>
            <span class="file-name">${file.name}</span>
        `;
        fileListContainer.appendChild(item);
    });
}

// --- LOGIC CHẤM BÀI VÀ DIFFING ---
function highlightDiff(expected, got) {
    if (expected === got) return escapeHTML(got);
    let result = ""; let isDiffing = false;
    for (let i = 0; i < got.length; i++) {
        if (i >= expected.length || got[i] !== expected[i]) {
            if (!isDiffing) { result += "<span class='diff-highlight'>"; isDiffing = true; }
            result += escapeHTML(got[i]);
        } else {
            if (isDiffing) { result += "</span>"; isDiffing = false; }
            result += escapeHTML(got[i]);
        }
    }
    if (isDiffing) result += "</span>";
    return result;
}

function escapeHTML(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// ... (Phần logic kéo thả và hàm highlightDiff giữ nguyên) ...

async function submitCode() {
    const btn = document.getElementById('runBtn');
    const tbody = document.getElementById('resultBody');
    const globalStatus = document.getElementById('globalStatus');

    if (selectedFiles.length === 0) {
        alert("Vui lòng kéo thả hoặc chọn file trước khi nộp!");
        return;
    }

    btn.disabled = true;
    tbody.innerHTML = "";
    globalStatus.style.display = "block";
    globalStatus.className = "bg-yellow";
    globalStatus.innerText = "Hệ thống đang khởi động và nạp file... ⚙️";

    const formData = new FormData();
    selectedFiles.forEach(file => formData.append('files', file));

    try {
        const response = await fetch('/api/submit', { method: 'POST', body: formData });
        
        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || "Lỗi Server");
        }

        // Đọc dữ liệu theo dạng Stream (Luồng chảy)
        const reader = response.body.getReader();
        const decoder = new TextDecoder("utf-8");
        let buffer = "";

        let totalTests = 0;
        let passCount = 0;
        let currentIndex = 0;

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, { stream: true });
            let lines = buffer.split('\n');
            buffer = lines.pop(); // Giữ lại phần text chưa hoàn chỉnh cho vòng lặp sau

            for (let line of lines) {
                if (!line.trim()) continue;
                const data = JSON.parse(line);

                if (data.type === 'start') {
                    totalTests = data.total;
                    globalStatus.innerText = `Đang chấm 0/${totalTests} Test Cases... ⏳`;
                } 
                else if (data.type === 'result') {
                    currentIndex++;
                    if (data.status === 'PASSED') passCount++;

                    // Cập nhật trạng thái liên tục
                    globalStatus.innerText = `Đang chấm ${currentIndex}/${totalTests} Test Cases... ⏳`;

                    // Vẽ ngay 1 dòng lên bảng
                    const tr = document.createElement('tr');
                    const statusClass = data.status === 'PASSED' ? 'pass' : 'fail';
                    const statusIcon = data.status === 'PASSED' ? '✅ PASSED' : '❌ FAILED';
                    const gotFormatted = (data.status === 'COMPILE ERROR' || data.got.includes("TLE")) 
                                        ? escapeHTML(data.got) : highlightDiff(data.expected, data.got);
                    
                    tr.innerHTML = `
                        <td class="stt-col" style="text-align: center; vertical-align: middle;">
                            <div style="font-size: 20px; color: #005b96; margin-bottom: 8px;"><b>#${currentIndex}</b></div>
                            <div class="${statusClass}" style="font-size: 14px;">${statusIcon}</div>
                        </td>
                        <td><pre>${escapeHTML(data.test_code)}</pre></td>
                        <td><pre>${escapeHTML(data.expected)}</pre></td>
                        <td><pre>${gotFormatted}</pre></td>
                        <td class="${statusClass}" style="vertical-align: middle; text-align: center;">${statusIcon}</td>
                    `;
                    tbody.appendChild(tr);

                    // Tự động cuộn trang xuống dòng mới nhất
                    tr.scrollIntoView({ behavior: 'smooth', block: 'end' });
                }
                else if (data.type === 'done') {
                    // Chốt kết quả tổng
                    if (passCount === 0) {
                        globalStatus.className = "bg-red";
                        globalStatus.innerText = `❌ Sai toàn bộ! (Pass ${passCount}/${totalTests})`;
                    } else if (passCount < totalTests) {
                        globalStatus.className = "bg-yellow";
                        globalStatus.innerText = `⚠️ Đúng một phần! (Pass ${passCount}/${totalTests})`;
                    } else {
                        globalStatus.className = "bg-green";
                        globalStatus.innerText = `✅ Hoàn hảo! Pass toàn bộ bài test (${passCount}/${totalTests}) 🎉`;
                    }
                }
            }
        }
    } catch (err) {
        globalStatus.className = "bg-red";
        globalStatus.innerText = err.message || "Lỗi kết nối tới Server!";
    }
    
    btn.disabled = false;
}