from tkinter import *
from tkinter import messagebox
import datetime

class Patient:
    def __init__(self, id):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F") 
        self.window.title("MedCare - Patient Dashboard")
        Name = Admin.GetPatientName(id)

        self.welcome = Label(self.window, text=f"Welcome {Name}", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold"))
        self.welcome.pack(pady=20)

        def LogOut():
            self.window.destroy()
            new_admin = Admin()
            new_admin.AdminDashboard()

        def ConsultBooking():
            Doctors = [doc["Name"] for doc in DoctorDatabase]
            Times = [f"{time} PM" for time in range(1, 13)]

            selected_doctor = StringVar(value=Doctors[0])
            selected_time = StringVar(value=Times[0])

            Label(self.window, text="Select Doctor:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).pack(pady=5)
            ChooseDoctor = OptionMenu(self.window, selected_doctor, *Doctors)
            ChooseDoctor.config(width=30, font=("Helvetica", 12))
            ChooseDoctor.pack(pady=5)

            Label(self.window, text="Select Time:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).pack(pady=5)
            SelectTime = OptionMenu(self.window, selected_time, *Times)
            SelectTime.config(width=30, font=("Helvetica", 12))
            SelectTime.pack(pady=5)

            def Report():
                with open("History.txt", "a") as file:
                    file.write(f"Consultation Booked. Doctor: {selected_doctor.get()} | Patient Name: {Name} | Time: {selected_time.get()} | Booking Date: {datetime.datetime.now().date()}\n")
                messagebox.showinfo("Confirmation", "Consultation Booked Successfully!")

            Button(self.window, text="Confirm", command=Report, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold")).pack(pady=15)

        Button(self.window, text="Book Consultation", command=ConsultBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold")).pack(pady=10)
        Button(self.window, text="LogOut", command=LogOut, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)

        self.window.mainloop()


