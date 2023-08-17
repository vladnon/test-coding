import sqlite3 as sq
# sql - субд, тоесть отдельный язык для работы с базами данных
#типы данных в базах данных
# null, integer, text, real, blob

with sq.connect("saper.db") as con:
    cur = con.cursor()
    
    
# чтобы удалить таблицу нужна команда drop table
    # cur.execute("DROP TABLE IF EXISTS users")
# Обычно имена столбцов пищутся с маленькой буквы, а типы данных с большой, как и команда создать таблицу
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        OLD INTEGER,
        score INTEGER
    )
                """)
    
# insert - добавление данных в таблицу
# select - выборка данных из таблицы
# INSERT INTO users VALUES()
# SELECT <coloms> FROM users
# но обычно селект используют с where, что обозначает условие
# SELECT * FROM users WHERE SEX == 2
# кстати знаки сравнения и сахар такие же как и в питоне, ну тоесть == или or and not in, и тд
# также есть оператор order by, которые показывает таблицу в указаном порядке(DESC - обратная, ACS - обычная )
# еще есть limit 
# эти команды можно писать и непосретсвенно в питоне
    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 3")
    # result  = cur.fetchall()
    # выведет список, из кортежей уже с содержимым нашей таблице
    # ну либо же можно просто перебрать cur, и тогда это займет меньше памяти
    # for result in cur:
    #     print(result)
    # если еще методы fetchmany() и fetchone(), в скобках первого мы указывает сколько напечатать кортежей, а второй просто выводит первый кортеж
    result = cur.fetchmany(2)
    result2 = cur.fetchone()
    print(result)
    print(result2)    
