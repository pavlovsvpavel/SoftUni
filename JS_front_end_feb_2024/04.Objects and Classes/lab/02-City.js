function solve(object) {
    for (const key in object) {
        if (Object.hasOwnProperty.call(object, key)) {
            const value = object[key];
            console.log(`${key} -> ${value}`);
        }
    }
}

solve({
    name: "Sofia",
    area: 492,
    population: 1238438,
    country: "Bulgaria",
    postCode: "1000",
});
