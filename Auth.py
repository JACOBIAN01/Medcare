from tkinter import *
import datetime
from tkinter import messagebox


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


class Patient:
    def PatientDashboard(self,id):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F") 
        self.window.title("MedCare - Patient Dashboard")
        Name = Admin.GetPatientName(id)
        Patient_ID = id

        
        self.welcome = Label(self.window, text=f"Welcome {Name} ", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold"))
        self.welcome.pack(pady=20)

        def ConsultBooking():
            Doctors = [doc["Name"] for doc in DoctorDatabase]
            Times = [f"{time} PM" for time in range(1, 13)]

            selected_doctor = StringVar(value=Doctors[0])
            selected_time = StringVar(value=Times[0])

            ChooseDoctor = OptionMenu(self.window, selected_doctor, *Doctors)
            ChooseDoctor.config(width=20, font=("Helvetica", 12))
            ChooseDoctor.pack(pady=5)

            SelectTime = OptionMenu(self.window, selected_time, *Times)
            SelectTime.config(width=20, font=("Helvetica", 12))
            SelectTime.pack(pady=5)

            def Report():
                with open("History.txt", "a") as file:
                    file.write(f"Consultation Booked. Doctor: {selected_doctor.get()}, Time: {selected_time.get()}\n")
                messagebox.showinfo("Confirmation","Consultation Booked Successfully!")

            Button(self.window, text="Confirm", command=Report, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=15)

        Button(self.window, text="Book Consultation", command=ConsultBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)
        self.window.mainloop()

class Doctor:
    def DoctorDashboard(self,id):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F")  
        self.window.title("MedCare - Doctor Dashboard")
        Name = Admin.GetDoctorName(id)
        Doctor_id = id

        
        Label(self.window, text=f"Welcome {Name}", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)
        self.window.mainloop()

class Admin:
    
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x400")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")

    
        with open("History.txt", "w") as file:
            pass
   
        Label(self.window, text="Welcome to MedCare", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        roles = ["Doctor", "Patient"]
        selected_role = StringVar(value=roles[0])
        OptionMenu(self.window, selected_role, *roles).config(width=15, font=("Helvetica", 12))
        OptionMenu(self.window, selected_role, *roles).pack(pady=10)

        
        Label(self.window, text="Enter User ID", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        UserID = Entry(self.window, font=("Helvetica", 10))
        UserID.pack()



        Label(self.window, text="Enter Password", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        PassWord = Entry(self.window, show="*", font=("Helvetica", 10))
        PassWord.pack()

        def auth():
            user_id = UserID.get()
            password = int(PassWord.get())
            if self.ValidDoctor(user_id, password) and selected_role.get().lower() == "doctor":
                self.window.destroy()
                Doctor().DoctorDashboard(user_id)
            elif self.ValidPatient(user_id, password) and selected_role.get().lower() == "patient":
                self.window.destroy()
                Patient().PatientDashboard(user_id)
            else:
                Label(self.window, text="Authentication Failed", fg="red", bg="#2F4F4F", font=("Helvetica", 10, "bold")).pack()
            

        Button(self.window, text="Login", command=auth, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)

        self.window.mainloop()

    
    def GetDoctorName(id):
                for doctor in DoctorDatabase:
                    if doctor["user_id"] == id:
                        return doctor["Name"]
                return "Unknown"
    def GetPatientName(id):
            for Patient in PatientDatabase:
                if Patient["patient_id"]==id:
                    return Patient["Name"]
            return "Unknown"
    

    def ValidDoctor(self,userid,password):
        for doctor in DoctorDatabase:
            if (userid in doctor["user_id"]  and doctor["password"]==password):
                return True
        return False

    
    def ValidPatient(self,userid,password):
        for patient in PatientDatabase:
            if (userid in patient["patient_id"]  and patient["password"]==password):
                return True
        return False



# Initialize Admin Panel
admin = Admin()
