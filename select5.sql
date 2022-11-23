--5. Какие курсы читает преподаватель.
SElECT 
	t.full_name as teacher,
	s.name as subject
FROM subjects s 
	LEFT JOIN teachers t  on s.teacher_id = t.id
WHERE t.id = 1	
ORDER BY t.full_name