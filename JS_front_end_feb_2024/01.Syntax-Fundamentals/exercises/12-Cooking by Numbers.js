function solve(string, param1, param2, param3, param4, param5) {
    let number = Number(string);
    let result = number;

    for (let i = 1; i < arguments.length; i++) {
        if (arguments[i] == 'chop') {
            result /= 2;
        } else if (arguments[i] == 'dice') {
            result = Math.sqrt(result);
        } else if (arguments[i] == 'spice') {
            result += 1;
        } else if (arguments[i] == 'bake') {
            result *= 3;
        } else if (arguments[i] == 'fillet') {
            result *= 0.8 
        }

        console.log(result);
    }
}


solve('32', 'chop', 'chop', 'chop', 'chop', 'chop')
solve('9', 'dice', 'spice', 'chop', 'bake', 'fillet')