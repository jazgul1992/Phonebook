import sqlite3
# Подключение к базе данных
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY,name TEXT,surname TEXT);""")

phonebook = {
"Мирбек" : {'phones': [703509876,503509876],
'birthday': '10.08.1989',
'email': 'mirbek@mail.ru'
},
"Кундуз": {'phones' : [703566470]}
}

print(phonebook['Мирбек'])
print(phonebook['Мирбек'] ['phones'])
print(phonebook['Мирбек'] ['phones'] [-1])
