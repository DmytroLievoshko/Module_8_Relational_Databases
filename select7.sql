--7. Оценки студентов в группе по предмету.
SELECT 
	g.name as [group],
	subjects.name as subject,
	s.full_name as student,	
	grades.grade,
	grades.date_of 
FROM students s 
	JOIN groups g on s.group_id = g.id AND g.id = 2
	JOIN grades ON s.id = grades.student_id AND grades.subject_id = 2
		LEFT JOIN subjects ON grades.subject_id = subjects.id