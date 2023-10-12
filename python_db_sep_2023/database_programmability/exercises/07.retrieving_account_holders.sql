CREATE OR REPLACE PROCEDURE
    sp_retrieving_holders_with_balance_higher_than (
    searched_balance NUMERIC
    )
AS
$$
DECLARE
    info RECORD;
BEGIN
    FOR info IN
        SELECT
            CONCAT_WS(' ', ah.first_name, ah.last_name) AS full_name,
            SUM(a.balance) AS total_balance
        FROM
            accounts AS a
        INNER JOIN
            account_holders AS ah
            ON
            a.account_holder_id = ah.id
        GROUP BY
            full_name
        HAVING
            SUM(a.balance) > searched_balance
        ORDER BY
            full_name
    LOOP
        RAISE NOTICE '% - %', info.full_name, info.total_balance;
    END LOOP;
END;
$$
LANGUAGE plpgsql;

-- CALL sp_retrieving_holders_with_balance_higher_than(200000)