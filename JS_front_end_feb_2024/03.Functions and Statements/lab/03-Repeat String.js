function solve(string, repeat) {
    let result = ""

    for (let i = 0; i < repeat; i++) {
        result += string;
    }

    return result
}


console.log(solve("abc", 3));
console.log(solve("String", 2));