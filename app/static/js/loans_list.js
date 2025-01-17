document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("loan-list");
    const searchInput = document.getElementById("search-input");

    // Load loans and render them in the table
    async function loadLoans(search = "") {
        try {
            const { loans } = await fetchAPI(`/api/loans?search=${encodeURIComponent(search)}`, "GET");
            tableBody.innerHTML = "";
            loans.forEach((loan) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td class="p-2 border border-gray-300">${loan.subscriber_name}</td>
                    <td class="p-2 border border-gray-300">${loan.document_title}</td>
                    <td class="p-2 border border-gray-300">${loan.status}</td>
                    <td class="p-2 border border-gray-300">
                        <button class="text-blue-500" onclick="editLoan('${loan._id}')">Edit</button>
                        <button class="text-red-500 ml-2" onclick="deleteLoan('${loan._id}')">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } catch (err) {
            console.error("Error loading loans:", err);
            alert("Failed to load loans.");
        }
    }

    // Edit a loan
    window.editLoan = async function (id) {
        const newStatus = prompt("Enter new status (Pending, Approved, Returned):");
        if (newStatus) {
            try {
                await fetchAPI(`/api/loans/${id}`, "PUT", { status: newStatus });
                alert("Loan updated successfully!");
                loadLoans();
            } catch (err) {
                console.error("Error updating loan:", err);
                alert("Failed to update loan.");
            }
        }
    };

    // Delete a loan with confirmation
    window.deleteLoan = async function (id) {
        const confirmDelete = confirm("Are you sure you want to delete this loan?");
        if (confirmDelete) {
            try {
                await fetchAPI(`/api/loans/${id}`, "DELETE");
                alert("Loan deleted successfully!");
                loadLoans();
            } catch (err) {
                console.error("Error deleting loan:", err);
                alert("Failed to delete loan.");
            }
        }
    };

    // Handle search input
    searchInput.addEventListener("input", () => {
        const searchTerm = searchInput.value.trim();
        loadLoans(searchTerm);
    });

    // Initial load of loans
    loadLoans();
});
