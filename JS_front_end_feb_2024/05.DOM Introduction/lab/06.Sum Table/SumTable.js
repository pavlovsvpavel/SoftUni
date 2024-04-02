function sumTable() {
    let rows = document.querySelectorAll('table tr td:nth-child(2)');
    let sum = 0;

    for (let i = 0; i < rows.length; i++) {
        sum += Number(rows[i].textContent);
    }

    document.getElementById('sum').textContent = sum;
}
