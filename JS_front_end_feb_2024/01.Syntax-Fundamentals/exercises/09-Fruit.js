function solve(fruit, weight, pricePerKilogram) {
    let weightInKilograms = weight / 1000
    let money = weightInKilograms * pricePerKilogram;

    console.log(`I need \$${money.toFixed(2)} to buy ${weightInKilograms.toFixed(2)} kilograms ${fruit}.`);
}

solve('orange', 2500, 1.80)
solve('apple', 1563, 2.35)