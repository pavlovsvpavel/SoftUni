function solve(input) {
    const numberOfAstronauts = Number(input[0]);

    const astronautsTeam = {};

    let astronauts = input.slice(1, numberOfAstronauts + 1)
    for (let line of astronauts) {
        const [astroName, oxygen, energy] = line.split(' ');
        astronautsTeam[astroName] = {
            oxygen: Number(oxygen),
            energy: Number(energy),
        }
    }

    let commandArgs =input.slice(numberOfAstronauts + 1);

    let commandLine = commandArgs.shift();

    while (commandLine != 'End') {
        let [command, astronautName, commandValue] = commandLine.split(' - ');
        const currentAstro = astronautsTeam[astronautName]
        commandValue = Number(commandValue);

        switch (command) {
            case 'Explore':
                if (currentAstro.energy >= commandValue) {
                    currentAstro.energy -= commandValue;
                    console.log(`${astronautName} has successfully explored a new area and now has ${currentAstro.energy} energy!`);
                } else {
                    console.log(`${astronautName} does not have enough energy to explore!`);
                }
                break;
            case 'Refuel':
                const currentEnergy = currentAstro.energy;
                const newEnergy = Math.min(200, currentEnergy + commandValue);
                currentAstro.energy = newEnergy;
                console.log(`${astronautName} refueled their energy by ${newEnergy - currentEnergy}!`);
                break;
            case 'Breathe':
                const currentOxygen = currentAstro.oxygen;
                const newOxygen = Math.min(100, currentAstro.oxygen + commandValue)
                currentAstro.oxygen = newOxygen
                console.log(`${astronautName} took a breath and recovered ${newOxygen - currentOxygen} oxygen!`);
                break;
        }

        commandLine = commandArgs.shift()
    }

    for (const astro in astronautsTeam) {
        console.log(`Astronaut: ${astro}, Oxygen: ${astronautsTeam[astro].oxygen}, Energy: ${astronautsTeam[astro].energy}`);
    }
}


// solve(['3',
// 'John 50 120',
// 'Kate 80 180',
// 'Rob 70 150',
// 'Explore - John - 50',
// 'Refuel - Kate - 30',
// 'Breathe - Rob - 20',
// 'End']
// )

solve(['4',
'Alice 60 100',
'Bob 40 80',
'Charlie 70 150',
'Dave 80 180',
'Explore - Bob - 60',
'Refuel - Alice - 30',
'Breathe - Charlie - 50',
'Refuel - Dave - 40',
'Explore - Bob - 40',
'Breathe - Charlie - 30',
'Explore - Alice - 40',
'End']
)