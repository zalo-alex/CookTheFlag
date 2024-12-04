const regexSearchInput = document.getElementById("regex-search-input")
const regexSearchResults = document.getElementById("regex-search-results")

async function regexSearch() {
    const query = regexSearchInput.value;

    const r = await fetch(`/regex/${btoa(query)}`)
    const result = (await r.json())["matches"]

    regexSearchResults.innerHTML = ""
    
    for (module of result) {
        regexSearchResults.innerHTML += `<li class="list-group-item"><a href="/module/${module.url}">${module.name}</a></li>`
    }
}