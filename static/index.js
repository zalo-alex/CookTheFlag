const regexSearchInput = document.getElementById("regex-search-input")
const regexSearchResults = document.getElementById("regex-search-results")

async function regexSearch() {
    const query = regexSearchInput.value;
    const b64_query = btoa(query)

    const r = await fetch(`/regex/${b64_query}`)
    const result = (await r.json())["matches"]

    regexSearchResults.innerHTML = ""
    
    for (module of result) {
        regexSearchResults.innerHTML += `<li class="list-group-item"><a class="text-decoration-none" href="/module/${module.url}?${module.id}=${b64_query}">${module.name} <span class="text-secondary description"> > ${module.element_name}</span></a></li>`
    }
}