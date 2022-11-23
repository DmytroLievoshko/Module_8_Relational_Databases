--2. 1 студент с наивысшим средним баллом по одному предмету.
SELECT 
	s.full_name as student,
	sub.name as subject,
	round(AVG(g.grade),2) as average_grade	 
FROM 
	students s
	JOIN grades g  on s.id = g.student_id AND g.subject_id = 2
		LEFT JOIN subjects sub on g.subject_id = sub.id 
GROUP BY s.full_name, sub.name  
ORDER BY average_grade DESC 
LIMIT 1