from tkinter import *
#Name age id password field - Doctor
#name,age,gender,id,password - Patient


class NewUser:
    def Account(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("New Account")

        Label(self.window, text=f"Choose Your Role", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()





        def CreateDoctorAccount():
            Label(self.window, text=f"Create new account", bg="#2F4F4F", fg="white", font=("Helvetica", 18, "bold"), pady=10).pack()

            Label(self.window, text=f"Enter Your Name", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Name = Entry(self.window, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()
            Label(self.window, text=f"Enter Your age",  bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Age = Entry(self.window, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()
            Label(self.window, text=f"Enter Your user_id", bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            User_ID = Entry(self.window, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()
            Label(self.window, text=f"Enter Your Password ",  bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Password= Entry(self.window, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()
            Label(self.window, text=f"Enter Your Field",  bg="#2F4F4F", fg="#ADD8E6", font=("Times", 12, "bold")).pack(pady=(10, 0))
            Field = Entry(self.window, font=("Arial", 12), width=30, relief="flat", bd=2, highlightbackground="#ADD8E6", highlightcolor="#ADD8E6", highlightthickness=1).pack()

            Button(self.window, text="Create Account", font=("Helvetica", 12, "bold"), bg="#4682B4", fg="white", activebackground="#5A9BD5", activeforeground="white", relief="flat", bd=3, padx=10, pady=5).pack(pady=20)


        CreateDoctorAccount()

        self.window.mainloop()


nu = NewUser()
nu.Account()