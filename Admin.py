from tkinter import *
import datetime
from tkinter import messagebox


class Admin:
    def AdminDashboard(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")
        self.window.iconbitmap("./Static/MedCareLogo.ico")

        Navbar = Frame(self.window,bg="cyan",height=55).pack(fill="x",side="top")
        Footer = Frame(self.window,height=20,bg="cyan").pack(fill="x",side="bottom")
   
        Label(self.window, text="Welcome to MedCare", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        roles = ["Doctor", "Patient"]
        selected_role = StringVar(value=roles[0])
        role_menu = OptionMenu(self.window, selected_role, *roles)
        role_menu.config(width=15, font=("Helvetica", 12))
        role_menu.pack(pady=10)

        Label(self.window, text="Enter User ID", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        UserID = Entry(self.window, font=("Helvetica", 10))
        UserID.pack()

        Label(self.window, text="Enter Password", bg="#2F4F4F", fg="white", font=("Helvetica", 10)).pack(pady=5)
        PassWord = Entry(self.window, show="*", font=("Helvetica", 10))
        PassWord.pack()

        def auth():
            import Database
            password = int(PassWord.get())
            user_id = UserID.get()
            try:
                if Database.ValidDoctor(user_id, password) and selected_role.get().lower() == "doctor":
                    import DoctorDashboard
                    self.window.destroy()
                    DoctorDashboard.Doctor.DoctorDashboard(self,user_id)
                elif Database.ValidPatient(user_id, password) and selected_role.get().lower() == "patient":
                    self.window.destroy()
                    import PatientDashboard
                    PatientDashboard.Patient.PatientDashboard(self,user_id)
                else:
                    messagebox.showerror("Error", "Authentication Failed")
            except ValueError:
                messagebox.showerror("Error", "Invalid Password Format")
        
        def CreateAccount():
            import NewAccount
            self.window.destroy()
            NewAccount.NewUser.Account(self)


        Button(self.window, text="Login", command=auth, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        Label(self.window, text="Don't Have any Account ? Create One", bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        Button(self.window, text="Sign Up", command=CreateAccount, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        
        
        self.window.mainloop()

