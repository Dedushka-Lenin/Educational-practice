class comments_query:
    create = 'INSERT INTO Comments (message, masterID, requestID) VALUES (?, ?, ?)'
    delete = 'DELETE FROM Comments WHERE id = ?'
    check = 'SELECT 1 FROM Comments WHERE id = ?'
    get = 'SELECT * FROM Comments WHERE id = ?'
    get_list =  'SELECT * FROM Comments'

class requests_query:
    create = 'INSERT INTO Requests (startDate, climateTechType, climateTechModel, problemDescryption, requestStatus, completionDate, repairParts, masterID, clientID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    delete = 'DELETE FROM Requests WHERE id = ?'
    check = 'SELECT 1 FROM Requests WHERE id = ?'
    get = 'SELECT * FROM Requests WHERE id = ?'
    get_list =  'SELECT * FROM Requests'

class users_query:
    create = 'INSERT INTO Users (fio, phone, login, password, type) VALUES (?, ?, ?, ?, ?)'
    delete = 'DELETE FROM Users WHERE id = ?'
    check = 'SELECT 1 FROM Users WHERE id = ?'
    get = 'SELECT * FROM Users WHERE id = ?'
    get_list =  'SELECT * FROM Users'

class token_query:
    create = 'INSERT INTO token (user_id, token) VALUES (?, ?)'
    delete = 'DELETE FROM token WHERE id = ?'
    check = 'SELECT 1 FROM token WHERE token = ?'
    get = 'SELECT * FROM token WHERE id = ?'
    get_list =  'SELECT * FROM token'
