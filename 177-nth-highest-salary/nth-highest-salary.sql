CREATE FUNCTION getNthHighestSalary(N INT) 
RETURNS INT
DETERMINISTIC
BEGIN
    Declare sal1 int;
        SELECT DISTINCT salary into sal1
        FROM (SELECT salary,DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
            FROM Employee) t
        WHERE rnk = N
        LIMIT 1;
    return sal1;
END;

