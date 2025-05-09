SELECT p.F_Name AS First_Name, 
	p.L_Name AS Last_Name, 
	p.SALARY, d.Department_NAME AS Department 
FROM Personnel p LEFT JOIN Departments d 
ON p.Department_ID = d.Department_ID
WHERE p.SALARY = (SELECT MAX(SALARY) FROM Personnel)