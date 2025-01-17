document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("document-list");
    const searchInput = document.getElementById("search-input");

    // Load documents and render them in the table
    async function loadDocuments(search = "") {
        try {
            const { documents } = await fetchAPI(`/api/documents?search=${encodeURIComponent(search)}`, "GET");
            tableBody.innerHTML = "";
            documents.forEach((doc) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td class="p-2 border border-gray-300">${doc.title}</td>
                    <td class="p-2 border border-gray-300">${doc.author}</td>
                    <td class="p-2 border border-gray-300">${doc.category}</td>
                    <td class="p-2 border border-gray-300">
                        <button class="text-blue-500" onclick="editDocument('${doc._id}')">Edit</button>
                        <button class="text-red-500 ml-2" onclick="deleteDocument('${doc._id}')">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } catch (err) {
            console.error("Error loading documents:", err);
            alert("Failed to load documents.");
        }
    }

    // Edit a document
    window.editDocument = async function (id) {
        const newTitle = prompt("Enter new title:");
        const newAuthor = prompt("Enter new author:");
        if (newTitle && newAuthor) {
            try {
                await fetchAPI(`/api/documents/${id}`, "PUT", {
                    title: newTitle,
                    author: newAuthor,
                });
                alert("Document updated successfully!");
                loadDocuments();
            } catch (err) {
                console.error("Error updating document:", err);
                alert("Failed to update document.");
            }
        }
    };

    // Delete a document with confirmation
    window.deleteDocument = async function (id) {
        const confirmDelete = confirm("Are you sure you want to delete this document?");
        if (confirmDelete) {
            try {
                await fetchAPI(`/api/documents/${id}`, "DELETE");
                alert("Document deleted successfully!");
                loadDocuments();
            } catch (err) {
                console.error("Error deleting document:", err);
                alert("Failed to delete document.");
            }
        }
    };

    // Handle search input
    searchInput.addEventListener("input", () => {
        const searchTerm = searchInput.value.trim();
        loadDocuments(searchTerm);
    });

    // Initial load of documents
    loadDocuments();
});
