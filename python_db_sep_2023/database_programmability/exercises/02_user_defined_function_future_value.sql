CREATE OR REPLACE FUNCTION fn_calculate_future_value(
    IN initial_sum NUMERIC,
    IN yearly_interest_rate NUMERIC,
    IN number_of_years INT,
    OUT future_value NUMERIC
    )
RETURNS NUMERIC AS

$$
BEGIN
    future_value :=
        TRUNC((initial_sum * POW((1 + yearly_interest_rate), number_of_years)), 4);
END;
$$
LANGUAGE plpgsql;

-- SELECT fn_calculate_future_value (1000, 0.1, 5);
-- SELECT fn_calculate_future_value(2500, 0.30, 2);
-- SELECT fn_calculate_future_value(500, 0.25, 10)