-- list cities
SELECT id, name FROM cities
WHERE state_id = (
SELECT id FROM states WHERE name = 'CALIFORNIA')
ORDER BY cities.id ASC;
