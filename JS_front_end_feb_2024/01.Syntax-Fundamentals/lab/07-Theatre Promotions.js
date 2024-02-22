function solve(day, age) {
    let ticket_price = 0;
    if (age >= 0 && age <= 18) {
        switch (day) {
            case 'Weekday':
                ticket_price = '12$';
                break;
            case 'Weekend':
                ticket_price = '15$';
                break;
            case 'Holiday':
                ticket_price = '5$';
                break;
        }
        console.log(ticket_price);
    } else if (age >= 0 && age <= 64) {
            switch (day) {
                case 'Weekday':
                    ticket_price = '18$';
                    break;
                case 'Weekend':
                    ticket_price = '20$';
                    break;
                case 'Holiday':
                    ticket_price = '12$';
                    break;
            }
            console.log(ticket_price); 
    } else if (age >= 0 && age <= 122) {
            switch (day) {
                case 'Weekday':
                    ticket_price = '12$';
                    break;
                case 'Weekend':
                    ticket_price = '15$';
                    break;
                case 'Holiday':
                    ticket_price = '10$';
                    break;
            }
            console.log(ticket_price);
    } else {
        console.log("Error!");
    }
}

solve('Weekday', 42)
solve('Holiday', -12)
solve('Holiday', 15)