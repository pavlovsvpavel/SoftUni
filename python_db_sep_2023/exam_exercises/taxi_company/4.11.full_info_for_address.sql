CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE sp_courses_by_address(
    IN address_name VARCHAR(100)
    )
AS

$$
BEGIN
    TRUNCATE search_results;
    INSERT INTO search_results (
                    address_name,
                    full_name,
                    level_of_bill,
                    make,
                    condition,
                    category_name
                )
    SELECT
    a.name AS address_name,
    cl.full_name,
    CASE
        WHEN c.bill <= 20 THEN 'Low'
        WHEN c.bill <= 30 THEN 'Medium'
        ELSE 'High'
    END AS level_of_bill,
    car.make,
    car.condition,
    cat.name AS category_name
    FROM
        courses AS c
    INNER JOIN
        addresses AS a
        ON
        c.from_address_id = a.id
    INNER JOIN
        clients AS cl
        ON
        cl.id = c.client_id
    INNER JOIN
        cars AS car
        ON
        c.car_id = car.id
    INNER JOIN
        categories AS cat
        ON
        cat.id = car.category_id
    WHERE
        a.name = address_name
    ORDER BY
        car.make,
        cl.full_name;
END;
$$
LANGUAGE plpgsql;

-- CALL sp_courses_by_address('700 Monterey Avenue');
-- SELECT * FROM search_results;
--
-- CALL sp_courses_by_address('66 Thompson Drive');
-- SELECT * FROM search_results;

