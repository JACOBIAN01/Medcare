import sqlite3


patient_database = sqlite3.connect("patient_database.db")
patient_cursor = patient_database.cursor()

doctor_database = sqlite3.connect("doctor_database.db")
doctor_cursor = doctor_database.cursor()


patient_record = """

CREATE TABLE IF NOT EXISTS patients(

name TEXT NOT NULL,
age INTEGER NOT NULL,
gender TEXT NOT NULL ,
pat_id INTEGER PRIMARY KEY ,
password INTEGER NOT NULL ,
);
"""



doctor_record = """

CREATE TABLE IF NOT EXISTS doctors(

name TEXT NOT NULL,
age INTEGER NOT NULL,
doc_id INTEGER PRIMARY KEY ,
password INTEGER NOT NULL ,
specialization TEXT NOT NULL
);
"""


insert_patient = "INSERT INTO patients (name,age,gender,pat_id,password) VALUES (?,?,?,?)"

insert_doctor = "INSERT INTO doctors (name,age,doc_id,password,specialization) VALUES (?,?,?,?)"


