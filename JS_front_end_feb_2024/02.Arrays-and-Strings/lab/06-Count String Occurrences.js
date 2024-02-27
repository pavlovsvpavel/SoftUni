function solve(sentense, word) {
    let count = 0;

    sentenceToArr = sentense.split(" ")

    for (const el of sentenceToArr) {
        if (el === word) {
            count += 1;
        }
    }

    console.log(count);
}


solve('This is a word and it also is a sentence','is')
solve('softuni is great place for learning new programming languages','softuni')