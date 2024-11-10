from tkinter import *
import TestDataBase


class Doctor:
    def DoctorDashboard(self, id):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Doctor Dashboard")
        Name = TestDataBase.GetDoctorName(id)

        Label(self.window, text=f"Welcome {Name}", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        def LogOut():
            self.window.destroy()
            import Welcome
            welcome = Welcome()
            
        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()

