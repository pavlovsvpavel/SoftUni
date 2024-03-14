function solve(input) {
    let cars = {};

    for (const element of input) {
        const [direction, carNumber] = element.split(", ")
        if (direction === "IN") {
            cars[carNumber] = direction;

        } else {
            delete cars[carNumber];
        }
    }

    let sortedCars = Object.entries(cars);
    sortedCars
        .sort((a, b) => (a[0].localeCompare(b[0])))
    

    if (sortedCars.length === 0) {
        console.log("Parking Lot is Empty");
        return
    }

    for (const car of sortedCars) {
        console.log(`${car[0]}`);
    }
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']
);