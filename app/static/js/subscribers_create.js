document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("subscriber-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const data = {
            first_name: form.first_name.value,
            last_name: form.last_name.value,
            email: form.email.value,
            phone: form.phone.value,
            address: form.address.value,
        };

        try {
            await fetchAPI("/api/subscribers", "POST", data);
            alert("Subscriber created successfully!");
            form.reset();
        } catch (err) {
            console.error(err);
        }
    });
});
