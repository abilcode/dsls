SELECT DISTINCT(Orders.ShipName)
FROM [Order Details]
JOIN Orders
ON [Order Details].OrderID = Orders.OrderID
JOIN Products
on [Order Details].ProductID = Products.ProductID
WHERE year(Orders.OrderDate) = 1997 AND
MONTH(Orders.OrderDate) = 6 AND
Products.ProductName = 'Chai'