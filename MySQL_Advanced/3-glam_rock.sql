-- SQL script that lists all bands with Glam rock as their main style
-- Ranked by their longevity up to 2024

SELECT band_name, (COALESCE(split, 2024) - formed) AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
