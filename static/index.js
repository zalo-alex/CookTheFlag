const regexSearchInput = document.getElementById("regex-search-input")
const regexSearchResults = document.getElementById("regex-search-results")

async function regexSearch() {
    const query = regexSearchInput.value;
    const b64_query = btoa(query)

    const r = await fetch(`/regex/${b64_query}`)
    const result = (await r.json())["matches"]

    regexSearchResults.innerHTML = ""
    
    for (module of result) {
        regexSearchResults.innerHTML += `<li class="list-group-item"><a href="/module/${module.url}?${module.id}=${b64_query}">${module.name}</a></li>`
    }
}