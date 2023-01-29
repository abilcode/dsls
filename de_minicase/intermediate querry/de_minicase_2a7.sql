WITH cte AS (
    SELECT MONTH(Orders.OrderDate) AS Month,SUM([Order Details].UnitPrice * [Order Details].Quantity ) AS TotalPrice, Products.ProductName,
    ROW_NUMBER() OVER(PARTITION BY MONTH(Orders.OrderDate) ORDER BY SUM([Order Details].UnitPrice * [Order Details].Quantity )DESC) AS Rank
    FROM [Order Details]
    JOIN Orders
        ON [Order Details].OrderID = Orders.OrderID
    JOIN Products
        ON [Order Details].ProductID = Products.ProductID
    WHERE YEAR(Orders.OrderDate) = 1997 
    GROUP BY Products.ProductName, MONTH(Orders.OrderDate)
    
) 
SELECT * 
FROM cte
WHERE Rank <= 5
