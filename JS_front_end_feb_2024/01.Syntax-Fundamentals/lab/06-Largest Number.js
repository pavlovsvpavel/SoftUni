function solve(num_1, num_2, num_3) {
    let result;
    if (num_1 > num_2 && num_1 > num_3) {
        result = num_1;
    } else if (num_2 > num_1 && num_2 > num_3) {
        result = num_2;
    } else if (num_3 > num_1 && num_3 > num_1) {
        result = num_3
    }
    console.log(`The largest number is ${result}.`);
}

solve(5, -3, 16)
solve(-3, -5, -22.5)