function OddAndEvenSum(number) {
    let numbersArray = Array.from(String(number), Number)
    let oddSum = 0;
    let evenSum = 0;

    for (const number of numbersArray) {
        if (number % 2 == 0) {
            evenSum += number;
        } else oddSum += number;
    }

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

OddAndEvenSum(1000435);
OddAndEvenSum(3495892137259234);