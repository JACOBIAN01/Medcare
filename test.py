PatientDatabase = [
    {"Name": "Subhadeep Ghorai", "patient_id": "admin", "password": 1234, "age": 21, "gender": "Male"},
    {"Name": "Ravi Kumar", "patient_id": "pat001", "password": 1294, "age": 45, "gender": "Male"},
    {"Name": "Anjali Desai", "patient_id": "pat002", "password": 1134, "age": 30, "gender": "Female"},
    {"Name": "Manoj Choudhary", "patient_id": "pat003", "password": 1254, "age": 55, "gender": "Male"},
    {"Name": "Sita Reddy", "patient_id": "pat004", "password": 1294, "age": 60, "gender": "Female"},
    {"Name": "Rajesh Kapoor", "patient_id": "pat005", "password": 1034, "age": 50, "gender": "Male"}
]

DoctorDatabase = [
    {"Name": "Subhadeep Ghorai", "user_id": "admin", "password": 1234,"specialization": "Cardiology"},
    {"Name": "Laiba Razi Khan", "user_id": "laiba", "password": 9800,"specialization": "Cardiology"},
    {"Name": "Dr. Rohan Sharma", "userid": "rohan_sharma", "password": 1234, "specialization": "Cardiology"},
    {"Name": "Dr. Anjali Mehta", "userid": "anjali_mehta", "password": 5678, "specialization": "Dermatology"},
    {"Name": "Dr. Vikram Singh", "userid": "vikram_singh", "password": 9101, "specialization": "Pediatrics"},
    {"Name": "Dr. Priya Desai", "userid": "priya_desai", "password": 1121, "specialization": "Neurology"},
    {"Name": "Dr. Arjun Patel", "userid": "arjun_patel", "password": 3141, "specialization": "Orthopedics"}
]

id = input()
password = int(input())
def ValidDoctor(id,password):
        for doctor in DoctorDatabase:
            if (id in doctor["user_id"]  and doctor["password"]==password):
                print("Login")
                break
            else:
                print("Error")
                break

ValidDoctor(id,password)