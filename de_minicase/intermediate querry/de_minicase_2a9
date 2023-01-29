CREATE PROCEDURE Invoice
AS
Create table #invoice (
    CustomerID varchar(50), 
    CompanyName varchar(50), 
    OrderID varchar(50), 
    OrderDate varchar(50), 
    RequiredDate varchar(50), 
    ShippedDate varchar(50)
)

Insert into #invoice
SELECT Customers.CustomerID , CompanyName, OrderID, OrderDate, RequiredDate, ShippedDate
FROM Customers
JOIN Orders
ON Customers.CustomerID = Orders.CustomerID

SELECT *
FROM #invoice 

EXEC Invoice @CustomerID = 'VINET'

