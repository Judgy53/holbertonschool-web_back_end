-- Script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- Query the number of fans by country
SELECT origin, SUM(fans) as nb_fans 
FROM metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;
