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


def get_all_products():
    initiate_db()
    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()
    for product in products:
        return f'Название: {product[0]}, Описание: {product[1]}, Цена: {product[2]}'


'''initiate_db()
for i in range(1, 5):
    cursor.execute('INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)', (i, f'Продукт {i}', f'Описание {i}', f'{i * 100}'))
get_all_products()
db.commit()
db.close()'''