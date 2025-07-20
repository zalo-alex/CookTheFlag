const searchInput = document.getElementById("search-input")
const runningTasksBadge = document.getElementById("running-tasks")

const ws = new WebSocket("ws://" + location.host + "/ws")

ws.onmessage = (event) => {
    const payload = JSON.parse(event.data)
    if (payload.type == "response") {
        handleResponseData(payload.data)
    }
    else if (payload.type == "done") {
        resetButton()
    }
    else if (payload.type == "running_tasks") {
        updateRunningTasks(payload.data.amount)
    }
}

function updateRunningTasks(amount) {
    runningTasksBadge.textContent = amount
}

function search() {
    const links = document.querySelectorAll(".collapse a")
    const query = searchInput.value.toLowerCase()

    for (const link of links) {
        const title = link.textContent.toLowerCase().replaceAll(" ", "").replaceAll("-", "").replaceAll(".", "").replaceAll("_", "")
        if (title.includes(query)) {
            link.parentElement.classList.remove("d-none")
        } else {
            link.parentElement.classList.add("d-none")
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