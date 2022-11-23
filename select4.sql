--4. Средний балл в потоке.
SELECT 
	round(AVG(g.grade),2) as average_grade	 
FROM 
	grades g