CREATE VIEW SOAL_8 AS
SELECT *, (1-Discount)*UnitPrice AS [PriceAfterDiscount] FROM [Order Details]
