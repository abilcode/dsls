SELECT TOP 5 Products.ProductName,COUNT(Products.ProductName) as OrdersValue
FROM [Order Details]
JOIN Orders
ON [Order Details].OrderID = Orders.OrderID
JOIN Products
on [Order Details].ProductID = Products.ProductID
WHERE year(Orders.OrderDate) = 1997 AND
MONTH(Orders.OrderDate) = 1
GROUP BY Products.ProductName
ORDER By COUNT(Products.ProductName) DESC
