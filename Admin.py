from tkinter import *
import datetime
from tkinter import messagebox
import NewAccount
import DoctorDashboard
import PatientDashboard
import TestDataBase




class Admin:
    def AdminDashboard(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")
   
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
            user_id = UserID.get()
            try:
                password = int(PassWord.get())
                if self.ValidDoctor(user_id, password) and selected_role.get().lower() == "doctor":
                    self.window.destroy()
                    DoctorDashboard.doctor(self,user_id)
                elif self.ValidPatient(user_id, password) and selected_role.get().lower() == "patient":
                    self.window.destroy()
                    PatientDashboard.Patient(self,user_id)
                else:
                    messagebox.showerror("Error", "Authentication Failed")
            except ValueError:
                messagebox.showerror("Error", "Invalid Password Format")
        
        def CreateAccount():
            self.window.destroy()
            NewAccount.NewUser.Account(self)

        Button(self.window, text="Login", command=auth, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        Label(self.window, text="Don't Have any Account ? Create One", bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        Button(self.window, text="Sign Up", command=CreateAccount, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()




admin = Admin()
admin.AdminDashboard()
