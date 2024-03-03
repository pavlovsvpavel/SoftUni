function solve(numOne, numTwo, operator) {

    let operators = {
        multiply: (firstNum, secondNum) => firstNum * secondNum,
        divide: (firstNum, secondNum) => firstNum / secondNum,
        add: (firstNum, secondNum) => firstNum + secondNum,
        subtract: (firstNum, secondNum) => firstNum - secondNum,
    }

    return operators[operator](numOne, numTwo)
}

console.log(solve(5, 5, 'multiply'));

