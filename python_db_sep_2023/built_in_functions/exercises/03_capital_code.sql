ALTER TABLE countries
ADD COLUMN capital_code CHAR(2) DEFAULT NULL;

UPDATE countries
SET capital_code = SUBSTRING(capital, 1, 2)
WHERE capital_code IS NULL;
