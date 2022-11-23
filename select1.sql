--1. 5 студентов с наибольшим средним баллом по всем предметам.
SELECT 
	s.full_name as student, 
	round(AVG(g.grade),2) as average_grade  
FROM 
	students s
	LEFT JOIN grades g  on s.id = g.student_id  
GROUP BY s.full_name 
ORDER BY average_grade DESC 
LIMIT 5