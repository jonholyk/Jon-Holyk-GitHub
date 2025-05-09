SELECT 
    STATE,
    ROUND(AVG(SALARY), 2) AS Avg_Salary
FROM 
    Personnel
GROUP BY 
    STATE
ORDER BY 
    Avg_Salary DESC;