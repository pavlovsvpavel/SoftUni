function solve(arrayOfNumbers) {
    sortedNumbers = [];

    while (arrayOfNumbers.length > 1) {
        let maxNumber = Math.max(...arrayOfNumbers);
        let minNumber = Math.min(...arrayOfNumbers);

        sortedNumbers.push(minNumber);
        sortedNumbers.push(maxNumber);

        let maxNumIndex = arrayOfNumbers.indexOf(maxNumber);
        let minNumIndex = arrayOfNumbers.indexOf(minNumber);

        let indexesToRemove = [maxNumIndex, minNumIndex].sort((a, b) => b - a);
        indexesToRemove.forEach(index => arrayOfNumbers.splice(index, 1));

    }

    if (arrayOfNumbers.length > 0) {
        sortedNumbers.push(arrayOfNumbers.pop());
    }
    
    return(sortedNumbers);
}

solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]);
solve([1, 65, 3, 52, 48, 63, 31, -3, 18]);
