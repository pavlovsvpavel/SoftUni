function solve(number) {
    let numberToString = number.toString()
    let sumOfNumbers = 0;
    let matchingNumber = numberToString[0];
    let unique = 'false';

    for (let i = 0; i < numberToString.length; i++) {
        singleNumber = Number(numberToString[i])
        sumOfNumbers += singleNumber;

        if (singleNumber == matchingNumber) {
            unique = 'true';
        } else {
            unique = 'false'
        }
    }

    console.log(unique);
    console.log(sumOfNumbers);
}

solve(2222222)
solve(1234)