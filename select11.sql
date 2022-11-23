--11. Средний балл, который преподаватель ставит студенту.
SELECT
	t.full_name as teacher,
	s.full_name as student,
	round(AVG(g.grade),2) as average_grade	
FROM grades g  
	JOIN students s ON g.student_id = s.id AND s.id = 30
	LEFT JOIN subjects s2  ON g.subject_id = s2.id
		JOIN teachers t ON s2.teacher_id = t.id AND t.id = 1
GROUP BY t.full_name, s.full_name