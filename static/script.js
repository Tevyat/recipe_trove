const autocomplete = document.querySelector(".autocomplete-box");
const inputBar = document.getElementById("search-bar")

async function fetchTitles() {
    try {
        const response = await fetch('/api/items'); 
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const titles = await response.json();

        inputBar.addEventListener('keyup', function() {
            let result = []
            let input = this.value;
            if (input.length) {
                result = titles.filter((keyword) => {
                    return keyword.toLowerCase().includes(input.toLowerCase());
                })
                console.log(result)
            }
            display(result)
        });
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

function display(result) {
    const content = result.map((list) => {
        return "<li onclick=selectInput(this)>" + list + "</li>";
    });

    autocomplete.innerHTML = "<ul>" + content.join("") + "</ul>";
}

function selectInput(list) {
    inputBar.value = list.innerHTML;
    autocomplete.innerHTML = ""
    inputBar.form.submit()
}

window.onload = fetchTitles();