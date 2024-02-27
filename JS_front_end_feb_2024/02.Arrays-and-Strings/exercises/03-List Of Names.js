function solve(arrayOfNames) {
    arrayOfNames.sort()

    for (let index = 0; index < arrayOfNames.length; index++) {
        let name = arrayOfNames[index];

        console.log(`${index + 1}.${name}`);
    }
}

solve (["John", "Bob", "Christina", "Ema"])
