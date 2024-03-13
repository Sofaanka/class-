import mysql.connector

# создаём подключение к БД
db = mysql.connector.connect(
    host="localhost",  # адрес сервера
    user="your_username",  # ваше имя пользователя
    password="your_password",  # ваш пароль
    database="история операций"  # имя базы данных
)

cursor = db.cursor()

# вводим данные
name = input("Введите имя: ")
email = input("Введите адрес электронной почты: ")

sql = "INSERT INTO your_table (name, email) VALUES (%s, %s)"
values = (name, email)

# выполняем SQL-запрос
cursor.execute(sql, values)

# подтверждаем изменения
db.commit()

print(cursor.rowcount, "запись добавлена.")

