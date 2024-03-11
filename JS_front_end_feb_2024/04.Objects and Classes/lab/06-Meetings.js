function solve(arrayOfStrings) {
    let meetings = {};

    for (const element of arrayOfStrings) {
        let tokens = element.split(" ");
        let name = tokens[1];
        let weekday = tokens[0];

        if (meetings.hasOwnProperty(weekday)) {
            console.log(`Conflict on ${weekday}!`);
        } else {
            meetings[weekday] = name;
            console.log(`Scheduled for ${weekday}`);
        }
    }

    for (const key in meetings) {
        if (meetings.hasOwnProperty.call(meetings, key)) {
            const value = meetings[key];
            console.log(`${key} -> ${value}`);
        }
    }
}

solve(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);
solve(["Friday Bob", "Saturday Ted", "Monday Bill", "Monday John", "Wednesday George"]);
