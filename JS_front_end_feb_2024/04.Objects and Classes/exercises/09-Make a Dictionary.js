function solve(array) {
    let objects = [];

    for (const element of array) {
        obj = JSON.parse(element)
        objects.push(obj)
    }

    let terms = {};

    objects.forEach(element => {
        for (const [term, description] of Object.entries(element)) {
            terms[term] = description
        }
    })

    let arrayOfTerms = Object.entries(terms);
    arrayOfTerms.sort((a, b) => (a[0].localeCompare(b[0])))

    for (const [term, description] of arrayOfTerms) {
        console.log(`Term: ${term} => Definition: ${description}`);
    }
}

solve([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}'
    ]
    );