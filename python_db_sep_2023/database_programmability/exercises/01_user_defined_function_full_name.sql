CREATE OR REPLACE FUNCTION fn_full_name(first_name VARCHAR(20), last_name VARCHAR(20))
RETURNS VARCHAR AS
$$
DECLARE
    full_name VARCHAR;
BEGIN
   IF first_name IS NULL THEN
       full_name := INITCAP(last_name);
   ELSIF last_name IS NULL THEN
       full_name := INITCAP(first_name);
   ELSE
       full_name := INITCAP(CONCAT(first_name, ' ', last_name));
   END IF;
   RETURN full_name;
END;
$$
LANGUAGE plpgsql;

SELECT fn_full_name('fred', 'sanford');
SELECT fn_full_name('', 'SIMPSONS');
SELECT fn_full_name('JOHN', '');
SELECT fn_full_name(NULL, NULL);
