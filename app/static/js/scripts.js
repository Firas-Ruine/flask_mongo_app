// Utility function to show messages in alerts
const showAlert = (id, message, type = "info") => {
    const alertDiv = document.getElementById(id);
    alertDiv.className = `alert alert-${type}`;
    alertDiv.innerText = message;
    alertDiv.classList.remove("d-none");
};

// Health Check
const checkHealth = async () => {
    try {
        const response = await fetch('/api/health/');
        if (!response.ok) {
            throw new Error('Failed to fetch health status');
        }
        const data = await response.json();
        showAlert('health-status', `Status: ${data.status}`, "success");
    } catch (error) {
        console.error('Error fetching health status:', error);
        showAlert('health-status', "Error checking health", "danger");
    }
};

// MongoDB Health Check
const checkMongo = async () => {
    try {
        const response = await fetch('/api/health/mongo');
        if (!response.ok) {
            throw new Error('Failed to fetch MongoDB status');
        }
        const data = await response.json();
        if (data.status === 'OK') {
            showAlert('mongo-status', `MongoDB: ${data.mongo}`, "success");
        } else {
            showAlert('mongo-status', `Error: ${data.mongo}`, "danger");
        }
    } catch (error) {
        console.error('Error fetching MongoDB status:', error);
        showAlert('mongo-status', "Error connecting to MongoDB", "danger");
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

const fetchData = async () => {
    const searchKeyword = document.getElementById('search-keyword').value || "";
    const sortBy = document.getElementById('sort-by').value || "purchase_date";
    const sortOrder = document.getElementById('sort-order').value || "asc";

    try {
        const response = await fetch(`/api/data/list?search=${searchKeyword}&sort_by=${sortBy}&order=${sortOrder}&limit=10`);
        const data = await response.json();

        const tableBody = document.getElementById('data-table-body');
        tableBody.innerHTML = ''; // Clear existing rows

        data.forEach((item, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${index + 1}</td>
                <td>${item.invoice_id || 'N/A'}</td>
                <td>${item.product_name || 'N/A'}</td>
                <td>${item.category || 'N/A'}</td>
                <td>${item.quantity || 'N/A'}</td>
                <td>${item.total ? `$${item.total.toFixed(2)}` : 'N/A'}</td>
                <td>${item.purchase_date || 'N/A'}</td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};


