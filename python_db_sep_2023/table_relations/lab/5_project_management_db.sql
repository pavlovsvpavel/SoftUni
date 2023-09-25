CREATE TABLE IF NOT EXISTS clients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS projects(
    id SERIAL PRIMARY KEY,
    client_id INT,
    project_lead_id INT,
    CONSTRAINT fk_client
        FOREIGN KEY (client_id)
            REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    project_id INT,
    CONSTRAINT fk_project
        FOREIGN KEY (project_id)
            REFERENCES projects(id)
);

ALTER TABLE projects
ADD CONSTRAINT fk_project_lead
    FOREIGN KEY (project_lead_id)
        REFERENCES employees(id)
;
