document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".search-form");
    const urlInput = document.querySelector(".url-input");

    form.addEventListener("submit", () => {
        if (!urlInput.value) {
            alert("Please enter a URL to summarize!");
            return false; // Prevents form submission
        }
    });
});
