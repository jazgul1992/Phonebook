import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users ( 
    login TEXT,
    password TEXT,
    cash BIGINT
)""")

db.commit()

user_login = input('Login:')
user_password = input('Password:')

if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?, ?, ?)" , (user_login, user_password, 0))
    db.commit()

    print('Зарегистрировано')
else:
    print('Такая запись уже есть')