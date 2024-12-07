const form = document.getElementById("form")

form.addEventListener("submit", async (e) => {
    e.preventDefault()

    const type = e.submitter.value
    e.submitter.disabled = true
    const text = e.submitter.textContent
    e.submitter.textContent = "..."

    const errorAlert = document.getElementById(`${type}-error`)
    errorAlert.classList.add("d-none")

    const resetButton = () => {
        e.submitter.disabled = false
        e.submitter.textContent = text
    }

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    const res = await fetch(location.pathname, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            type,
            ...data
        })
    })
    const json = await res.json()

    if (json.__error) {
        resetButton()
        errorAlert.textContent = json.__error
        errorAlert.classList.remove("d-none")
        return
    }

    for (const [id, value] of Object.entries(json)) {
        document.getElementById(id).value = value
    }

    resetButton()
})