function AddAndSubtract(num1, num2, num3) {
    function sum() {
        return num1 + num2;
    }

    function subtract() {
        return sum() - num3;
    }

    return subtract();
}

console.log(AddAndSubtract(23, 6, 10));
console.log(AddAndSubtract(1, 17, 30));
console.log(AddAndSubtract(42, 58, 100));
