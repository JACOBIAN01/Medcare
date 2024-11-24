from tkinter import *
import Database


class Doctor:
    def DoctorDashboard(self, id):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Doctor Dashboard")
        self.window.iconbitmap("./Static/MedCareLogo.ico")
        Name = Database.GetDoctorName(id)

        Navbar = Frame(self.window,bg="cyan",height=55).pack(fill="x",side="top")
        Footer = Frame(self.window,height=20,bg="cyan").pack(fill="x",side="bottom")

        Label(self.window, text=f"Welcome {Name}", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack(pady=20)

        def LogOut():
            self.window.destroy()
            import Welcome
            Welcome.welcomeuser

        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()

