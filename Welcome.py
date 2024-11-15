
from tkinter import *

class Welcome:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Admin Panel")
        self.window.iconbitmap("./Static/MedCareLogo.ico")

        Navbar = Frame(self.window,bg="cyan",height=55)
        Navbar.pack(fill="x",side="top")
        Footer = Frame(self.window,height=20,bg="cyan")
        Footer.pack(fill="x",side="bottom")

        Footer_Text = Label(Footer,text="© 2024 MedCare. All Rights Reserved",fg="black",bg="cyan",font=("Alice",10,"bold"))
        Footer_Text.pack(padx=5)
   
        Header = Label(Navbar, text="Welcome to MedCare", bg="cyan", fg="#2F4F4F", font=("Helvetica", 16, "bold"))
        Header.pack(pady=30)

        def welcome():
            self.window.destroy()
            import Admin
            Admin.Admin.AdminDashboard(self)
        Button(self.window, text="Continue", command=welcome, bg="#4682B4", fg="white", font=("Helvetica", 10, "bold")).pack(pady=20)
        self.window.mainloop()




welcome = Welcome()
