from tkinter import *
import Admin

class Doctor:
    def __init__(self, id):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Doctor Dashboard")
        Name = Admin.Admin.GetDoctorName(id)

        Label(self.window, text=f"Welcome {Name}", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        def LogOut():
            self.window.destroy()
            new_admin = Admin.Admin.AdminDashboard()
            new_admin.AdminDashboard()

        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()


