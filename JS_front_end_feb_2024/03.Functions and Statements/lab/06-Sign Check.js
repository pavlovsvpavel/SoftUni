function solve(...numbers) {
    let negativeSigns = 0;

    for (const num of numbers) {
        if (num < 0) {
            negativeSigns += 1
        }
    }

    if (negativeSigns % 2 !== 0) {
        console.log("Negative");
    } else console.log("Positive");
}


solve(5, 12, -15);
solve(-6, -12, 14);
solve(-1, -2, -3);
solve(-5, 1, 1);