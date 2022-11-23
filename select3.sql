--3. средний балл в группе по одному предмету.
SELECT 
	gr.name  as [group],
	sub.name as subject,
	round(AVG(g.grade),2) as average_grade	 
FROM 
	students s
	LEFT JOIN groups gr on s.group_id = gr.id 
	JOIN grades g  on s.id = g.student_id AND g.subject_id = 2
		LEFT JOIN subjects sub on g.subject_id = sub.id 
GROUP BY gr.name, sub.name  
ORDER BY average_grade DESC