class material_type_query:
    create = 'INSERT INTO Material_type ("Тип материала", "Процент потерь сырья") VALUES (?, ?)'
    delete = 'DELETE FROM Material_type WHERE id = ?'
    check = 'SELECT 1 FROM Material_type WHERE id = ?'
    get = 'SELECT * FROM Material_type WHERE id = ?'
    get_list =  'SELECT * FROM Material_type'

class product_type_query:
    create = 'INSERT INTO Product_type ("Тип продукции", "Коэффициент типа продукции") VALUES (?, ?)'
    delete = 'DELETE FROM Product_type WHERE id = ?'
    check = 'SELECT 1 FROM Product_type WHERE id = ?'
    get = 'SELECT * FROM Product_type WHERE id = ?'
    get_list =  'SELECT * FROM Product_type'

class product_workshops_query:
    create = 'INSERT INTO Product_workshops ("Наименование продукции", "Название цеха", "Время изготовления, ч") VALUES (?, ?)'
    delete = 'DELETE FROM Product_workshops WHERE id = ?'
    check = 'SELECT 1 FROM Product_workshops WHERE id = ?'
    get = 'SELECT * FROM Product_workshops WHERE id = ?'
    get_list =  'SELECT * FROM Product_workshops'

class products_query:
    create = 'INSERT INTO Products ("Тип продукции", "Наименование продукции", "Артикул", "Минимальная стоимость для партнера", "Основной материал") VALUES (?, ?)'
    delete = 'DELETE FROM Products WHERE id = ?'
    check = 'SELECT 1 FROM Products WHERE id = ?'
    get = 'SELECT * FROM Products WHERE id = ?'
    get_list =  'SELECT * FROM Products'

class workshop_query:
    create = 'INSERT INTO Workshops ("Название цеха", "Тип цеха", "Количество человек для производства") VALUES (?, ?)'
    delete = 'DELETE FROM Workshops WHERE id = ?'
    check = 'SELECT 1 FROM Workshops WHERE id = ?'
    get = 'SELECT * FROM Workshops WHERE id = ?'
    get_list =  'SELECT * FROM Workshops'