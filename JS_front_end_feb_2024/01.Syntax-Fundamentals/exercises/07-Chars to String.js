function solve(param1, param2, param3) {
    let string = "";

    for (let i = 0; i < arguments.length; i++) {
        string += arguments[i];
    }

    console.log(string);
}

solve('a', 'b', 'c')
solve('%', '2', 'o')
solve('1', '5', 'p')