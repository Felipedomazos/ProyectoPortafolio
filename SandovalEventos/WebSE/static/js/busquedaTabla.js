const searchInput = document.getElementById("search");
const figures = document.querySelectorAll(".tablas figure");

searchInput.addEventListener("input", function () {
    const searchTerm = searchInput.value.toLowerCase();

    figures.forEach(function (figure) {
        const h3 = figure.querySelector("h3");
        const text = h3.innerText.toLowerCase();

        if (text.includes(searchTerm)) {
            figure.style.display = "block";
        } else {
            figure.style.display = "none";
        }
    });
});