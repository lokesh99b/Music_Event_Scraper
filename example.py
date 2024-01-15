import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# try:
#     # Begin a transaction
#     connection.execute('BEGIN')
#
#     # Insert data into the database
#     new_rows = [('Cats', 'Cat city', '2023.5.12'), ('Mouse', 'Mumbai city', '2023.5.13')]
#     cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
#
#     # Commit the transaction
#     connection.commit()
# except sqlite3.Error as e:
#     # Rollback the transaction if an error occurs
#     connection.rollback()
#     print("Transaction rolled back:", e)
# finally:
#     # Close the database connection
#     connection.close()


#cursor.execute("SELECT * FROM events WHERE Date='2023.5.12'")
#rows = cursor.fetchall()
#print(rows)

#cursor.execute("SELECT Band, Date FROM events WHERE Date='2023.5.12'")
#rows = cursor.fetchall()
#print(rows)

#insert new rows
# new_rows = [('Cats', 'Cat city', '2023.5.12'), ('Mouse', 'Mumbai city', '2023.5.13')]
#
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)