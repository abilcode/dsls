SELECT Orders.OrderID, SUM([Order Details].UnitPrice * [Order Details].Quantity ) AS TotalPrice, 
CASE
    WHEN SUM([Order Details].UnitPrice * [Order Details].Quantity ) <= 100 Then 'SMALL'
    WHEN SUM([Order Details].UnitPrice * [Order Details].Quantity ) BETWEEN 100 AND 500 Then 'MED'
    ELSE 'LARGE'
END AS StatusOfTotalPrice
FROM [Order Details]
JOIN Orders
ON [Order Details].OrderID = Orders.OrderID
JOIN Products
on [Order Details].ProductID = Products.ProductID
GROUP BY Orders.OrderID
