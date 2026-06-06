-- SQL script that ranks country origins of bands by the number of fans
-- Selects origin and the total number of fans, ordered by fans in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
