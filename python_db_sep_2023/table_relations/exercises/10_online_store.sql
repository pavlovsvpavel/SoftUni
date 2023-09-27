CREATE TABLE IF NOT EXISTS item_types(
    id SERIAL PRIMARY KEY,
    item_type_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS items(
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_type_id INT,
    CONSTRAINT fk_items_item_types
        FOREIGN KEY (item_type_id)
            REFERENCES item_types(id)
);

CREATE TABLE IF NOT EXISTS cities(
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers(
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(30) NOT NULL,
    birthday DATE NOT NULL,
    city_id INT,
    CONSTRAINT fk_customers_cities
        FOREIGN KEY (city_id)
            REFERENCES cities(id)
);

CREATE TABLE IF NOT EXISTS orders(
    id SERIAL PRIMARY KEY,
    customer_id INT,
    CONSTRAINT fk_orders_customers
        FOREIGN KEY (customer_id)
            REFERENCES customers(id)
);

CREATE TABLE IF NOT EXISTS order_items(
    order_id INT,
    item_id INT,
    CONSTRAINT fk_order_items_orders
        FOREIGN KEY (order_id)
            REFERENCES orders(id),
    CONSTRAINT fk_order_items_items
        FOREIGN KEY (item_id)
            REFERENCES items(id)
);
