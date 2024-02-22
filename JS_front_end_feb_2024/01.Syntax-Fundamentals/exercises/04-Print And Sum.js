function solve(start, end) {
    let sumNumbers = 0;
    let numbersRange = ""

    for (let i = start; i <= end; i++) {
        numbersRange += i + " "
        sumNumbers += i
    }
    console.log(numbersRange.trimEnd());
    console.log(`Sum: ${sumNumbers}`);
}

solve(5, 10)
solve(0, 26)
solve(50, 60)