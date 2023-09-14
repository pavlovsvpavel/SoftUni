ALTER TABLE minions_info
ADD COLUMN email VARCHAR(20),
ADD COLUMN equipped BOOLEAN NOT NULL,
ADD CONSTRAINT equipped_const CHECK(true or false)
