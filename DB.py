import sqlite3

connection = sqlite3.connect("db.sl3", 5)
cur = connection.cursor()

# ====== CREATE ========
# cur.execute("CREATE TABLE users (login TEXT);")
# connection.commit()



# ====== INSERT ========
# name = input("Login : ")
# cur.execute(f"INSERT INTO users (login) VALUES ('{name}');")
# connection.commit()
# print("Login added!")


# ====== SELECT =======
# cur.execute(f"SELECT * FROM users;")
cur.execute(f"SELECT * FROM users WHERE login='admin234234';")
connection.commit()
res = cur.fetchall()
print(res)



connection.close()
