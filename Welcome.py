
from tkinter import *

class Welcome:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")
        self.window.iconbitmap("./Static/MedCareLogo.ico")
   
        Label(self.window, text="Welcome to MedCare", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)
        def welcome():
            self.window.destroy()
            import Admin
            Admin.Admin.AdminDashboard(self)
        Button(self.window, text="Continue", command=welcome, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)

        self.window.mainloop()



wel = Welcome()
