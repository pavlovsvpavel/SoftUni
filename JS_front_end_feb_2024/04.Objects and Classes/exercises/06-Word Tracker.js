function solve(input) {
    let wordsToSearch = input.shift().split(" ");

    let wordsCount = wordsToSearch.reduce(
        // creating new array on every iteration - expression body -> ()
        // (array, key) => ({ ...array, [key]: 0 }), {});

        // array is referent on every iteration - statement body -> {}
        (array, key) => {
            array[key] = 0;

            return array;
        }, {});

    for (let i = 1; i < input.length; i++) {
        let word = input[i];

        if (wordsCount.hasOwnProperty(word)) {
            wordsCount[word] += 1;
        }
    }

    let entries = Object.entries(wordsCount);
    
    entries.sort((a, b) => b[1] - a[1])

    for (let [key, value] of entries) {
        console.log(`${key} - ${value}`);
    }
}

solve([
    "this sentence",
    "In",
    "this",
    "sentence",
    "you",
    "have",
    "to",
    "count",
    "the",
    "occurrences",
    "of",
    "the",
    "words",
    "this",
    "and",
    "sentence",
    "because",
    "this",
    "is",
    "your",
    "task",
]);

solve([
    "is the",
    "first",
    "sentence",
    "Here",
    "is",
    "another",
    "the",
    "And",
    "finally",
    "the",
    "the",
    "sentence",
]);
