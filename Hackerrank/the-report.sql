-- https://www.hackerrank.com/challenges/the-report/problem
SELECT CASE WHEN Grade < 8 THEN NULL ELSE Name END AS Name, Grade, Marks
FROM Students, Grades
WHERE Marks BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade DESC, Name, Marks