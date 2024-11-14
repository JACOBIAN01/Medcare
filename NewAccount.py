from tkinter import *


class NewUser:
    def Account(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("New Account")

        
        def clear_frame():
            for widget in self.window.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()

        def CreatePatientAccount():
            clear_frame()  

            frame = Frame(self.window, padx=20, pady=20, bg="cyan")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            Label(frame, text="Create New Patient Account", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

            Label(frame, text="Enter Your Name", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your Age", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your User ID", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your Password", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1, show="*").pack()

            Label(frame, text="Enter Your Gender", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Button(frame, text="Create Account", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", activebackground="#5A9BD5", activeforeground="white", relief="flat", bd=3, padx=10, pady=5).pack(pady=20)

        def CreateDoctorAccount():
            clear_frame()  # Clear any existing frames

            frame = Frame(self.window, padx=20, pady=20, bg="cyan")
            frame.pack(fill="both", expand=True, padx=10, pady=10)

            Label(frame, text="Create New Doctor Account", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

            Label(frame, text="Enter Your Name", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your Age", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your User ID", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Label(frame, text="Enter Your Password", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1, show="*").pack()

            Label(frame, text="Enter Your Field", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Entry(frame, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Button(frame, text="Create Account", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", activebackground="#5A9BD5", activeforeground="white", relief="flat", bd=3, padx=10, pady=5).pack(pady=20)

        Label(self.window, text="Choose Your Role", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

        roles = ["Doctor", "Patient"]
        selected_role = StringVar(value=roles[0])
        OptionMenu(self.window, selected_role, *roles).pack(padx=10)

        def Continue():
            if selected_role.get() == "Doctor":
                CreateDoctorAccount()
            elif selected_role.get() == "Patient":
                CreatePatientAccount()

        Button(self.window, text="Continue", command=Continue, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)

        self.window.mainloop()


nu = NewUser()
nu.Account()
