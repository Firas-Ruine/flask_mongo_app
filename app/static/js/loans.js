document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("loan-form");
    const tableBody = document.querySelector("#loan-list tbody");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            subscriber_id: form.subscriber_id.value,
            document_id: form.document_id.value,
            due_date: form.due_date.value,
        };

        try {
            await fetchAPI("/api/loans", "POST", data);
            alert("Loan recorded successfully!");
            form.reset();
            loadLoans();
        } catch (err) {
            console.error(err);
            alert("Failed to record loan. Please try again.");
        }
    });

    async function loadLoans() {
        try {
            const { loans } = await fetchAPI("/api/loans", "GET");
            tableBody.innerHTML = "";
            loans.forEach((loan) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${loan.subscriber_id}</td>
                    <td>${loan.document_id}</td>
                    <td>${loan.loan_date}</td>
                    <td>${loan.due_date}</td>
                    <td>${loan.status}</td>
                `;
                tableBody.appendChild(row);
            });
        } catch (err) {
            console.error(err);
            alert("Failed to load loans. Please try again.");
        }
    }

    loadLoans();
});
