--12. Средний балл, который ставит преподаватель.
SELECT
	t.full_name as teacher,
	round(AVG(g.grade),2) as average_grade	
FROM grades g  
	LEFT JOIN subjects s2  ON g.subject_id = s2.id
		JOIN teachers t ON s2.teacher_id = t.id AND t.id = 1
GROUP BY t.full_name