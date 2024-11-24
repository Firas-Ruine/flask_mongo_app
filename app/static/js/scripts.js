const showAlert = (id, message, type = "info") => {
    const element = document.getElementById(id);
    element.className = `alert alert-${type}`;
    element.innerText = message;
    element.classList.remove("d-none");
};

// Show status messages in the UI
const showMongoStatus = (message, type) => {
    const statusDiv = document.getElementById('mongo-status');
    statusDiv.className = `alert alert-${type}`;
    statusDiv.innerText = message;
    statusDiv.style.display = 'block';
};

// Check MongoDB status
const checkMongo = async () => {
    try {
        const response = await fetch('/api/mongo/status');
        const data = await response.json();
        if (response.ok) {
            showMongoStatus(`MongoDB Status: ${data.status}`, 'success');
        } else {
            showMongoStatus(`Error: ${data.error}`, 'danger');
        }
    } catch (error) {
        showMongoStatus('Error checking MongoDB status.', 'danger');
    }
};

// Reconnect to MongoDB
const reconnectMongo = async () => {
    try {
        const response = await fetch('/api/mongo/reconnect', {
            method: 'POST'
        });
        const data = await response.json();
        if (response.ok) {
            showMongoStatus(data.message, 'success');
        } else {
            showMongoStatus(`Error: ${data.error}`, 'danger');
        }
    } catch (error) {
        showMongoStatus('Error reconnecting to MongoDB.', 'danger');
    }
};


const generateData = async () => {
    const numRecords = document.getElementById('num-records').value || 100;
    try {
        const response = await fetch('/api/data/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ num_records: parseInt(numRecords) }),
        });
        const data = await response.json();
        showAlert('data-status', data.message, "success");
    } catch (error) {
        showAlert('data-status', "Error generating data", "danger");
    }
};

const fetchData = async (page = 1) => {
    const search = document.getElementById('search-keyword').value || '';
    const sortBy = document.getElementById('sort-by').value || 'purchase_date';
    const sortOrder = document.getElementById('sort-order').value || 'asc';
    const limit = 10;

    try {
        const response = await fetch(
            `/api/data/list?search=${search}&sort_by=${sortBy}&order=${sortOrder}&page=${page}&limit=${limit}`
        );
        const result = await response.json();

        const tableBody = document.getElementById('data-table-body');
        tableBody.innerHTML = '';

        result.data.forEach((item, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${(page - 1) * limit + index + 1}</td>
                <td>${item.invoice_id || 'N/A'}</td>
                <td>${item.product_name || 'N/A'}</td>
                <td>${item.category || 'N/A'}</td>
                <td>${item.quantity || 'N/A'}</td>
                <td>${item.total ? `$${item.total.toFixed(2)}` : 'N/A'}</td>
                <td>${item.purchase_date || 'N/A'}</td>
            `;
            tableBody.appendChild(row);
        });

        updatePagination(result.page, result.total_pages);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

const updatePagination = (currentPage, totalPages) => {
    const paginationControls = document.getElementById('pagination-controls');
    paginationControls.innerHTML = '';

    const prevPage = currentPage > 1 ? currentPage - 1 : 1;
    paginationControls.innerHTML += `
        <li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
            <a class="page-link" href="#" onclick="fetchData(${prevPage})">Previous</a>
        </li>
    `;

    if (currentPage > 2) {
        paginationControls.innerHTML += `
            <li class="page-item"><a class="page-link" href="#" onclick="fetchData(1)">1</a></li>
        `;
        if (currentPage > 3) {
            paginationControls.innerHTML += `
                <li class="page-item disabled"><span class="page-link">...</span></li>
            `;
        }
    }

    for (let i = Math.max(1, currentPage - 1); i <= Math.min(totalPages, currentPage + 1); i++) {
        paginationControls.innerHTML += `
            <li class="page-item ${i === currentPage ? 'active' : ''}">
                <a class="page-link" href="#" onclick="fetchData(${i})">${i}</a>
            </li>
        `;
    }

    if (currentPage < totalPages - 1) {
        if (currentPage < totalPages - 2) {
            paginationControls.innerHTML += `
                <li class="page-item disabled"><span class="page-link">...</span></li>
            `;
        }
        paginationControls.innerHTML += `
            <li class="page-item"><a class="page-link" href="#" onclick="fetchData(${totalPages})">${totalPages}</a></li>
        `;
    }

    const nextPage = currentPage < totalPages ? currentPage + 1 : totalPages;
    paginationControls.innerHTML += `
        <li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
            <a class="page-link" href="#" onclick="fetchData(${nextPage})">Next</a>
        </li>
    `;
};

