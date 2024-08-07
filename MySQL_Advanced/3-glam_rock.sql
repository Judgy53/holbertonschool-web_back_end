-- Script that lists all Glam rock bands, ranked by their longevity

-- Query the bands and their longevity
SELECT band_name, IFNULL(split, 2020) - formed as lifespan
FROM metal_bands 
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
