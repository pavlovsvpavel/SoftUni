function toggle() {
    const button = document.getElementsByClassName("button")[0];
    const text = document.getElementById('extra');
    let textStyleDisplay = text.style.display;

    if (textStyleDisplay == 'none') {
        text.style.display = 'block';
        button.textContent = 'Less';
    } else {
        text.style.display = 'none';
        button.textContent = 'More';
    }
}