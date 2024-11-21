import sqlite3
import random

ntdb = sqlite3.connect('not_telegram.db')
cursor = ntdb.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#for i in range(1, 11):
#    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{random.randint(18, 100)}', f'{random.randint(0, 1000)}'))

#for i in range(1, 11, 2):
#    cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, i))

#for i in range(1, 11, 3):
#    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

#cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

cursor.execute('SELECT COUNT(*) FROM Users')
count = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
summa = cursor.fetchone()[0]
print(summa/count)

cursor.execute('SELECT AVG(balance) FROM Users')
avg = cursor.fetchone()[0]
print(avg)

# Решила посчитать обоими способами


ntdb.commit()
ntdb.close()