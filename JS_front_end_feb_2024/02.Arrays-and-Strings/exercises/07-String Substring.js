function solve(word, sentence) {
    sentence = sentence.split(" ")

    for (const singleWord of sentence) {
        if (singleWord.toLowerCase() === word) {
            return console.log(word);
        }
    }

    console.log(`${word} not found!`);
}


solve('javascript', 'JavaScript is the best programming language')
solve('python', 'JavaScript is the best programming language')