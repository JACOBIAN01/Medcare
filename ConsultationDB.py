import sqlite3
import random

conn = sqlite3.connect('consultDB.db')
cursor = conn.cursor()

consultation_history = """
CREATE TABLE IF NOT EXISTS history(
    consult_id TEXT PRIMARY KEY,
    doctor TEXT NOT NULL,
    patient TEXT NOT NULL,
    time TEXT NOT NULL,
    booking_date TEXT NOT NULL
)
"""


cursor.execute(consultation_history)
insert_history = "INSERT INTO history (consult_id, doctor, patient, time, booking_date) VALUES (?,?,?,?,?)"

def GenerateConsulId(DocName, PatName):
    DocShort = ''.join(text[0] for text in DocName.split())
    PatShort = ''.join(text[0] for text in PatName.split())
    id = DocShort + PatShort + str(random.randint(1, 99999))
    return str(id)

def AddHistory(doctor, patient, time, booking_date):
    consult_id = GenerateConsulId(doctor, patient)
    doctor = str(doctor)
    patient = str(patient)
    time = str(time)
    booking_date = str(booking_date)
    cursor.execute(insert_history,(consult_id, doctor, patient, time, booking_date))
    conn.commit()

def GetAllHistory():
    cursor.execute("SELECT * FROM history")
    history = cursor.fetchall()
    for item in history:
        id = item[0]
        doctor = item[1]
        patient = item[2]
        time = item[3]
        date = item[4]
        print(f"ID: {id}, Doctor: Dr.{doctor}, Patient: {patient}, Time: {time}, Date: {date}\n")

def ClearHistory():
    cursor.execute("DELETE FROM history")
    conn.commit()

def DocHistory(name):
    cursor.execute("SELECT * FROM history WHERE doctor = ?", (name,))
    history = cursor.fetchall()
    if history:
        result = []
        for item in history:
            id = item[0]
            doctor = item[1]
            patient = item[2]
            time = item[3]
            date = item[4]
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
            id = item[0]
            doctor = item[1]
            patient = item[2]
            time = item[3]
            date = item[4]
            results.append(f"Doctor: Dr.{doctor}, Patient: {patient}, Time: {time}, Date: {date}")
        return "\n".join(results)
    else:
        return f"No consultation history found for Patient {name}"

def ClearPatHistory(name):
    cursor.execute("DELETE FROM history WHERE patient = ?", (name,))
    conn.commit()

AddHistory("Subhadeep Ghorai", "Subhadeep Ghorai", "7 PM", "2024")
GetAllHistory()
