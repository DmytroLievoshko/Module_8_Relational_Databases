--10. Список курсов, которые студенту читает преподаватель.
SELECT 
	s.full_name as student,
	s2.name as subject,
	t.full_name as teacher
FROM students_subjects ss 
	JOIN students s ON ss.student_id = s.id AND s.id = 30 
	LEFT JOIN subjects s2  ON ss.subject_id = s2.id
		JOIN teachers t ON s2.teacher_id = t.id AND t.id = 1