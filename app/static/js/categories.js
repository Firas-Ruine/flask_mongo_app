document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("category-form");
    const list = document.getElementById("category-list");

    // Load categories and render them
    async function loadCategories() {
        const { categories } = await fetchAPI("/api/categories", "GET");
        list.innerHTML = "";
        categories.forEach((cat) => {
            const item = document.createElement("li");
            item.className = "flex justify-between items-center p-2 border rounded";
            item.innerHTML = `
                <span>${cat.name} (${cat.status ? "Enabled" : "Disabled"})</span>
                <div>
                    <button onclick="toggleStatus('${cat._id}', ${cat.status})" class="text-blue-500">Toggle</button>
                    <button onclick="deleteCategory('${cat._id}')" class="text-red-500 ml-2">Delete</button>
                </div>
            `;
            list.appendChild(item);
        });
    }

    // Add category
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const name = document.getElementById("category-name").value;
        await fetchAPI("/api/categories", "POST", { name, status: true });
        loadCategories();
        form.reset();
    });

    // Toggle category status
    window.toggleStatus = async (id, status) => {
        await fetchAPI(`/api/categories/${id}`, "PUT", { status: !status });
        loadCategories();
    };

    // Delete category
    window.deleteCategory = async (id) => {
        if (confirm("Are you sure you want to delete this category?")) {
            await fetchAPI(`/api/categories/${id}`, "DELETE");
            loadCategories();
        }
    };

    // Initial load
    loadCategories();
});
