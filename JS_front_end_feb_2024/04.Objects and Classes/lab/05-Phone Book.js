function solve(arrayOfStrings) {
    let phonebook = {};

    for (const element of arrayOfStrings) {
        let token = element.split(" ")
        let name = token[0];
        let phoneNumber = token[1];

        phonebook[name] = phoneNumber;
    }

    for (const key in phonebook) {
        if (phonebook.hasOwnProperty.call(phonebook, key)) {
            const value = phonebook[key];
            console.log(`${key} -> ${value}`);
        }
    }
}

solve(['Tim 0834212554',
'Peter 0877547887',
'Bill 0896543112',
'Tim 0876566344']
)