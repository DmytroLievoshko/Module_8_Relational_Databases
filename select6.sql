--6. Список студентов в группе.
SELECT 
	g.name as [group],
	s.full_name  as student
FROM students s
	LEFT JOIN groups g on s.group_id = g.id 
WHERE g.id = 1
ORDER BY s.full_name