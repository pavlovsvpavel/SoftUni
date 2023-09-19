SELECT
    peak_name,
    RIGHT(peak_name, 4) as "Positive Left",
    RIGHT(peak_name, -4) as "Negative Left"
FROM
    peaks