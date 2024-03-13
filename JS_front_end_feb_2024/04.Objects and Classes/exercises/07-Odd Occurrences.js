function solve(string) {
    let arrayOfElements = string.split(" ");
    let elementsAsObject = {};

    for (let element of arrayOfElements) {
        element = element.toLowerCase();

        if (!elementsAsObject.hasOwnProperty(element)) {
            elementsAsObject[element] = 0;
        }

        elementsAsObject[element]++;
    }

    let entries = Object.entries(elementsAsObject)

    let result = [];
    for (const [key, value] of entries) {
        if (value % 2 !== 0) {
            result.push(key);
        }
    }

    console.log(result.join(" "));
}

solve('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
solve('Cake IS SWEET is Soft CAKE sweet Food');
