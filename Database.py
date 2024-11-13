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

def GetAllDoctors():
     doctor_cursor.execute("SELECT name FROM doctors")
     Doctors = doctor_cursor.fetchall()
     Doctor_Name_list = []
     for doctor in Doctors:
          Doctor_Name_list.append(doctor[0])
     return Doctor_Name_list

def GetAllPatients():
     patient_cursor.execute("SELECT name FROM patients")
     Patient = patient_cursor.fetchall()
     Patient_Name_list =[]
     for patient in Patient:
          Patient_Name_list.append(patient[0])

     return Patient_Name_list

def ClearDatabase():
     patient_cursor.execute("DELETE FROM patients")
     doctor_cursor.execute("DELETE FROM doctors")

     patient_database.commit()
     doctor_database.commit()

     patient_database.close()
     doctor_database.close()


def AddDoctor(name,age,id,password,field):
     doctor_cursor.execute(insert_doctor,(name,age,id,password,field))
     doctor_database.commit()
     doctor_database.close()

def AddPatient(name,age,gender,id,password):
     patient_cursor.execute(insert_patient,(name,age,gender,id,password))
     patient_database.commit()
     patient_database.close()




