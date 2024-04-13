function solve(input) {
    const numberOfHeroes = Number(input[0]);

    const heroesTeam = {};

    const heroesDetails = input.slice(1, numberOfHeroes + 1);
    for (let line of heroesDetails) {
        const [heroName, hp, bullets] = line.split(' ');
        heroesTeam[heroName] = {
            hp: Number(hp),
            bullets: Number(bullets),
        }
    }
    
    const commands = input.slice(numberOfHeroes + 1);
    let commandLine = commands.shift();

    while (commandLine != 'Ride Off Into Sunset') {
        let [command, heroName, ...others] = commandLine.split(' - ');

        const currentHero = heroesTeam[heroName];
        if (command == 'FireShot') {
            let target = others[0];

            if (currentHero.bullets > 0) {
                currentHero.bullets -= 1;
                console.log(`${heroName} has successfully hit ${target} and now has ${currentHero.bullets} bullets!`);
            } else {
                console.log(`${heroName} doesn't have enough bullets to shoot at ${target}!`);
            }

        } else if (command == 'TakeHit') {
            let [damage, attacker] = [...others];
            damage = Number(damage);
            currentHero.hp -= damage;

            if (currentHero.hp > 0) {
                console.log(`${heroName} took a hit for ${damage} HP from ${attacker} and now has ${currentHero.hp} HP!`);
            } else {
                delete heroesTeam[heroName];
                console.log(`${heroName} was gunned down by ${attacker}!`);
            }

        } else if (command == 'Reload') {
            let currentBullets = currentHero.bullets;
            if (currentBullets < 6) {
                let bulletsToReload = 6 - currentBullets; 
                currentHero.bullets = 6;
                console.log(`${heroName} reloaded ${bulletsToReload} bullets!`);
            } else {
                console.log(`${heroName}'s pistol is fully loaded!`);
            }
        } else if (command == 'PatchUp') {
            let amount = Number(others[0]);
            let currentHp = currentHero.hp;

            if (currentHp != 100) {
                newHp = Math.min(100, currentHero.hp + amount);
                currentHero.hp = newHp;
                console.log(`${heroName} patched up and recovered ${amount} HP!`);
            } else {
                console.log(`${heroName} is in full health!`);
            }

        }

        commandLine = commands.shift();
    }

    for (const hero in heroesTeam) {
        console.log(`${hero}`);
        console.log(` HP: ${heroesTeam[hero].hp}`);
        console.log(` Bullets: ${heroesTeam[hero].bullets}`);
    }
}


// solve(["2",
// "Gus 100 0",
// "Walt 100 6",
// "FireShot - Gus - Bandit",
// "TakeHit - Gus - 100 - Bandit",
// "Reload - Walt",
// "Ride Off Into Sunset"])

// solve(["2",
// "Jesse 100 4",
// "Walt 100 5",
// "FireShot - Jesse - Bandit",
//  "TakeHit - Walt - 30 - Bandit",
//  "PatchUp - Walt - 20" ,
//  "Reload - Jesse",
//  "Ride Off Into Sunset"])


 solve(["2",
 "Gus 100 4",
 "Walt 100 5",
 "FireShot - Gus - Bandit",
 "TakeHit - Walt - 100 - Bandit",
 "Reload - Gus",
 "Ride Off Into Sunset"])
