from tkinter import *
from tkinter import messagebox ,ttk
import datetime
import Database
import ConsultationDB
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

        def UpdateProfile():

            if hasattr(self,'profile_frame') and profile_frame.winfo_exists() :
                  profile_frame.destroy()

            profile_frame = Frame(self.window,bg="cyan",width=250)
            profile_frame.pack(side="right",fill="y")

            profile_des= Label(profile_frame,text="Your Profile",bg="#4682B4", fg="white", font=("Helvetica",8, "bold"),padx=10)
            profile_des.grid(row=0,column=1)

            NameText = Label(profile_frame,text="Update Name",bg="#4682B4", fg="white", font=("Helvetica", 8, "bold"))
            NameText.grid(row=1,column=0)

            Name_Entry = Entry(profile_frame)
            Name_Entry.grid(row=1,column=1)


            Update = Button(profile_frame, text="Update", command=UpdateProfile, bg="#4682B4", fg="white", font=("Helvetica",8, "bold"),relief="groove")
            Update.grid(row=3,column=1)

            def Close():
                profile_frame.destroy()
            
            Close = Button(profile_frame, text="Close", command=Close, bg="#4682B4", fg="white", font=("Helvetica",8, "bold"),relief="groove")
            Close.grid(row=3,column=0)



        Profile = Button(Navbar, text="Profile", command=UpdateProfile, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        Profile.pack(pady=5,side="right",padx=2)


        Header = Label(Navbar,text=f"Welcome, {Name}",bg="cyan", fg="black", font=("Alice", 15,"bold"))
        Header.pack(pady=5,side="right")


        def LogOutFunc():
            self.window.destroy()
            import Welcome
            Welcome.Welcome.WelcomeDashboard(self)

        def ViewHistory():
            if hasattr(self,'history_frame') and self.history_frame.winfo_exists() :
                  self.history_frame.destroy()
            
            
            import ConsultationDB
            self.my_history=ConsultationDB.PatHistory(Name)

            def Frame_Destroy():
                self.history_frame.destroy()

            def CancelBooking():
                History_Label.config(text=f"No consultation history found for Dr. {Name}")
                ConsultationDB.ClearPatHistory(Name)
            

            self.history_frame = Frame(self.window,height=50,bg="lightblue")
            self.history_frame.pack(fill="both")
            History_Label = Label(self.history_frame,bg="#2F4F4F", fg="white", font=("Helvetica", 12),text=self.my_history)
            History_Label.pack()
            Close_button = Button(self.history_frame, text="Close", command=Frame_Destroy, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
            Close_button.pack()
            Close_button = Button(self.history_frame, text="Cancel Booking", command=CancelBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
            Close_button.pack()
            
            

        def ConsultBooking():

            if hasattr(self,'consult_frame') and self.consult_frame.winfo_exists() :
                  self.consult_frame.destroy()

            self.consult_frame = Frame(self.window,height=30,bg="lightblue")
            self.consult_frame.pack(fill="both")

            Doctors = Database.GetAllDoctors()
            Times = [f"{time} PM" for time in range(1, 13)]

            selected_doctor = StringVar(value=Doctors[0])
            selected_time = StringVar(value=Times[0])

            Label(self.consult_frame, text="Select Doctor:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).grid(column=1,row=0, pady=5)
            ChooseDoctor = OptionMenu(self.consult_frame, selected_doctor, *Doctors)
            ChooseDoctor.config(width=30, font=("Helvetica", 12))
            ChooseDoctor.grid(column=2,row=0, pady=5)

            Label(self.consult_frame, text="Select Time:", bg="#2F4F4F", fg="white", font=("Helvetica", 12)).grid(column=1,row=1, pady=5)
            SelectTime = OptionMenu(self.consult_frame, selected_time, *Times)
            SelectTime.config(width=30, font=("Helvetica", 12))
            SelectTime.grid(row=1,column=2,pady=5)


            def Report():
                try:
                  ConsultationDB.AddHistory(selected_doctor.get(),Name,selected_time.get(),datetime.date.today())
                except E:
                    print(E)
                messagebox.showinfo("Confirmation", "Consultation Booked Successfully!")

            def Cancel():
                self.consult_frame.destroy()

            Confirm = Button(self.consult_frame, text="Confirm", command=Report, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"))
            Confirm.grid(pady=15,column=1,row=3)
            CancelButton = Button(self.consult_frame, text="Cancel", command=Cancel, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
            CancelButton.grid(pady=15,row=3,column=2)
            

        ConsultBook = Button(Navbar, text="Book Consultation", command=ConsultBooking, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        ConsultBook.pack(pady=10,side="left")
        History = Button(Navbar, text="View History", command=ViewHistory, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        History.pack(pady=10,side='left')
        LogOut = Button(Navbar, text="LogOut", command=LogOutFunc, bg="#4682B4", fg="white", font=("Helvetica", 12, "bold"),relief="groove")
        LogOut.pack(pady=10,side="left")

        def AI(msg):
            pass

        AIButton = ttk.Button(self.window,Text="Ask AI Doctor",command=AI,padding=5)
        AIButton.place(x=900,y=600)


        self.window.mainloop()

