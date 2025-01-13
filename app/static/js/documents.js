document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("document-form");
    const tableBody = document.querySelector("#document-list tbody");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            title: form.title.value,
            author: form.author.value,
            genre: form.genre.value,
            total_copies: parseInt(form.total_copies.value),
        };

        try {
            await fetchAPI("/api/documents", "POST", data);
            alert("Document added successfully!");
            form.reset();
            loadDocuments();
        } catch (err) {
            console.error(err);
            alert("Failed to add document. Please try again.");
        }
    });

    async function loadDocuments() {
        try {
            const { documents } = await fetchAPI("/api/documents", "GET");
            tableBody.innerHTML = "";
            documents.forEach((doc) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${doc.title}</td>
                    <td>${doc.author}</td>
                    <td>${doc.genre}</td>
                    <td>${doc.total_copies}</td>
                    <td>${doc.available_copies}</td>
                `;
                tableBody.appendChild(row);
            });
        } catch (err) {
            console.error(err);
            alert("Failed to load documents. Please try again.");
        }
    }

    loadDocuments();
});
