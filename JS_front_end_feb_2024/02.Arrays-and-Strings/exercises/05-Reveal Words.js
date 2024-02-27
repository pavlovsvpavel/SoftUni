function solve(words, sentence) {
    words = words.split(", ")
    sentence = sentence.split(" ")

    for (const word of words) {
        for (const sentenceWord of sentence) {
            if (sentenceWord.length === word.length && sentenceWord.startsWith("*")) {
                let index = sentence.indexOf(sentenceWord);
                sentence[index] = word;
            }
        }
    }

    console.log(sentence.join(" "));
}

solve('great', 'softuni is ***** place for learning new programming languages')
solve('great, learning', 'softuni is ***** place for ******** new programming languages')