function solve(jsonString) {
    let person = JSON.parse(jsonString);

    for (const key in person) {
        if (person.hasOwnProperty.call(person, key)) {
            const value = person[key];
            console.log(`${key}: ${value}`);
        }
    }
}

solve('{"name": "George", "age": 40, "town": "Sofia"}');