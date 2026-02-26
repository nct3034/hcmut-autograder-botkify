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

let allResultsData = [];
let currentPage = 1;
const itemsPerPage = 10;
let autoScroll = true; // Cờ theo dõi: tự động nhảy trang khi đang chấm

// Hàm vẽ lại bảng theo trang
function renderTable() {
    const tbody = document.getElementById('resultBody');
    tbody.innerHTML = "";
    
    // Tính toán cắt mảng: ví dụ trang 1 cắt từ 0->10, trang 2 từ 10->20
    const start = (currentPage - 1) * itemsPerPage;
    const end = start + itemsPerPage;
    const pageData = allResultsData.slice(start, end);

    pageData.forEach(data => {
        const tr = document.createElement('tr');
        const statusClass = data.status === 'PASSED' ? 'pass' : 'fail';
        const statusIcon = data.status === 'PASSED' ? '✅ PASSED' : '❌ FAILED';
        const gotFormatted = (data.status === 'COMPILE ERROR' || data.got.includes("TLE")) 
                            ? escapeHTML(data.got) : highlightDiff(data.expected, data.got);
        
        tr.innerHTML = `
            <td class="stt-col" style="text-align: center; vertical-align: middle;">
                <div style="font-size: 20px; color: #005b96; margin-bottom: 8px;"><b>#${data.currentIndex}</b></div>
                <div class="${statusClass}" style="font-size: 14px;">${statusIcon}</div>
            </td>
            <td><pre>${escapeHTML(data.test_code)}</pre></td>
            <td><pre>${escapeHTML(data.expected)}</pre></td>
            <td><pre>${gotFormatted}</pre></td>
            <td class="${statusClass}" style="vertical-align: middle; text-align: center;">${statusIcon}</td>
        `;
        tbody.appendChild(tr);
    });
}

// Hàm vẽ lại các nút bấm phân trang
function renderPagination() {
    const topContainer = document.getElementById('paginationControlsTop');
    const bottomContainer = document.getElementById('paginationControlsBottom');
    
    // Hàm phụ để tạo nội dung các nút bấm
    const createControls = (container) => {
        container.innerHTML = "";
        const totalPages = Math.ceil(allResultsData.length / itemsPerPage);

        if (totalPages <= 1 && allResultsData.length <= itemsPerPage) {
            container.style.display = "none";
            return;
        }
        container.style.display = "flex";

        // --- Nút PREVIOUS ---
        const prevBtn = document.createElement('button');
        prevBtn.className = "page-btn nav-btn";
        prevBtn.innerHTML = "&laquo; Trước"; // Biểu tượng <<
        prevBtn.disabled = (currentPage === 1);
        prevBtn.onclick = () => {
            if (currentPage > 1) {
                currentPage--;
                autoScroll = false;
                renderTable();
                renderPagination();
            }
        };
        container.appendChild(prevBtn);

        // --- Các nút SỐ TRANG ---
        for (let i = 1; i <= totalPages; i++) {
            const btn = document.createElement('button');
            btn.className = `page-btn ${i === currentPage ? 'active' : ''}`;
            btn.innerText = i;
            btn.onclick = () => {
                currentPage = i;
                autoScroll = false;
                renderTable();
                renderPagination();
            };
            container.appendChild(btn);
        }

        // --- Nút NEXT ---
        const nextBtn = document.createElement('button');
        nextBtn.className = "page-btn nav-btn";
        nextBtn.innerHTML = "Sau &raquo;"; // Biểu tượng >>
        nextBtn.disabled = (currentPage === totalPages);
        nextBtn.onclick = () => {
            if (currentPage < totalPages) {
                currentPage++;
                autoScroll = false;
                renderTable();
                renderPagination();
            }
        };
        container.appendChild(nextBtn);
    };

    // Vẽ vào cả 2 nơi
    createControls(topContainer);
    createControls(bottomContainer);
}

// Hàm nộp bài chính
async function submitCode() {
    const btn = document.getElementById('runBtn');
    const tbody = document.getElementById('resultBody');
    const globalStatus = document.getElementById('globalStatus');

    if (selectedFiles.length === 0) {
        alert("Vui lòng kéo thả hoặc chọn file trước khi nộp!");
        return;
    }

    // Reset lại toàn bộ trạng thái khi nộp bài mới
    btn.disabled = true;
    tbody.innerHTML = "";
    document.getElementById('paginationControlsTop').innerHTML = "";
    document.getElementById('paginationControlsBottom').innerHTML = "";
    globalStatus.style.display = "block";
    globalStatus.className = "bg-yellow";
    globalStatus.innerText = "Hệ thống đang khởi động và nạp file... ⚙️";
    
    allResultsData = [];
    currentPage = 1;
    autoScroll = true;

    const formData = new FormData();
    selectedFiles.forEach(file => formData.append('files', file));

    try {
        const response = await fetch('/api/submit', { method: 'POST', body: formData });
        
        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.error || "Lỗi Server");
        }

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
            buffer = lines.pop(); 

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
                    
                    // Lưu dữ liệu vào mảng tổng
                    data.currentIndex = currentIndex;
                    allResultsData.push(data);

                    // Nếu đang chế độ autoScroll, tự động chuyển sang trang mới nhất
                    if (autoScroll) {
                        currentPage = Math.ceil(allResultsData.length / itemsPerPage);
                    }

                    // Cập nhật giao diện liên tục
                    globalStatus.innerText = `Đang chấm ${currentIndex}/${totalTests} Test Cases... ⏳`;
                    renderTable();
                    renderPagination();
                }
                else if (data.type === 'done') {
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