SELECT    COUNT(*) 
FROM      Orders 
WHERE     YEAR(OrderDate) = '1997' 
GROUP BY  MONTH(OrderDate)