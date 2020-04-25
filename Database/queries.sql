-- SELECT DISTINCT
-- The select distinct statement is used to return only distinct (different) values from the table
select distinct country from customers;

-- ORDER BY
-- The ORDER BY statement is used to sort the result set in ascending or descending order
select * from interaction_request_jobs order by job_id;

-- SELECT MIN
-- The MIN() function returns the minimum value from the result set
select min(job_id) from interaction_request_jobs;

-- SELECT MAX
-- The MAX() function returns the maximum value from the result set
select max(job_id) from interaction_request_jobs;

-- SELECT COUNT
-- Returns the total numbers of records in the result set based on condition
select count(*) from interactions where parent_id is null;

-- SELECT AVG
-- Returns the average value of a numeric column
select AVG(Price) from Products;

-- SELECT SUM
-- Returns the sum of the numeric values of a column, ignoring the null values
select sum(price) from products;

-- LIKE
-- The like operator is used with the where clause to search for results with a specific pattern
select * from names where name like 'a%';
-- 'a%' -> Finds any value that starts with a
-- '%a' -> Finds any value that ends with a
-- '%a%' -> Finds any value that have a in any position
-- '_r%' -> Finds any value with r in the second position
-- 'a_%' -> Finds any value that starts with a and are atleast 2 characters in length
-- 'a__%' -> Finds any value that starts with a and are atleast 3 characters in length
-- 'a%o' -> Finds any value that starts with a and ends with o

-- '%' and '_' are all wildcard characters. Wild card characters are basically used to subsitute one
-- or more characters in a string

-- IN
-- The in operator helps in specifying mulatiple values in a where clause.
select * from customers where country in ('Germany', 'France', 'UK');
select * from customers where country not in ('Germany', 'France', 'UK');
select * from customers where country in (select country from suppliers);

-- BETWEEN
-- The between operator selects a value within a given range. The between operator
-- is inclusive that means it includes the starting and the end values as well
select * from products where price between 10 and 20;
select * from products where price not between 10 and 20;

-- ALIAS
-- Aliases are used to give a temporary name to a table or a column in a table a temporary name
select customer_id  as id, customer_name as customer from customers;

-- JOINS
-- A join clause is used to combine rows from two or more tables based on a
-- related column between them
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate
from Orders
inner join Customers on Orders.CustomerID=Customers.CustomerID;

-- INNER JOIN
-- Returns records that have matchine values in both the tables
-- LEFT (OUTER) JOIN
-- Returns all the records from the left table and the matched records from the right table.
-- RIGHT (OUTER) JOIN
-- Returns all the records from the ight table and the matched records from the left table.
-- FULL (OUTER) JOIN
-- Returns all records when there is a match in both tables
-- SELF JOIN
-- Retuns all records after joining in the same table

-- INNER JOIN
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

-- LEFT OUTER JOIN
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName;

-- RIGHT OUTER JOIN
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;

-- FULL OUTER JOIN
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;

-- SELF JOIN
SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
AND A.City = B.City
ORDER BY A.City;

-- UNION
-- Union combines the result sets of two or more select statements.
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;

-- Group By
-- The GROUP BY statement groups rows that have the same values into summary rows,
-- like "find the number of customers in each country".
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

-- EXISTS
-- The exists operator is used to test for the existence of any record in a subquery
-- The exists operator retuns true for a record if a record exists in a subquery
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM Products
  WHERE Products.SupplierID = Suppliers.supplierID AND Price < 20);

-- HAVING
-- The HAVING clause was added to SQL because the WHERE keyword
-- could not be used with aggregate functions.
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) > 5;
