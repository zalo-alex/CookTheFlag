const form = document.getElementById("form")

form.addEventListener("submit", async (e) => {
    e.preventDefault()

    const type = e.submitter.value

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

    for (const [id, value] of Object.entries(json)) {
        document.getElementById(id).value = value
    }
})