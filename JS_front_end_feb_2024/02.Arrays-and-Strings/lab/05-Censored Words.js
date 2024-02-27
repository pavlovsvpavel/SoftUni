function solve(sentence, word) {
    modifiedWord = '*'.repeat(word.length);
    
    while (sentence.includes(word)) {
        sentence = sentence.replace(word, modifiedWord)
    }

    console.log(sentence);
}


solve('A small sentence with some words', 'small')
solve('Find the hidden word', 'hidden')