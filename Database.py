import sqlite3


patient_record = sqlite3.connect("patient_records.db")
patient_cursor = patient_record.cursor()

doctor_record = sqlite3.connect("doctor_records.db")
doctor_cursor = doctor_record.cursor()
