function solve(arrayOfStrings) {
    let cats = [];

    class Cat {
        constructor(catName, age) {
            this.catName = catName;
            this.age = age;
        }

        meow() {
            console.log(`${this.catName}, age ${this.age} says Meow`);
        }
    }

    for (let i = 0; i < arrayOfStrings.length; i++) {
        [catName, age] = arrayOfStrings[i].split(' ');
        cats.push(new Cat(catName, age));
    }

    for (const cat of cats) {
        cat.meow();
    }
}


solve(['Mellow 2', 'Tom 5'])
solve(['Candy 1', 'Poppy 3', 'Nyx 2'])