--9. Список курсов, которые посещает студент
SELECT 
	s.full_name as student,
	s2.name as subject
FROM students_subjects ss 
	LEFT JOIN students s ON ss.student_id = s.id 
	LEFT JOIN subjects s2  ON ss.subject_id = s2.id 
WHERE s.id = 30