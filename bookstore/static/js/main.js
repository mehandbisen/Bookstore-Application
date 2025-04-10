// main.js

// JavaScript for back button functionality
document.addEventListener("DOMContentLoaded", function () {
    const backBtn = document.getElementById("back-btn");
    if (backBtn) {
        backBtn.addEventListener("click", function () {
            window.history.back();
        });
    }
});
