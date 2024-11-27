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
        
        Label(self.window, text=f"Welcome {Name}", bg="cyan", fg="black", font=("Helvetica", 16, "bold")).place(x=900,y=10)
        def ShowBookings():
            self.my_frame = Frame(self.window,bg='green',height=50)
            self.my_frame.pack(fill="both")
            self.newbook = Label(self.my_frame,font=("Helvetica", 14, "bold"),bg='green')
            self.newbook.pack()
            self.patients = Database.GetPatientName(Name)
            self.newbook.config(text=self.patients)


        View_Bookings = Button(Navbar,text="View Bookings",font=("Helvetica", 11, "bold"),padx=20,pady=5,command=ShowBookings)
        View_Bookings.place(x=5,y=2)

        def LogOut():
            self.window.destroy()
            import Welcome
            Welcome.welcomeuser

        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 11, "bold"),padx=20,pady=5).place(x=165,y=2)
        self.window.mainloop()

doc = Doctor().DoctorDashboard("admin")