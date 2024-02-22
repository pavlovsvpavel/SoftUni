function solve(number) {
    const numberToString = number.toString();
    let result = 0;

    for (let i = 0; i < numberToString.length; i++) {
        result += Number(numberToString[i]);
    }

    console.log(result);
}

solve(245678)