SELECT concat(Name, '(', substring(Occupation, 1, 1), ')') FROM OCCUPATIONS ORDER BY NAME;

SELECT concat('There are a total of ', count(*), ' ', LOWER(Occupation), 's.') AS TOTAL FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY TOTAL;

