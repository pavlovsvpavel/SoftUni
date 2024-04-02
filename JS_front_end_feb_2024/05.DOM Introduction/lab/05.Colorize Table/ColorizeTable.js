function colorize() {
    let rows = document.querySelectorAll('table tr');

    for (i = 0; i < rows.length - 1; i++) {
        if (i % 2 !== 0) {
            rows[i].style.background = 'teal';
        }
    }
}