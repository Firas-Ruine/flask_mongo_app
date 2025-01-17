document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loan-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            subscriber_name: form.subscriber_name.value,
            document_title: form.document_title.value,
            status: form.status.value,
        };

        try {
            await fetchAPI("/api/loans", "POST", data);
            alert("Loan created successfully!");
            form.reset();
        } catch (err) {
            console.error(err);
            alert("Failed to create loan.");
        }
    });
});
