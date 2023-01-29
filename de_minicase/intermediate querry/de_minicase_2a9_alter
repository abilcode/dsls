SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER PROCEDURE [dbo].[Invoice]
@CustomerID nvarchar(50)
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
WHERE Customers.CustomerID = @CustomerID

SELECT *
FROM #invoice
GO
