from tkinter import *
import datetime

PatientDatabase = [
    {"admin":1234},
    {"user1":2345},
    {"user2":4567}
]


DoctorDatabase = [
    {"admin":1234},
    {"doc1":2345},
    {"doc2":4567}
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
                for doctor in doctors:
                    Doctors.append(doctor)
                    
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
                consult_report = f"Consultation Booked with Doctor {Current_Doctor} at {Current_time}"
                report = Label(self.window, text=consult_report)
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
                welcome.config(text="Welcome to MedCare !")
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
        for record in DoctorDatabase:
            if userid in record and record[userid]==password:
                return True
        
        return False
    
    def ValidPatient(self,userid,password):
        for record in PatientDatabase:
            if userid in record and record[userid]==password:
                return True
        
        return False
    




admin = Admin()










