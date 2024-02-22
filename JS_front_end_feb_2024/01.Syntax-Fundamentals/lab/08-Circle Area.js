function solve(param) {
    let circle_area = 0;
    if (typeof(param) === 'number') {
        circle_area = Math.PI * (param ** 2);
        console.log(circle_area.toFixed(2));
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeof(param)}.`);
    }
}

solve(5)
solve('name')