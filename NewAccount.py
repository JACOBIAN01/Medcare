from tkinter import *
from tkinter import messagebox

class NewUser:
    def Account(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("New Account")

        Navbar = Frame(self.window,bg="cyan",height=55).pack(fill="x",side="top")
        Footer = Frame(self.window,height=20,bg="cyan").pack(fill="x",side="bottom")

        
        def clear_frame():
            for widget in self.window.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()



        def CreatePatientAccount(self):
            clear_frame()  

            def createNewPat():
                    import Database
                    name = Pat_Name.get()
                    age = Pat_age.get()
                    id = Pat_id.get()
                    password = Pat_pass.get()
                    gender = pat_gender.get()
                    Database.AddPatient(name,age,id,password,gender)
                    messagebox.showinfo('INFO',f"Account Successfully Created .\nName:{name}\nAge:{age}\nID:{id}\nPassword:{password}\nGender:{gender}")

            frame = Frame(self.window, padx=20, pady=20, bg="cyan")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            Label(frame, text="Create New Patient Account", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

            Label(frame, text="Enter Your Name", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Pat_Name=Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Pat_Name.pack()

            Label(frame, text="Enter Your Age", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Pat_age =Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Pat_age.pack()

            Label(frame, text="Enter Your User ID", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Pat_id = Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Pat_id.pack()

            Label(frame, text="Enter Your Password", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Pat_pass = Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1, show="*")
            Pat_pass.pack()

            Label(frame, text="Enter Your Gender", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            pat_gender = Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            pat_gender.pack()

            Button(frame, text="Create Account", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", activebackground="#5A9BD5", activeforeground="white", relief="flat", bd=3, padx=10, pady=5,command=createNewPat).pack(pady=20)

        def CreateDoctorAccount(self):
            clear_frame()  # Clear any existing frames

            def createNewDoc():
                    name = Doc_Name.get()
                    age = Doc_age.get()
                    id = Doc_id.get()
                    password = Doc_pass.get()
                    field = Doc_field.get()
                    import Database
                    Database.AddDoctor(name,age,id,password,field)
                    messagebox.showinfo('INFO',f"Account Successfully Created .\nName:{name}\nAge:{age}\nID:{id}\nPassword:{password}\nField:{field}")
            

            frame = Frame(self.window, padx=20, pady=20, bg="cyan")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            Label(frame, text="Create New Doctor Account", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

            Label(frame, text="Enter Your Name", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Doc_Name = Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Doc_Name.pack()

            Label(frame, text="Enter Your Age", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Doc_age=Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Doc_age.pack()

            Label(frame, text="Enter Your User ID", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Doc_id=Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Doc_id.pack()

            Label(frame, text="Enter Your Password", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Doc_pass = Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1, show="*")
            Doc_pass.pack()

            Label(frame, text="Enter Your Field", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Doc_field= Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1)
            Doc_field.pack()

            Button(frame, text="Create Account", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", activebackground="#5A9BD5", activeforeground="white", relief="flat", bd=3, padx=10, pady=5,command=createNewDoc).pack(pady=20)

        Label(self.window, text="Choose Your Role", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

        roles = ["Doctor", "Patient"]
        selected_role = StringVar()
        selected_role.set(roles[0])
        OptionMenu(self.window, selected_role, *roles).pack(padx=10)

        def Continue():
            if selected_role.get() == "Doctor":
                CreateDoctorAccount(self)
            elif selected_role.get() == "Patient":
                CreatePatientAccount(self)


        def Back():
            self.window.destroy()
            import Admin
            Admin.Admin.AdminDashboard(self)

        Button(self.window, text="Continue", command=Continue, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        Button(self.window, text="Back", command=Back, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)

        self.window.mainloop()
