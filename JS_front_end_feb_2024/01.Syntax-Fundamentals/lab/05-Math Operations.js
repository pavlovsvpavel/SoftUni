function solve(number_1, number_2, operator) {
    let result = 0;
    if (operator === '+') {
        console.log(number_1 + number_2);
    } else if (operator === '-') {
        console.log(number_1 - number_2);
    } else if (operator === '*') {
        console.log(number_1 * number_2);
    } else if (operator === '/') {
        console.log(number_1 / number_2);
    } else if (operator === '%') {
        console.log(number_1 % number_2);
    } else if (operator === '**') {
        console.log(number_1 ** number_2);
    }
}

solve(5, 6, '+')
solve(3, 5.5, '*')