function solve(people, group, day) {
    let pricePerPerson = 0;
    let totalPrice = 0;

    if (day === 'Friday') {
        switch (group) {
            case 'Students':
                pricePerPerson = 8.45;
                break;
            case 'Business':
                pricePerPerson = 10.90;
                break;
            case 'Regular':
                pricePerPerson = 15;
                break;
        }
    } else if (day === 'Saturday') {
        switch (group) {
            case 'Students':
                pricePerPerson = 9.80;
                break;
            case 'Business':
                pricePerPerson = 15.60;
                break;
            case 'Regular':
                pricePerPerson = 20;
                break;
        } 
    } else if (day === 'Sunday') {
        switch (group) {
            case 'Students':
                pricePerPerson = 10.46;
                break;
            case 'Business':
                pricePerPerson = 16;
                break;
            case 'Regular':
                pricePerPerson = 22.50;
                break;
        }
    }

    totalPrice = people * pricePerPerson

    if (group === 'Students' && people >= 30) {
        totalPrice *= 0.85;
    } else if (group === 'Business' && people >= 100) {
        totalPrice -= pricePerPerson * 10
    } else if (group === 'Regular' && (people >= 10 && people <= 20)) {
        totalPrice *= 0.95
    }

    console.log(`Total price: ${totalPrice.toFixed(2)}`);
}

solve(30,"Students","Sunday")
solve(40,"Regular","Saturday")
