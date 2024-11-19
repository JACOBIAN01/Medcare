from tkinter import *
from tkinter import ttk

class Welcome:
    def WelcomeDashboard(self):
        # Create the main window
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#1E1E2F")  # Dark premium background
        self.window.title("MedCare - Admin Panel")
        self.window.iconbitmap("./Static/MedCareLogo.ico")

        # Navbar
        Navbar = Frame(self.window, bg="#00ADB5", height=55)  # Modern teal accent
        Navbar.pack(fill="x", side="top")
        Header = Label(Navbar, text="Welcome to MedCare", bg="#00ADB5", fg="#EEEEEE",
                       font=("Helvetica", 16, "bold"))
        Header.pack(pady=10)

        # Footer
        Footer = Frame(self.window, height=30, bg="#00ADB5")
        Footer.pack(fill="x", side="bottom")
        Footer_Text = Label(Footer, text="© 2024 MedCare. All Rights Reserved", fg="#EEEEEE", bg="#00ADB5",
                            font=("Helvetica", 10, "italic"))
        Footer_Text.pack(pady=5)

        # Content Section
        ContentFrame = Frame(self.window, bg="#1E1E2F")
        ContentFrame.pack(expand=True)

        WelcomeText = Label(ContentFrame, text="Your Health, Our Priority", bg="#1E1E2F", fg="#EEEEEE",
                            font=("Helvetica", 24, "bold"))
        WelcomeText.pack(pady=40)

        # Modern button style
        style = ttk.Style()
        style.configure("TButton",
                        background="#00ADB5",
                        foreground="black",
                        font=("Helvetica", 12, "bold"),
                        padding=10,
                        borderwidth=0)
        style.map("TButton", background=[("active", "#007A7C")])  # Active hover effect

        def welcome():
            self.window.destroy()
            import Admin
            Admin.Admin.AdminDashboard(self)

        ContinueButton = ttk.Button(ContentFrame, text="Continue", command=welcome, style="TButton")
        ContinueButton.pack(pady=20)

        self.window.mainloop()


welcomeuser = Welcome().WelcomeDashboard()
