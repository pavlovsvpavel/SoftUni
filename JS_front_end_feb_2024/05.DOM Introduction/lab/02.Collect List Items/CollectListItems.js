function extractText() {
    let elements = document.querySelectorAll("ul#items li");
    let textarea = document.querySelector("#result");
    for (let element of elements) {
        textarea.value += element.textContent + "\n";
    }
}
