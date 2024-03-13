function solve(currentStock, orderedStock) {
    let products = {};

    for (i = 0; i < currentStock.length; i++) {
        if (i % 2 !== 0) {
            let productName = currentStock[i - 1];
            let quantity = Number(currentStock[i]);

            products[productName] = quantity;
        }
    }

    for (j = 0; j < orderedStock.length; j++) {
        if (j % 2 !== 0) {
            let productName = orderedStock[j - 1];
            let quantity = Number(orderedStock[j]);

            if (products.hasOwnProperty(productName)) {
                products[productName] += quantity
            } else {
                products[productName] = quantity
            }
        } 
    }

    for (const key in products) {
        if (products.hasOwnProperty.call(products, key)) {
            const value = products[key];
            console.log(`${key} -> ${value}`);
        }
    }  
}



solve(['Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'],
    ['Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30']);