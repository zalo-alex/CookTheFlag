const searchInput = document.getElementById("search-input")

function search() {
    const links = document.querySelectorAll(".collapse a")
    const query = searchInput.value.toLowerCase()

    for (const link of links) {
        const title = link.textContent.toLowerCase().replaceAll(" ", "").replaceAll("-", "").replaceAll(".", "").replaceAll("_", "")
        if (title.includes(query)) {
            link.classList.remove("d-none")
        } else {
            link.classList.add("d-none")
        }
    }

    const categories = document.querySelectorAll('button[data-bs-toggle="collapse"]')
    if (query === "") {
        for (const category of categories) {
            category.classList.add("collapsed")
            category.setAttribute("aria-expanded", "false")
            category.parentElement.querySelector(".collapse").classList.remove("show")
        }
    } else {
        for (const category of categories) {
            category.classList.remove("collapsed")
            category.setAttribute("aria-expanded", "true")
            category.parentElement.querySelector(".collapse").classList.add("show")
        }
    }
}