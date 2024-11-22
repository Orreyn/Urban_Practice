import sqlite3

db = sqlite3.connect('not_telegram.db')
cursor = db.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')


def get_all_products():
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    for product in products:
        return f'Название: {product[0]}, Описание: {product[1]}, Цена: {product[2]}'


def is_included(username):
    cursor.execute('SELECT username FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == username:
            return True
    return False


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?) ', (username, email, age, 1000))
    db.commit()


'''initiate_db()
for i in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
get_all_products()
db.commit()
db.close()'''

'''
add_user('Admin', 'admin@mail.ru', 23)
cursor.execute('DELETE FROM Users WHERE id = ?', (11,))
db.commit()
db.close()'''