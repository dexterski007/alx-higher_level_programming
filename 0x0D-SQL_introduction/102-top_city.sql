-- display top 3 cities in july and august
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE MONTH IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
