CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    release_year INT,
    rating FLOAT,
    category_name VARCHAR(50),
    publisher_name VARCHAR(50),
    min_players VARCHAR(50),
    max_players VARCHAR(50)
);

CREATE OR REPLACE PROCEDURE usp_search_by_category(
IN category VARCHAR(50)
)
AS

$$
BEGIN
    TRUNCATE search_results;
    INSERT INTO search_results
        (name, release_year, rating, category_name, publisher_name, min_players, max_players)

    SELECT
        b.name,
        b.release_year,
        b.rating,
        c.name,
        p.name,
        CONCAT(pr.min_players, ' ', 'people'),
        CONCAT(pr.max_players,' ', 'people')
    FROM
        board_games AS b
    INNER JOIN
        categories AS c
        ON
        b.category_id = c.id
    INNER JOIN
        publishers AS p
        ON
        p.id = b.publisher_id
    INNER JOIN
        players_ranges AS pr
        ON
        pr.id = b.players_range_id
    WHERE
        c.name = category
    ORDER BY
        p.name,
        b.release_year DESC;
END;
$$
LANGUAGE plpgsql;


CALL usp_search_by_category('Wargames');
SELECT * FROM search_results;
