function solve(param1, param2, param3) {
    let string = "";

    for (let i = arguments.length - 1; i >= 0; i--) {
        string += arguments[i] + " ";
    }

    console.log(string);
}

solve('A', 'B', 'C')
solve('1', 'L', '&')
