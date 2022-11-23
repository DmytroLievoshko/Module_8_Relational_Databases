--8. Оценки студентов в группе по предмету на последнем занятии.
SELECT 
	g.name as [group],
	subjects.name as subject,
	s.full_name as student,	
	grades.grade,
	grades.date_of 
FROM students s 
	JOIN groups g on s.group_id = g.id AND g.id = 2
	JOIN grades ON s.id = grades.student_id AND grades.subject_id = 2 
		JOIN (SELECT 
				g.subject_id,
				MAX(g.date_of) as last_date  	
			  FROM grades g
			  GROUP BY g.subject_id) as last_d ON grades.subject_id = last_d.subject_id AND grades.date_of = last_d.last_date
		LEFT JOIN subjects ON grades.subject_id = subjects.id