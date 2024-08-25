import tkinter
from tkinter import *

class Patient_Welcome_Page:

    def __init__(self):
        # Window setup
        p_window = Tk()
        p_window.title("MedCare Plus Patient")
        p_window.geometry("1000x600")
        p_window.config(background='lightblue')
        
        def back():
            p_window.destroy()
            MainPage() 

        #button
        Back = Button(text="Back",command=back)
        Back.pack()

        p_window.mainloop()

class Doctor_Welcome_Page:
    def __init__(self):
        # Window setup

        d_window = Tk()
        d_window.title("MedCare Plus Doctor")
        d_window.geometry("1000x600")
        d_window.config(background='lightblue')
        def Back():
            d_window.destroy()
            MainPage()

        #Button
        BackButton = Button(text="Back",command=Back)
        BackButton.pack()

        d_window.mainloop()

class MainPage:
    def __init__(self):
        # Window setup
        window = Tk()
        window.title("MedCare Plus")
        window.geometry("1000x600")
        window.config(background='lightblue')
        icon = PhotoImage(file="MedCare Logo.png")
        window.iconphoto(False, icon)
        #FUnctions
        def Doctor():
            window.destroy()
            Doctor_Welcome_Page() #COnstructor Called
        def Patient():
            window.destroy()
            Patient_Welcome_Page()
        #Label:
        Header = Label(text="Welcome to Medcare Portal")
        Header.pack()
        Header2 = Label(text="Please Choose who you are !")
        Header2.pack()

        # Buttons
        Patient_Welcome_Button = Button(text="Patient", command=Patient)
        Patient_Welcome_Button.pack()
        Doctor_Welcome_Button = Button(text="Doctor", command=Doctor)
        Doctor_Welcome_Button.pack()

        window.mainloop()
#Object
MainPage()
