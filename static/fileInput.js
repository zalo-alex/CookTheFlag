function createFileElement(explorer, name, type) {
    const element = document.createElement("li")
    element.className = "explorer_file list-group-item list-group-item-action d-flex align-items-center gap-2"
    element.setAttribute("name", name)
    if (type == "folder") {
        element.innerHTML = `<svg width="20" height="20"><use href="#folder-icon"/></svg>${name}`
    } else {
        element.innerHTML = `<svg width="20" height="20"><use href="#file-icon"/></svg>${name}`
    }
    element.onclick = async () => {
        if (type == "folder") {
            let newPath = explorer.getAttribute("path")
            if (name == "..") {
                newPath = newPath.split("/").slice(0, newPath.split("/").length - 1)
            } else {
                newPath += `/${name}`
            }
            explorer.setAttribute("path", newPath)
            updateExplorerFiles(explorer)
        } else {
            const input = explorer.parentElement.querySelector(".form-control")
            input.value = explorer.getAttribute("path") + `/${name}`
            explorer.classList.add("d-none")
        }
    }
    return element
}

async function updateExplorerFiles(explorer) {
    const path = explorer.getAttribute("path")
    const explorerFiles = explorer.querySelector(".list-group")

    explorerFiles.innerHTML = ""

    const content = await fetch(`/api/files?path=${path}`).then(res => res.json())

    if (path != ".") {
        const element = createFileElement(explorer, "..", "folder")
        explorerFiles.appendChild(element)
    }

    content.folders.forEach(folder => {
        const element = createFileElement(explorer, folder, "folder")
        explorerFiles.appendChild(element)
    });
    content.files.forEach(folder => {
        const element = createFileElement(explorer, folder, "files")
        explorerFiles.appendChild(element)
    });
}

async function onFileInputFocus(id) {
    const inputContainer = document.querySelector(`#container-${id}`)
    const explorer = inputContainer.querySelector(".explorer")
    const explorerFiles = explorer.querySelector(".list-group")

    explorerFiles.innerHTML = ""
    if (!explorer.getAttribute("path")) {
        explorer.setAttribute("path", ".")
    }
    explorer.classList.remove("d-none")

    await updateExplorerFiles(explorer)
}

window.addEventListener("click", (e) => {
    if (!e.target.closest(".file_input") && !e.target.classList.contains("explorer_file")) {
        document.querySelectorAll(".explorer").forEach((element) => {
            element.classList.add("d-none")
        })
    }
})