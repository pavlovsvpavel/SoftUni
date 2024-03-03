function loadingBar(number) {
    let steps = number / 10;
    let bar = [];

    for (let i = 0; i < steps; i++) {
        bar += "%";
        }

    for (let i = 0; i < 10 - steps; i++) {
        bar += ".";
        }

    if (number === 100) {
        console.log("100% Complete!");
        console.log(`[${bar}]`);
    } else {
        console.log(`${number}% [${bar}]`);
        console.log("Still loading...");
    }
}

loadingBar(30)