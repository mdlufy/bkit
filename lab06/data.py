import sqlite3

conn = sqlite3.connect('orders.db')

cur = conn.cursor()


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  userName TEXT NOT NULL,
  userAge INTEGER
);
"""
cur.execute(create_users_table)

conn.commit()


# user = (3, 'German', 19)
# cur.execute("INSERT INTO users VALUES(?, ?, ?);", user)
# conn.commit()

cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(*all_results, sep = '\n')