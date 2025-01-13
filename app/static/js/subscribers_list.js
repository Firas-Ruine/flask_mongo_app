document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.getElementById("subscriber-list");
    const searchInput = document.getElementById("search-input"); // Reference to the search input field

    // Load subscribers and render them in the table
    async function loadSubscribers(search = "") {
        try {
            // Fetch subscribers with optional search query
            const { subscribers } = await fetchAPI(`/api/subscribers?search=${encodeURIComponent(search)}`, "GET");
            tableBody.innerHTML = ""; // Clear existing rows
            subscribers.forEach((sub) => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td class="p-2 border border-gray-300">${sub.first_name}</td>
                    <td class="p-2 border border-gray-300">${sub.last_name}</td>
                    <td class="p-2 border border-gray-300">${sub.email}</td>
                    <td class="p-2 border border-gray-300">${sub.phone}</td>
                    <td class="p-2 border border-gray-300">${sub.address}</td>
                    <td class="p-2 border border-gray-300">
                        <button class="text-blue-500" onclick="editSubscriber('${sub._id}')">Edit</button>
                        <button class="text-red-500 ml-2" onclick="deleteSubscriber('${sub._id}')">Delete</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        } catch (err) {
            console.error("Error loading subscribers:", err);
            alert("Failed to load subscribers.");
        }
    }

    // Edit a subscriber
    window.editSubscriber = async function (id) {
        const newFirstName = prompt("Enter new first name:");
        const newLastName = prompt("Enter new last name:");
        if (newFirstName && newLastName) {
            try {
                await fetchAPI(`/api/subscribers/${id}`, "PUT", {
                    first_name: newFirstName,
                    last_name: newLastName,
                });
                alert("Subscriber updated successfully!");
                loadSubscribers();
            } catch (err) {
                console.error("Error updating subscriber:", err);
                alert("Failed to update subscriber.");
            }
        }
    };

    // Delete a subscriber with confirmation
    window.deleteSubscriber = async function (id) {
        const confirmDelete = confirm("Are you sure you want to delete this subscriber?");
        if (confirmDelete) {
            try {
                await fetchAPI(`/api/subscribers/${id}`, "DELETE");
                alert("Subscriber deleted successfully!");
                loadSubscribers();
            } catch (err) {
                console.error("Error deleting subscriber:", err);
                alert("Failed to delete subscriber.");
            }
        }
    };

    // Handle search input
    searchInput.addEventListener("input", () => {
        const searchTerm = searchInput.value.trim();
        loadSubscribers(searchTerm);
    });

    // Initial load of subscribers
    loadSubscribers();
});
