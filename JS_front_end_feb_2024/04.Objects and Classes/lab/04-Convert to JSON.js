function solve(firstName, lastName, hairColor) {
    let person = {
        "name": firstName,
        "lastName": lastName,
        "hairColor": hairColor,
    }

    personJson = JSON.stringify(person)
    console.log(personJson);
}

solve('George', 'Jones', 'Brown')