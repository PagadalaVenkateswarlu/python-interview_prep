-- SELECT TOP 40 PERCENT * FROM table name


-- WHERE CustomerName LIKE 'a%' Finds any values that starts with "a"
-- WHERE CustomerName LIKE '%a' Finds any values that ends with "a"
-- WHERE CustomerName LIKE '%or%'
-- WHERE CustomerName LIKE '_r%'
-- Finds any values that have "or" in any position
-- Finds any values that have "r" in the second position
-- WHERE CustomerName LIKE
-- 'a_%_%'
-- Finds any values that starts with "a" and are at least 3
-- characters in length
-- WHERE ContactName LIKE 'a%o' Finds any values that starts with "a" and ends with "o

------------------------------------------------------------------------------------------
--
-- SELECT NAME,AGE,MARKS,
--
-- case
--     when age>50 then 'old'
--     when age between 20 and 30 then 'young'
--     else 'minor'
-- end
--
-- FROM student
-- where age is not null
-- order by age
--
-- --------------------------------------CASE STATEMENT------------------------------------------------------
--
-- SELECT JOB_TITLE,FIRST_NAME,LAST_NAME,SALARY,
--        CASE
--            WHEN JOB_TITLE ='SOFTWARE ENGINNER' THEN SALARY + (SALARY*10)
--            WHEN JOB_TITLE='SENIOR SOFTWARE ENGINEER' THEN SALARY + (SALARY*20)
--        END AS FINAL_HIKE
-- FROM EMPLOYEE E JOIN SALARY S ON E.EMPLOYEE_ID = S.EMPLOYEE_ID
--
-- ------------------------------------------HAVING STATEMENT-----------------------------------------------------
--
-- SELECT Name,AGE,count(SALARY)
-- FROM SALARY S JOIN EMPLOYEE E ON S.EMPLOYEE_ID=E.EMPLOYEE_ID
-- GROUP BY SALARY
-- HAVING COUNT(SALARY)>1;
--
-- -----------------------------------AVG HAVING ------------------------------------------------------
-- SELECT Name,AGE,AVG(SALARY)
-- FROM SALARY S JOIN EMPLOYEE E ON S.EMPLOYEE_ID=E.EMPLOYEE_ID
-- GROUP BY SALARY
-- HAVING AVG(SALARY)>100
-- ORDER BY AVG(SALARY) DESC;
-- -------------------------------SUB QUERY IN SELECT------------------------------------------------
-- SELECT NAME, (AVG(SALARY) FROM  EMPLOYEE) AS EMPLOYEE_AVG_SALARY FROM SALARY;
--
-- ------------------------------SUB QUERY PARTITION--------------------------------------------------
-- SELECT NAME,AGE ,AVG(SAALRY) OVER() (PARTTION BY SALARY ORDER BY DESC) AS SAL) FROM EMPLOYEE;
--
-- ----------------------------SUB QUERY IN FROM STATEMENT--------------------------------------------
-- SELECT * FROM (SELECT SALARY FROM EMPLOYEE) A ORDER BY A.EMPLOYEE_ID


------------------------------------------------------SQL JOINS-------------------------------------
-- 1.INNER JOIN
-- 2.SELF JOIN
-- 3.OUTER JOIN
-- 4.CROSS JOIN
-- 5.LEFT OUTER JOIN
-- 6.RIGHT OUTER JOIN
-- 7.FULL OUTER JOIN
---------------------------------- CTE(COMMON TABLE EXPRESSION---------------------------
-- CTE :
    --create temporary result set which is used to manipulate the complex sub-queries data.
    --created in memory rather than Teamdb database,so cannot create any index on CTE.
--Example:
--     WITH CTE_EXPRESSION AS(
-- SELECT * FROM TABLE
-- WHERE SALARY>3000
--     )
-- SELECT * FROM CTE_EXPRESSION WHERE TOTAL>20;

------------------------------------WINDOW FUNCTIONS-----------------------------------
-- ROW_NUMBER() :
    --get a unique sequential number for each row
    --get different ranks for the row having similar values

-- example

--     SELECT *,ROW_NUMBER() OVER(ORDER BY SALARY DESC) SALARYRANK FROM EMPLOYEESALARY

-- RANK()
    --specify rank for each row in the result set.
    --use partition by to performs calculation on each group
    -- each subset get rank as per salary in descending order
    --skip a rank if have similar values
-- example
--         SELECT *,RANK()  OVER(PARTITION BY JOBTITLE ORDER BY SALARY DESC) SALARY_RANK
--         FROM EMPLOYEESALARY
--         ORDER BY JOBTITLE,SALARY_RANK

--NOT USING PARTITION BY
    --get same ranks for the row having similar values

--     SELECT * ,RANK() OVER(ORDER BY SALARY DESC) SALARY_RANK
--     FROM EMPLOYEESALARY
--     ORDER BY SALARY_RANK

-- DENSE_RANK()
    --if have duplicate values,SQL assigns different ranks to those rows.
    -- will get the same rank for duplicate or similar values
    -- maintains the rank and does not give any gap for the values
    -- SELECT * ,DENSE_RANK() OVER(ORDER BY SALARY DESC) SALARY_RANK
    --FROM EMPLOYEESALARY
    --ORDER BY SALARY_RANK


--NTILE()
    --can specify required how many group of result,and it will rank accordingly.
    --SELECT *,NTITLE(3) OVER(ORDER BY SALARY DESC) SalaryRank
    --From EmployeeSalary
    -- Order by SalaryRank

-- Primary key
    --It is a column(or set of columns) in a table that uniquely identifies each row.(a unique id)
    --There is only one primary key in table & it should be not null.

-- Foreign key
    --A foreign key is a column(or set of columns) in a table that refers to the primary key in another table.
    -- There can be multiple FKs.
    -- FKs can have duplicate & null values.


--View
-- A view is a virtual table based on the result-set of an SQL statement.

-- example
-- CREATE VIEW VENKAT AS SELECT * FROM TABLE_NAME
--
-- SELECT * FROM VENKAT

--A view always shows up-to-date data.The database engine recreates the view ,every time a user queries it.

--Cascading for FK:
--   on Delete Cascade: When



--Having Clause:
--     Similar to where i.e.applies some condition on rows
--     Used when we want to apply any condition after grouping

--Group By Clause:
--     Groups rows that have the same values into summary rows
--     It collects data from multiple records and groups the result by one or more column.
-- Generally we use group by with some aggregation function.

-- Aggregate Functions
-- Aggregare functions perform a calculation on a set of values,and return a single value.
--     COUNT()
--     MAX()
--     MIN()
--     SUM()
--     AVG()


--SQL Constraints
-- --SQL constraints are used to specify rules for data in a table
-- NOT NULL
-- UNIQUE
-- PAIMARY KEY
-- FOREIGN KEY  - prevents actions that would destroy links between tables
-- DEFAULT


--------------------------------------------------------------------SQL CODING-----------------------------------------------------------
--second highest salary

    -- select max(salary)
    -- from employee
    -- where salary<(select max(salary) from employee)
--------------------------------Nth highest salary---------------------------------------------------------------------------------------
-- select DISTINCT age
-- from (SELECT DISTINCT age, DENSE_RANK() OVER(order by age desc) as age_rank from customers) as rnk
-- where age_rank=4;
----------------------------------------------------------------------
-- How to list all employees hired in the last 6 months?
-- SELECT *
-- FROM employees
-- WHERE hire_date > ADDDATE(CURDATE(), INTERVAL -6 MONTH)


---------------------------------------------------------------------------------

-- How to find employees who joined the company in the same month and
-- year as their manager?
--
-- SELECT e.employee_id, e.name
-- FROM employees e
-- JOIN employees m ON e.manager_id = m.employee_id
-- WHERE MONTH(e.join_date) = MONTH(m.join_date)
-- AND YEAR(e.join_date) = YEAR(m.join_date)





