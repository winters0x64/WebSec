# SQL

Structured query language(SQL) is a query based language which is used as the default language for interacting with the database on a wide variety of database architectures like mysql,postgresql etc.

Some commonly used commands are as follows

# The Select statement and parameters that we can give

SELECT
SELECT is probably the most commonly-used SQL statement. You’ll use it pretty much every time you query data with SQL. It allows you to define what data you want your query to return.

For example, in the code below, we’re selecting a column called name from a table called customers.

SELECT name
FROM customers;

SELECT *
SELECT used with an asterisk (*) will return all of the columns in the table we’re querying.*

SELECT * FROM customers;

SELECT DISTINCT
SELECT DISTINCT only returns data that is distinct — in other words, if there are duplicate records, it will return only one copy of each.

The code below would return only rows with a unique name from the customers table.

SELECT DISTINCT name
FROM customers;

SELECT INTO
SELECT INTO copies the specified data from one table into another.

SELECT * INTO customers
FROM customers_backup;

SELECT TOP
SELECT TOP only returns the top x number or percent from a table.

The code below would return the top 50 results from the customers table:

SELECT TOP 50 * FROM customers;
The code below would return the top 50 percent of the customers table:

SELECT TOP 50 PERCENT * FROM customers;

AS
AS renames a column or table with an alias that we can choose. For example, in the code below, we’re renaming the name column as first_name:

SELECT name AS first_name
FROM customers;
FROM
FROM specifies the table we’re pulling our data from:

SELECT name
FROM customers;

WHERE
WHERE filters your query to only return results that match a set condition. We can use this together with conditional operators like =, >, <, >=, <=, etc.

SELECT name
FROM customers
WHERE name = ‘Bob’;

AND
AND combines two or more conditions in a single query. All of the conditions must be met for the result to be returned.

SELECT name
FROM customers
WHERE name = ‘Bob’ AND age = 55;

OR
OR combines two or more conditions in a single query. Only one of the conditions must be met for a result to be returned.

SELECT name
FROM customers
WHERE name = ‘Bob’ OR age = 55;

BETWEEN
BETWEEN filters your query to return only results that fit a specified range.

SELECT name
FROM customers
WHERE age BETWEEN 45 AND 55;

LIKE
LIKE searches for a specified pattern in a column. In the example code below, any row with a name that included the characters Bob would be returned.

SELECT name
FROM customers
WHERE name LIKE ‘%Bob%’;

Other operators for LIKE:

%x — will select all values that begin with x
%x% — will select all values that include x
x% — will select all values that end with x
x%y — will select all values that begin with x and end with y
_x% — will select all values have x as the second character
x_% — will select all values that begin with x and are at least two characters long. You can add additional _ characters to extend the length requirement, i.e. x___%

IN
IN allows us to specify multiple values we want to select for when using the WHERE command.

SELECT name
FROM customers
WHERE name IN (‘Bob’, ‘Fred’, ‘Harry’);


IS NULL
IS NULL will return only rows with a NULL value.

SELECT name
FROM customers
WHERE name IS NULL;

IS NOT NULL
IS NOT NULL does the opposite — it will return only rows without a NULL value.

SELECT name
FROM customers
WHERE name IS NOT NULL;

# The Create statement and the parameters that we can give

CREATE
CREATE can be used to set up a database, table, index or view.

CREATE DATABASE
CREATE DATABASE creates a new database, assuming the user running the command has the correct admin rights.

CREATE DATABASE dataquestDB;
CREATE TABLE
CREATE TABLE creates a new table inside a database. The terms int and varchar(255) in this example specify the datatypes of the columns we’re creating.

CREATE TABLE customers (
    customer_id int,
    name varchar(255),
    age int
);

# The Drop statement and the parameters that we can give

DROP
DROP statements can be used to delete entire databases, tables or indexes.

It goes without saying that the DROP command should only be used where absolutely necessary.

DROP DATABASE
DROP DATABASE deletes the entire database including all of its tables, indexes etc as well as all the data within it.

Again, this is a command we want to be very, very careful about using!

DROP DATABASE dataquestDB;
DROP TABLE
DROP TABLE deletes a table as well as the data within it.

DROP TABLE customers;

DROP INDEX
DROP INDEX deletes an index within a database.

DROP INDEX idx_name;

CREATE INDEX
CREATE INDEX generates an index for a table. Indexes are used to retrieve data from a database faster.

(More on index:
In SQL, an index is a database structure that provides a fast and efficient way of accessing data stored in a table. It is essentially a mapping of the values in specific columns of a table to their location on disk, allowing for quicker retrieval of data compared to scanning the entire table. Indexes can improve the performance of SELECT, UPDATE, and DELETE operations, as well as help enforce uniqueness constraints.
)
CREATE INDEX idx_name
ON customers (name);

CREATE VIEW
CREATE VIEW creates a virtual table based on the result set of an SQL statement. A view is like a regular table (and can be queried like one), but it is not saved as a permanent table in the database.

CREATE VIEW [Bob Customers] AS
SELECT name, age
FROM customers
WHERE name = ‘Bob’;

# The Update statement and its parameters

UPDATE
The UPDATE statement is used to update data in a table. For example, the code below would update the age of any customer named Bob in the customers table to 56.

UPDATE customers
SET age = 56
WHERE name = ‘Bob’;

# The Delete statement and its parameters

DELETE
DELETE can remove all rows from a table (using ), or can be used as part of a WHERE clause to delete rows that meet a specific condition.

DELETE FROM customers
WHERE name = ‘Bob’;

# The Alter table statement and its parameters

ALTER TABLE
ALTER TABLE allows you to add or remove columns from a table. In the code snippets below, we’ll add and then remove a column for surname. The text varchar(255) specifies the datatype of the column.

ALTER TABLE customers
ADD surname varchar(255);
ALTER TABLE customers
DROP COLUMN surname;

# The Aggregrate functions

AGGREGATE FUNCTIONS (COUNT/SUM/AVG/MIN/MAX)
An aggregate function performs a calculation on a set of values and returns a single result.

COUNT
COUNT returns the number of rows that match the specified criteria. In the code below, we’re using *, so the total row count for customers would be returned.*

SELECT COUNT(*)
FROM customers;*

SUM
SUM returns the total sum of a numeric column.

SELECT SUM(age)
FROM customers;
AVG
AVG returns the average value of a numeric column.

SELECT AVG(age)
FROM customers;
MIN
MIN returns the minimum value of a numeric column.

SELECT MIN(age)
FROM customers;
MAX
MAX returns the maximum value of a numeric column.

SELECT MAX(age)
FROM customers;


# The Group By statement

The GROUP BY statement groups rows with the same values into summary rows.The statement is often used with aggregate functions.

Here's an example to understand this better

SELECT product, SUM(quantity) FROM sales GROUP BY product;

This query will calculate the total quantity of each product sold in a table named sales. The result will be a table with two columns: product and SUM(quantity). Each row in the output table will represent a unique product in the sales table, and the SUM(quantity) column will contain the total quantity of that product sold.

For example, if the sales table contained the following data:

product | quantity
------- | --------
Apple   | 10
Banana  | 5
Apple   | 20
Banana  | 15

The output of the query would be:

product | SUM(quantity)
------- | -------------
Apple   | 30
Banana  | 20

In this example, the GROUP BY clause groups the rows with the same product name, and the SUM aggregate function calculates the total quantity of each product. The result is a table that shows the total quantity of each product sold.


HAVING
HAVING performs the same action as the WHERE clause. The difference is that HAVING is used for aggregate functions, whereas WHERE doesn’t work with them.

The below example would return the number of rows for each name, but only for names with more than 2 records.

SELECT COUNT(customer_id), name
FROM customers
GROUP BY name
HAVING COUNT(customer_id) > 2;

ORDER BY
ORDER BY sets the order of the returned results. The order will be ascending by default.

SELECT name
FROM customers
ORDER BY age;

DESC
DESC will return the results in descending order.

SELECT name
FROM customers
ORDER BY age DESC;

OFFSET
The OFFSET statement works with ORDER BY and specifies the number of rows to skip before starting to return rows from the query.

SELECT name
FROM customers
ORDER BY age
OFFSET 10 ROWS;

FETCH
FETCH specifies the number of rows to return after the OFFSET clause has been processed. The OFFSET clause is mandatory, while the FETCH clause is optional.

SELECT name
FROM customers
ORDER BY age
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;

# JOINS(INNER,LEFT,RIGHT,FULL)

Joins are used in SQL to combine data from multiple tables into a single result set. This allows you to retrieve information from multiple tables as if they were a single table, making it easier to work with the data.

# Inner join

INNER JOIN selects records that have matching values in both tables.

SELECT name
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id;

This statement will return a table whose contents will be data that has same cutomer_id in both the tables (name and orders)

# Left join

SELECT Customers.customer_name, Orders.order_total
FROM Customers
LEFT JOIN Orders
ON Customers.customer_id = Orders.customer_id;

A LEFT JOIN is a type of join operation in SQL that combines rows from two or more tables based on a related column between them and returns all rows from the left table (first table), and the matching rows from the right table (second table). If there is no match, NULL values will be returned for right table columns. It preserves the unmatched rows from the left table, which is why it is called a "left" join.

So what's the difference between a left join and inner join:

In inner join if there is a value in right table which is absent in the left table that particular data won't be returned but in case of left join it will preserve the value of  the left table if the that particular value is absent on the right table and  a null value will be shown in the right table.

# Right join

SELECT customers.name, customers.city, orders.amount
FROM customers
RIGHT JOIN orders
ON customers.id = orders.customer_id;

Similar to left join the only difference here is if the value is absent in the left table and is present in the right table then the value of the right table will be displayed and NULL value will be shown in the left table.

# Full join

SELECT customers.name, customers.city, orders.amount
FROM customers
FULL JOIN orders
ON customers.id = orders.customer_id;


A FULL JOIN, also known as a FULL OUTER JOIN, is a type of join operation in SQL (Structured Query Language) that combines records from both tables (left and right), and returns all matched and unmatched records from both tables. If there is no match, NULL values will be displayed for the missing side's columns.

Note that the unmatched records from both tables are still included in the result, but with NULL values for the columns from the missing side's table.

# Exists

SELECT * 
FROM Orders 
WHERE EXISTS (
    SELECT * 
    FROM Customers 
    WHERE Orders.CustomerID = Customers.CustomerID
    AND Customers.Country = 'USA'
);

In this example, the outer query selects all columns from the "Orders" table, and the inner query selects all columns from the "Customers" table where the "Country" column is equal to "USA". The "EXISTS" keyword is used in the outer query's "WHERE" clause to check if any rows are returned from the inner query, and if so, it returns the rows from the "Orders" table where the "CustomerID" matches the "CustomerID" in the inner query. In other words, the result of the query will include all orders placed by customers in the USA.

also select * from table_name where false; -> Wont return anything
    select * from table_name where false; -> Will return the entire table

# DCL and TCL queries

GRANT
GRANT gives a particular user access to database objects such as tables, views or the database itself. The below example would give SELECT and UPDATE access on the customers table to a user named “usr_bob”.

GRANT SELECT, UPDATE ON customers TO usr_bob;

REVOKE
REVOKE removes a user’s permissions for a particular database object.

REVOKE SELECT, UPDATE ON customers FROM usr_bob;

SAVEPOINT
SAVEPOINT allows you to identify a point in a transaction to which you can later roll back. Similar to creating a backup.

SAVEPOINT SAVEPOINT_NAME;

COMMIT
COMMIT is for saving every transaction to the database. A COMMIT statement will release any existing savepoints that may be in use and once the statement is issued, you cannot roll back the transaction.

DELETE FROM customers
WHERE name = ‘Bob’;
COMMIT

ROLLBACK
ROLLBACK is used to undo transactions which are not saved to the database. This can only be used to undo transactions since the last COMMIT or ROLLBACK command was issued. You can also rollback to a SAVEPOINT that has been created before.

ROLLBACK TO SAVEPOINT_NAME;

TRUNCATE
TRUNCATE TABLE removes all data entries from a table in a database, but keeps the table and structure in place. Similar to DELETE.

TRUNCATE TABLE customers;

# The Union statement

SELECT name, salary
FROM employees
UNION
SELECT name, salary
FROM departments;

Combine two tables and eliminate duplicate rows

Use the UNION ALL operator to include duplicate rows in the result set

SELECT name, salary
FROM employees
UNION ALL
SELECT name, salary
FROM departments;

The UNION operator in SQL combines the result sets of two or more SELECT statements into a single result set.

Conditions:
1) Every SELECT statement within UNION must have the same number of columns
2) The columns must also have similar data types
3) The columns in every SELECT statement must also be in the same order