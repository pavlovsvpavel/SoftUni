function solve(speed, area) {
    let speedLimit = 0;
    let speedDifference = 0;
    let status = "";

    if (area === 'motorway') {
        speedLimit = 130;
    } else if (area == 'interstate') {
        speedLimit = 90;
    } else if (area == 'city') {
        speedLimit = 50;
    } else if (area == 'residential') {
        speedLimit = 20;
    }

    speedDifference = speed - speedLimit;

    switch (true) {
        case speedDifference <= 20:
            status = 'speeding';
            break;
        case speedDifference <= 40:
            status = 'excessive speeding';
            break;
        case speedDifference > 40:
            status = 'reckless driving';
            break;
    }

    if (speedDifference > 0) {
        console.log(`The speed is ${speedDifference} km/h faster than the allowed speed of ${speedLimit} - ${status}`);

    } else {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`);
    }
}


solve(40, 'city')
solve(21, 'residential')
solve(120, 'interstate')
solve(200, 'motorway')