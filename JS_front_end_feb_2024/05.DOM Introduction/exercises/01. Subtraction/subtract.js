function subtract() {
    const firstNumber = document.getElementById('firstNumber').value
    const secondNumber = document.getElementById('secondNumber').value
    const result = document.getElementById('result')
    const subtraction = Number(firstNumber) - Number(secondNumber)
    
    console.log(result.textContent = subtraction);
}
