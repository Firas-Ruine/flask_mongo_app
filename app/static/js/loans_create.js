document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loan-form");
    const subscriberDropdown = document.getElementById("subscriber_id");
    const documentDropdown = document.getElementById("document_id");

    // Populate dropdowns
    async function populateDropdowns() {
        try {
            // Fetch subscribers
            const { subscribers } = await fetchAPI("/api/subscribers", "GET");
            subscribers.forEach((sub) => {
                const option = document.createElement("option");
                option.value = sub._id;
                option.textContent = `${sub.first_name} ${sub.last_name}`;
                subscriberDropdown.appendChild(option);
            });

            // Fetch documents
            const { documents } = await fetchAPI("/api/documents", "GET");
            documents.forEach((doc) => {
                const option = document.createElement("option");
                option.value = doc._id;
                option.textContent = doc.title;
                documentDropdown.appendChild(option);
            });
        } catch (err) {
            console.error("Error loading dropdowns:", err);
            alert("Failed to load subscribers or documents.");
        }
    }

    // Handle form submission
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            subscriber_id: subscriberDropdown.value,
            document_id: documentDropdown.value,
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

    // Populate dropdowns on page load
    populateDropdowns();
});
