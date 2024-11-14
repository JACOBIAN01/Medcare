from tkinter import *
from tkinter import messagebox
import datetime
import Database
class Patient:
    def PatientDashboard(self, id):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F") 
        self.window.title("MedCare - Patient Dashboard")
        self.window.iconbitmap("./Static/MedCareLogo.ico")
        Name = Database.GetPatientName(id)

        Footer = Frame(self.window,height=20,bg="cyan").pack(fill="x",side="bottom")
        Navbar = Frame(self.window,bg="cyan",height=55)
        Navbar.pack(fill="x",side="top")

        Header = Label(Navbar,text=f"Welcome {Name}",bg="cyan", fg="black", font=("Alice", 15,"bold"))
        Header.pack(pady=5,side="right")


        def LogOutFunc():
            self.window.destroy()
            import Welcome
            welcome = Welcome()
            

        def ConsultBooking():

            
            Doctors = Database.GetAllDoctors()
            Times = [f"{time} PM" for time in range(1, 13)]

            selected_doctor = StringVar(value=Doctors[0])
            selected_time = StringVar(value=Times[0])

            Label(self.window, text="Select Doctor:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).grid(column=1,row=0, pady=5)
            ChooseDoctor = OptionMenu(self.window, selected_doctor, *Doctors)
            ChooseDoctor.config(width=30, font=("Helvetica", 12))
            ChooseDoctor.grid(column=2,row=0, pady=5)

            Label(self.window, text="Select Time:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).grid(column=1,row=1, pady=5)
            SelectTime = OptionMenu(self.window, selected_time, *Times)
            SelectTime.config(width=30, font=("Helvetica", 12))
            SelectTime.grid(row=1,column=2,pady=5)


            def Report():
                with open("History.txt", "a") as file:
                    file.write(f"Consultation Booked. Doctor: Dr. {selected_doctor.get()} | Patient Name: {Name} | Time: {selected_time.get()} | Booking Date: {datetime.datetime.now().date()}\n")
                messagebox.showinfo("Confirmation", "Consultation Booked Successfully!")

            Button(self.window, text="Confirm", command=Report, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold")).pack(pady=15)

        ConsultBook = Button(Navbar, text="Book Consultation", command=ConsultBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        ConsultBook.pack(pady=10,side="left")
        LogOut = Button(Navbar, text="LogOut", command=LogOutFunc, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        LogOut.pack(pady=10,side="left")

        self.window.mainloop()
