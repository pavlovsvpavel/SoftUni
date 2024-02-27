function solve(sentence) {
    sentence = sentence.split(" ")
    let regex = /^#[a-zA-Z]+$/;

    for (const word of sentence) {
        if (word.startsWith("#") && word.length > 1 && regex.test(word)) {
            console.log(word.substring(1));
        }
    }
}


solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')
solve('#spec33al')