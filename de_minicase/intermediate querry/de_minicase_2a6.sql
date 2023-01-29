SELECT Orders.ShipName, 
CASE
    WHEN SUM([Order Details].UnitPrice * [Order Details].Quantity ) <= 100 Then 'SMALL'
    WHEN SUM([Order Details].UnitPrice * [Order Details].Quantity ) BETWEEN 100 AND 500 Then 'MED'
    ELSE 'LARGE'
END AS StatusOfTotalPrice
FROM [Order Details]
JOIN Orders
ON [Order Details].OrderID = Orders.OrderID

WHERE YEAR(Orders.OrderDate) = 1997
GROUP BY Orders.ShipName
HAVING SUM([Order Details].UnitPrice * [Order Details].Quantity) > 500

