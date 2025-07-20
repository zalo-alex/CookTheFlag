let form = undefined
let resetButton = () => {}
let autoToggled = true
let errorAlert = undefined;

function handleResponseData(data) {
    for (const [id, value] of Object.entries(data)) {
        if (id == "__error") continue
        document.getElementById(id).value = value
    }

    if (data.__error) {
        resetButton()
        // errorAlert should be set in the form submit event handler
        errorAlert.textContent = data.__error
        errorAlert.classList.remove("d-none")
        return
    }
}

window.addEventListener("load", () => {
    form = document.getElementById("form")

    form.addEventListener("submit", async (e) => {
        e.preventDefault()

        const type = e.submitter.value
        e.submitter.disabled = true
        const text = e.submitter.textContent
        e.submitter.textContent = "..."

        errorAlert = document.getElementById(`${type}-error`)
        errorAlert.classList.add("d-none")

        resetButton = () => {
            e.submitter.disabled = false
            e.submitter.textContent = text
        }

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        for (element of document.querySelectorAll(".key_value")) {
            var id = element.id.replace("container-", "")
            var kvContainer = document.getElementById(id)
            data[id] = {}

            for (row of kvContainer.querySelectorAll(".kv-row")) {
                if (row.querySelector(".kv-value").value) {
                    data[id][row.querySelector(".kv-key").value] = row.querySelector(".kv-value").value
                }
            }
        }

        var json;

        if (typeof isClientSide !== "undefined") {
            json = await executeClientSide(type, data)
            handleResponseData(json)
            resetButton()
        } else {
            await executeServerSide(type, data)
            // handleResponseData is done in the websocket message handler
        }
    })
})

async function executeServerSide(type, data) {
    ws.send(JSON.stringify({
        "type": "submit",
        "payload": {
            "module": location.pathname.split("/").pop(),
            "type": type,
            "data": data
        }
    }))
}

function executeClientSide(type, data) {
    
    for (const [id, value] of Object.entries(data)) {
        if (parsers[id]) {
            data[id] = parsers[id](value)
        }
    }

    try {
        return clientSideFunction(type, data)
    } catch(e) {
        return {
            "__error": e.toString()
        }
    }
}

function addKeyValueRow(id, key = "", value = "") {
    var rowId = new Date().toJSON()
    const rowContainer = document.createElement("div")
    rowContainer.id = rowId
    rowContainer.className = "row g-3 align-items-center kv-row"
    rowContainer.innerHTML += `<div class="col-md-2">
        <input type="text" class="form-control kv-key" placeholder="Key" value="${key}">
    </div>
    <div class="col-md-9">
        <input type="text" class="form-control kv-value" placeholder="Value" value="${value}">
    </div>
    <div class="col-md">
        <button class="btn btn-danger ratio-1x1" type="button" onclick="deleteKeyValueRow('${rowId}')">-</button>
    </div>`
    document.getElementById(id).appendChild(rowContainer)
}

function deleteKeyValueRow(id) {
    document.getElementById(id).remove()
}

function auto() {
    if (typeof autoButton == "undefined" || !autoToggled) {
        return
    }

    autoButton.click()
}