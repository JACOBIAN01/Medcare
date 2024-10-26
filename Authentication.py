from tkinter import *

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

        self.welcome  = Label(self.window, text=f"Welcome Patient",bg="lightblue")
        self.welcome.pack()

        


        self.window.mainloop()
        


        
        
    def Valid(self,userid,password):
        for record in PatientDatabase:
            if userid in record and record[userid]==password:
                return True
        
        return False


class Doctor:
    def __init__(self):
        pass

    
    def DoctorDashboard(self):
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="lightblue")

        self.welcome  = Label(self.window, text=f"Welcome Doctor ! ",bg="lightblue")
        self.welcome.pack()

        


        self.window.mainloop()
        

    
class Admin:
    def __init__(self):
            
        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="lightblue")

        
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








