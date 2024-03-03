function charactersInRange(firstChar, secondChar) {
    let startNumber = firstChar.charCodeAt();
    let endNumber = secondChar.charCodeAt();
    let result = [];

    if (startNumber > endNumber) {
        [startNumber, endNumber] = [endNumber, startNumber];
    }

    for (let i = startNumber + 1; i < endNumber; i++) {
        result.push(String.fromCharCode(i));   
    }

    console.log(result.join(" "));
}

charactersInRange('a', 'd');
charactersInRange('#', ':');
charactersInRange('C', '#');