SELECT DISTINCT city FROM STATION WHERE NOT ((CITY LIKE '%a' or CITY LIKE '%e' or CITY LIKE '%i' or CITY LIKE '%o' or CITY LIKE '%u') AND (CITY LIKE 'a%' or CITY LIKE 'e%' or CITY LIKE 'i%' or CITY LIKE 'o%' or CITY LIKE 'u%'))