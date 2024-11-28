from tkinter import *
import Database
import ConsultationDB


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
        Footer_Text = Label(Footer, text="© 2024 MedCare. All Rights Reserved", fg="#EEEEEE", bg="#00ADB5",font=("Helvetica", 10, "italic"))
        Footer_Text.pack(pady=5)

        
        Label(self.window, text=f"Welcome {Name}", bg="cyan", fg="black", font=("Helvetica", 16, "bold")).place(x=900,y=10)
        def ShowBookings():
            self.my_frame = Frame(self.window,bg='green',height=50)
            self.my_frame.pack(fill="both")
            self.newbook = Label(self.my_frame,font=("Helvetica", 14, "bold"),bg='green')
            self.newbook.pack()
            self.patients = ConsultationDB.DocHistory(Name)
            self.newbook.config(text=self.patients)
            def Cancel():
                self.my_frame.destroy()

            self.cancel = Button(self.my_frame,text="Cancel",font=("Helvetica", 8, "bold"),padx=8,pady=3,command=Cancel)
            self.cancel.pack()



        View_Bookings = Button(Navbar,text="View Bookings",font=("Helvetica", 11, "bold"),padx=20,pady=5,command=ShowBookings)
        View_Bookings.place(x=5,y=2)

        def LogOut():
            self.window.destroy()
            import Welcome
            Welcome.Welcome.WelcomeDashboard()

        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 11, "bold"),padx=20,pady=5).place(x=165,y=2)
        self.window.mainloop()

