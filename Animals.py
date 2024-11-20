import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# cur.execute("DROP TABLE Animal;")
# connection.commit()

cur.execute("CREATE TABLE IF NOT EXISTS Animal (id INT, name TEXT, type TEXT);")
connection.commit()

# cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (1, 'Лев', 'Ссавець');")
# cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (2, 'Крокодил', 'Плазун');")
# cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (3, 'Орел', 'Птах');")
# cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (4, 'Морська черепаха', 'Плазун');")
# cur.execute(f"INSERT INTO Animal (id, name, type) VALUES (5, 'Мавпа', 'Ссавець');")
# connection.commit()

# cur.execute("SELECT * FROM Animal WHERE type='Ссавець';")
cur.execute("SELECT * FROM Animal;")
connection.commit()
res = cur.fetchall()
for row in res:
    print(f"{row[0]}. {row[1]} - {row[2]}")