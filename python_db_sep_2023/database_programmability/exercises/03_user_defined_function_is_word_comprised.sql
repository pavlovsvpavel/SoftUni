CREATE OR REPLACE FUNCTION fn_is_word_comprised(
    IN set_of_letters VARCHAR(50),
    IN word VARCHAR(50),
    OUT result BOOLEAN
    )
RETURNS BOOLEAN AS

$$
BEGIN
    result := TRIM(LOWER(word), LOWER(set_of_letters)) = '';
END;

$$
LANGUAGE plpgsql;

SELECT fn_is_word_comprised('ois tmiah%f', 'halves');
-- SELECT fn_is_word_comprised('ois tmiah%f', 'Sofia');
-- SELECT fn_is_word_comprised('bobr', 'Rob');
-- SELECT fn_is_word_comprised('papopep', 'toe');
-- SELECT fn_is_word_comprised('R@o!B$B', 'Bob')
