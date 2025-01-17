document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("document-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            title: form.title.value,
            author: form.author.value,
            category: form.category.value,
        };

        try {
            await fetchAPI("/api/documents", "POST", data);
            alert("Document created successfully!");
            form.reset();
        } catch (err) {
            console.error(err);
            alert("Failed to create document.");
        }
    });
});
