SELECT
    name,
    date_trunc('second', start_date) as start_date
FROM
    projects
WHERE
    name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;
