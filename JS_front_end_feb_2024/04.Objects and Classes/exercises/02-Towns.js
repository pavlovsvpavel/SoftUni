function solve(input) {
    class Town {
        constructor(town, latitude, longitude) {
            this.town = town,
            this.latitude = latitude,
            this.longitude = longitude
        }

        toString() {
            return `{ town: '${this.town}', latitude: '${this.latitude}', longitude: '${this.longitude}' }`;
        }    
    }

    arrayOfTowns = [];

    for (const element of input) {
        let [currentTown, latitude, longitude] = element.split(" | ")
        latitude = Number(latitude).toFixed(2);
        longitude = Number(longitude).toFixed(2);

        arrayOfTowns.push(new Town(currentTown, latitude, longitude));
    }

    arrayOfTowns.forEach(element => {
        console.log(element.toString());
    });
}

solve(['Sofia | 42.696552 | 23.32601', 'Beijing | 39.913818 | 116.363625'])