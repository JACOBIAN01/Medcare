from tkinter import *
#Name age id password field - Doctor
#name,age,gender,id,password - Patient


class NewUser:
    def Account(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("New Account")


        def CreateDoctorAccount():
            Label(self.window, text=f"Create new account", bg="#2F4F4F", fg="white", font=("Helvetica", 16, "bold")).pack()
            Label(self.window, text=f"Enter Your Name", bg="#2F4F4F", fg="white", font=("Times", 12, "bold")).pack()
            Name = Entry(self.window)
            Label(self.window, text=f"Enter Your age", bg="#2F4F4F", fg="white", font=("Times", 12, "bold")).pack()
            Age = Entry(self.window)
            Label(self.window, text=f"Enter Your user_id", bg="#2F4F4F", fg="white", font=("Times", 12, "bold")).pack()
            User_ID = Entry(self.window)
            Label(self.window, text=f"Enter Your Password ", bg="#2F4F4F", fg="white", font=("Times", 12, "bold")).pack()
            Password= Entry(self.window)
            
        
            

        






        self.window.mainloop()


