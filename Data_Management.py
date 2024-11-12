import Database

Database.doctor_cursor.execute("SELECT * FROM doctors")
rows = Database.doctor_cursor.fetchall()


for row in rows:
    print(row)