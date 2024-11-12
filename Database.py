import sqlite3


patient_database = sqlite3.connect("patient_database.db")
patient_cursor = patient_database.cursor()

doctor_database = sqlite3.connect("doctor_database.db")
doctor_cursor = doctor_database.cursor()

patient_record = """
CREATE TABLE IF NOT EXISTS patients(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    pat_id TEXT,
    password INTEGER NOT NULL
);
"""

doctor_record = """
CREATE TABLE IF NOT EXISTS doctors(
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    doc_id TEXT ,
    password INTEGER NOT NULL,
    specialization TEXT NOT NULL
);
"""

patient_cursor.execute(patient_record)
doctor_cursor.execute(doctor_record)


insert_patient = "INSERT INTO patients (name,age,gender,pat_id,password) VALUES (?,?,?,?,?)"

insert_doctor = "INSERT INTO doctors (name,age,doc_id,password,specialization) VALUES (?,?,?,?,?)"


# patient_cursor.execute(insert_patient,("Subhadeep Ghorai", 21, "Male", "patadmin", 1234))
# patient_cursor.execute(insert_patient,("Laiba Razi", 21, "Female", "pat_01",2345))
# patient_cursor.execute(insert_patient,("Avi", 21, "Male", "pat_02", 5764))


# doctor_cursor.execute(insert_doctor,("Subhadeep Ghorai", 45, "docadmin", 1234, "Cardiology"))
# doctor_cursor.execute(insert_doctor,("Supriti Nayek", 45, "doc_01", 9800, "Cardiology"))
# doctor_cursor.execute(insert_doctor,("Rahul Dutta", 45, "doc_02", 3654, "Cardiology"))


# patient_database.commit()
# doctor_database.commit()

# patient_database.close()
# doctor_database.close()


def GetDoctorName(id):
   doctor_cursor.execute("SELECT name FROM doctors WHERE doc_id = ?",(id,))
   Name = doctor_cursor.fetchone()
   return Name[0] if Name else "Unknown"
   
def GetPatientName(id):
     patient_cursor.execute("SELECT name FROM patients WHERE pat_id = ?",(id,))
     Name = patient_cursor.fetchone()
     return Name[0] if Name else "Unknown"


def ValidDoctor(userid, password):
        doctor_cursor.execute("SELECT * FROM doctors WHERE doc_id =? AND password = ?",(userid,password))
        return bool(doctor_cursor.fetchone())


def ValidPatient(userid, password):
     patient_cursor.execute("SELECT * FROM patients WHERE pat_id = ? AND password = ?",(userid,password))
     return bool(patient_cursor.fetchone())




