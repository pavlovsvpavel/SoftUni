CREATE TABLE minions_birthdays(
	id SERIAL PRIMARY KEY,
	name VARCHAR(150) NOT NULL,
	date_of_birth DATE NOT NULL,
	age INTEGER NOT NULL,
	present VARCHAR(100) NOT NULL,
	party TIMESTAMPTZ NOT NULL
);
