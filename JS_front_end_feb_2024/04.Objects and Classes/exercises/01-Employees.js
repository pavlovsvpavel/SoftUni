function solve(arrayOfNames) {
    class Employees {
        constructor(fullName, personalNumber) {
            this.fullName = fullName,
            this.personalNumber = personalNumber
        }
    }

    let arrayEmployees = [];

    for (const fullName of arrayOfNames) {
        personalNumber = fullName.length

        arrayEmployees.push(new Employees(fullName, personalNumber))
    }

    arrayEmployees.forEach(employee => {
        console.log(`Name: ${employee.fullName} -- Personal Number: ${employee.personalNumber} `);
    });
}


solve([
    'Silas Butler',
    'Adnaan Buckley',
    'Juan Peterson',
    'Brendan Villarreal'
    ])