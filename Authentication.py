from tkinter import *
import datetime

PatientDatabase = [
    {
        "Name": "Subhadeep Ghorai",
        "patient_id": "admin",
        "password":1234,
        "age": 21,
        "gender": "Male"
    },
    {
        "Name": "Ravi Kumar",
        "patient_id": "pat001",
        "password":1294,
        "age": 45,
        "gender": "Male"
    },
    {
        "Name": "Anjali Desai",
        "patient_id": "pat002",
        "password":1134,
        "age": 30,
        "gender": "Female"
    },
    {
        "Name": "Manoj Choudhary",
        "patient_id": "pat003",
        "password":1254,
        "age": 55,
        "gender": "Male"
    },
    {
        "Name": "Sita Reddy",
        "patient_id": "pat004",
        "password":1294,
        "age": 60,
        "gender": "Female"
    },
    {
        "Name": "Rajesh Kapoor",
        "patient_id": "pat005",
        "password":1034,
        "age": 50,
        "gender": "Male"
    }
]





DoctorDatabase = [
        {
        "Name": "Subhadeep Ghorai",
        "userid": "admin",
        "password": 1234,
        "specialization": "SDE"
    },
    {
        "Name": "Dr. Rohan Sharma",
        "userid": "rohan_sharma",
        "password": 1234,
        "specialization": "Cardiology"
    },
    {
        "Name": "Dr. Anjali Mehta",
        "userid": "anjali_mehta",
        "password": 5678,
        "specialization": "Dermatology"
    },
    {
        "Name": "Dr. Vikram Singh",
        "userid": "vikram_singh",
        "password": 9101,
        "specialization": "Pediatrics"
    },
    {
        "Name": "Dr. Priya Desai",
        "userid": "priya_desai",
        "password": 1121,
        "specialization": "Neurology"
    },
    {
        "Name": "Dr. Arjun Patel",
        "userid": "arjun_patel",
        "password": 3141,
        "specialization": "Orthopedics"
    }
]

class Patient:
    def __init__(self):
        pass

    
    def PatientDashboard(self):
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="lightblue")
        self.window.title("Medcare")

        self.welcome  = Label(self.window, text=f"Welcome Patient",bg="lightblue",font=("Times",12,"bold"))
        self.welcome.pack()

        def ConsultBooking():
            Doctors = []
            Time = []
            for time in range(1,13):
                Time.append(f"{time} PM")

            for doctors in DoctorDatabase:
                    Doctors.append(doctors["Name"])
                    
            selected_doctor = StringVar()
            selected_doctor.set(Doctors[0])
            selected_time = StringVar()
            selected_time.set(Time[0])

            ChooseDoctor = OptionMenu(self.window,selected_doctor,*Doctors)
            ChooseDoctor.pack()


            SelectTime = OptionMenu(self.window,selected_time,*Time)
            SelectTime.pack()
            
            def Report():
                Current_Doctor = selected_doctor.get()
                Current_time = selected_time.get()
                with open("History.txt","a") as file:
                    file.write(f"Consultation Booked. Doctor Name: {Current_Doctor} , Time: {Current_time}\n")
        
                report = Label(self.window, text="Consultation Confirmed!")
                report.pack()

            Book  = Button(self.window,text="Confirm",command= Report)
            Book.pack()


        Book_consult = Button(text="Book Consultation",bg="navyblue",fg="white",font=("Alice",9,"bold"),command=ConsultBooking)
        Book_consult.pack()

        self.window.mainloop()
         
        
    def Valid(self,userid,password):
        for record in PatientDatabase:
            if userid in record and record[userid]==password:
                return True
        
        return False


class Consultation:
    def __init__(self):
        pass


class Doctor:
    def __init__(self):
        pass

    def DoctorDashboard(self):
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="lightblue")
        self.window.title("Medcare")

        self.welcome  = Label(self.window, text=f"Welcome Doctor ! ",bg="lightblue")
        self.welcome.pack()

        

        self.window.mainloop()
        
    
class Admin:
    def __init__(self):
            
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="lightblue")
        self.window.title("Medcare")

        file = open("History.txt","w")
        

        Header = Label(text="Welcome to Medcare",bg="lightblue",font=("Times",12,"bold"))
        Header.pack()

        
        roles = ["doctor","patient"]
        selected_role = StringVar()
        selected_role.set(roles[0])

        ChooseRole = OptionMenu(self.window,selected_role,*roles)
        ChooseRole.pack()

        def auth():
            id = UserID.get()
            password = PassWord.get()
            if self.ValidDoctor(id,int(password)) and selected_role.get()=="doctor":
                welcome.config(text=f"Welcome to MedCare {id}")
                self.window.destroy()
                Doctor.DoctorDashboard(self)
            elif self.ValidPatient(id,int(password)) and selected_role.get()=="patient":
                welcome.config(text="Welcome to MedCare !")
                self.window.destroy()
                Patient.PatientDashboard(self)
            else:
                welcome.config(text="Authentication Failed")


        label1 = Label(self.window,text="Enter User ID",bg="lightblue")
        UserID = Entry(self.window)
        label2 = Label(self.window,text="Enter Password",bg="lightblue")
        PassWord = Entry(self.window,show="*")
        check  = Button(self.window,text="Login",command=auth)
        welcome = Label(self.window,bg="lightblue")
        label1.pack()
        UserID.pack()
        label2.pack()
        PassWord.pack()
        check.pack()
        welcome.pack()

        self.window.mainloop()


    def ValidDoctor(self,userid,password):
        for doctor in DoctorDatabase:
            if (userid in doctor["userid"]  and doctor["password"]==password):
                return True
            else:
                return False

    
    def ValidPatient(self,userid,password):
        for patient in PatientDatabase:
            if (userid in patient["patient_id"]  and patient["password"]==password):
                return True
            else:
                return False

    
    
        



admin = Admin()










