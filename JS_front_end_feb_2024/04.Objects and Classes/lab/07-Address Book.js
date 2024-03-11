function solve(arrayOfStrings) {
    let addressBook = {};

    for (let entry of arrayOfStrings) {
        let [name, address] = entry.split(":");
        addressBook[name] = address
    }

    let addressBookAsArray = Object.entries(addressBook)
    addressBookAsArray.sort((a, b) => a[0].localeCompare(b[0]));

    for (let i=0; i < addressBookAsArray.length; i++) {
        let [name, address] = addressBookAsArray[i]
        console.log(`${name} -> ${address}`);      
    }
}

solve([
    "Tim:Doe Crossing",
    "Bill:Nelson Place",
    "Peter:Carlyle Ave",
    "Bill:Ornery Rd",
]);
