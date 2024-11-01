
PatientDatabase = [
    {"Name": "Subhadeep Ghorai", "patient_id": "admin", "password": 1234, "age": 21, "gender": "Male"},
    {"Name": "Ravi Kumar", "patient_id": "pat001", "password": 1294, "age": 45, "gender": "Male"},
    {"Name": "Anjali Desai", "patient_id": "pat002", "password": 1134, "age": 30, "gender": "Female"},
    {"Name": "Manoj Choudhary", "patient_id": "pat003", "password": 1254, "age": 55, "gender": "Male"},
    {"Name": "Sita Reddy", "patient_id": "pat004", "password": 1294, "age": 60, "gender": "Female"},
    {"Name": "Rajesh Kapoor", "patient_id": "pat005", "password": 1034, "age": 50, "gender": "Male"}
]


id = input()
for i in range(len(PatientDatabase)):
    if(PatientDatabase[i]["patient_id"]==id):
        print(PatientDatabase[i]["Name"])
        break

                    
