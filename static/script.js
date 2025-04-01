document.addEventListener("DOMContentLoaded", function () {
    const searchBar = document.getElementById("searchBar");
    const searchResults = document.getElementById("searchResults");

    let foodItems = [];

    // Fetch food items from the server
    fetch("/get_food_items")
        .then(response => response.json())
        .then(data => {
            foodItems = data;
        })
        .catch(error => console.error("Error fetching food items:", error));

    searchBar.addEventListener("input", function () {
        const query = searchBar.value.toLowerCase();
        searchResults.innerHTML = "";

        if (query.length === 0) {
            searchResults.style.display = "none";
            return;
        }

        let filteredItems = foodItems.filter(item => item.toLowerCase().includes(query));

        if (filteredItems.length === 0) {
            searchResults.style.display = "none";
            return;
        }

        filteredItems.slice(0, 5).forEach(item => {
            let link = document.createElement("a");
            link.classList.add("search-result");
            link.href = "/item/" + encodeURIComponent(item);
            link.textContent = item;
            searchResults.appendChild(link);
        });

        searchResults.style.display = "block";
    });

    // Hide results when clicking outside
    document.addEventListener("click", function (e) {
        if (!searchBar.contains(e.target) && !searchResults.contains(e.target)) {
            searchResults.style.display = "none";
        }
    });
});
