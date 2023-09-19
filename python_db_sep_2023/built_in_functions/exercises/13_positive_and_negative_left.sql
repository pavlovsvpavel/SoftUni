SELECT
    peak_name,
    LEFT(peak_name, 4) as "Positive Left",
    LEFT(peak_name, -4) as "Negative Left"
FROM
    peaks