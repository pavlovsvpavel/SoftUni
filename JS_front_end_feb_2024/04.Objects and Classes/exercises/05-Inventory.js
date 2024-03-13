function solve(input) {
    class Hero {
        constructor(heroName, heroLevel, heroItems) {
            this.heroName = heroName,
            this.heroLevel = heroLevel,
            this.heroItems = heroItems
        }
    }

    allHeroes = [];

    for (const element of input) {
        let [heroName, heroLevel, ...heroItems] = element.split(" / ");
        heroLevel = Number(heroLevel);
        allHeroes.push(new Hero(heroName, heroLevel, ...heroItems));
    }

    allHeroes.sort((a, b) => a.heroLevel - b.heroLevel)

    for (const hero of allHeroes) {
        console.log(`Hero: ${hero.heroName}`);
        console.log(`level => ${hero.heroLevel}`);
        console.log(`items => ${hero.heroItems}`);
    }
}


solve([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
    ]);