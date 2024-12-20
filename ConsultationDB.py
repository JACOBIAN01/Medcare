import sqlite3

conn = sqlite3.connect('consultDB.db')
cursor = conn.cursor()


consultation_history ="""
CREATE TABLE IF NOT EXISTS history(
bookid INTEGER ,
doctor TEXT NOT NULL,
patient TEXT NOT NULL,
time TEXT NOT NULL,
booking_date TEXT NOT NULL
)
"""


cursor.execute(consultation_history)
insert_history = "INSERT INTO history (doctor,patient,time,booking_date) VALUES (?,?,?,?)"


def AddHistory(doctor,patient,time,booking_date):
    doctor = str(doctor)
    patient = str(patient)
    time = str(time)
    booking_date = str(booking_date)
    cursor.execute(insert_history,(doctor,patient,time,booking_date))
    conn.commit()


def GetAllHistory():
    cursor.execute("SELECT *  FROM history")
    history = cursor.fetchall()
    for item in history:
        doctor = item[0]
        patient = item[1]
        time = item[2]
        date = item[3]
        print(f"Doctor: Dr.{doctor}, Patient:{patient},Time:{time},Date:{date}\n")
        


def ClearHistory():
    cursor.execute("DELETE FROM history")
    conn.commit()


def DocHistory(name):
    cursor.execute("SELECT * FROM history WHERE doctor = ?", (name,))
    history = cursor.fetchall()
    if history:
        result = []
        for item in history:
            doctor = item[0]
            patient = item[1]
            time = item[2]
            date = item[3]
            result.append(f"Doctor: Dr.{doctor}, Patient: {patient}, Time: {time}, Date: {date}")
        return "\n".join(result) 
    else:
        return f"No consultation history found for Dr. {name}"
    

   
def PatHistory(name):
    cursor.execute("SELECT * FROM history WHERE patient = ?", (name,))
    history = cursor.fetchall()
    if history:
        results = []
        
        for item in history:
            doctor = item[0]
            patient = item[1]
            time = item[2]
            date = item[3]
            results.append(f"Doctor: Dr.{doctor}, Patient: {patient}, Time: {time}, Date: {date}")
        return "\n".join(results)
    else:
        return f"No consultation history found for Patient {name}"



def ClearPatHistory(name):
    cursor.execute("DELETE FROM history WHERE patient =?",(name,))
    conn.commit()


