SELECT p.name AS Products, c.name AS Categories
FROM Products p
LEFT JOIN ProductsCategory pc ON p.id = pc.Products_id
LEFT JOIN Category c ON pc.Category_id = c.id