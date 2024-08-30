import tkinter
from tkinter import *
from PIL import Image , ImageTk

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
        
        #Header
        Header = Label(text="Patient Dashboard")
        Header.pack()

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
        #Header
        Header = Label(text="Patient Dashboard")
        Header.pack()

        #Button
        BackButton = Button(text="Back",command=Back)
        BackButton.pack()

        d_window.mainloop()

class MainPage:
    def __init__(self):
        # Window setup
        window = Tk()
        window.title("MedCare Plus-Welcome")
        window.geometry("1000x600")
        window.config(background="lightblue")
        icon = PhotoImage(file="MedCare Logo.png")
        window.iconphoto(False, icon)       

        #Header
        Header = Label(window,text="Welcome to Medcare Portal",fg="#1a1a1a",bg="#f7f7f7",font=(("Helvetica",30,"bold")),borderwidth=2,relief="ridge")
        Header.pack()

        #Image
        image = Image.open("Welcome_Image.jpg")
        photo = ImageTk.PhotoImage(image)
        
        #Canvas
        canvas = Canvas(window,width=1000,height=400)
        canvas.pack()
        canvas.create_image(0,0,anchor=NW,image=photo)

        Header2 = Label(window,text="Please Choose who you are !",font=("Helvetica",14,"bold"))
        Header2.pack()

        #FUnctions
        def Doctor():
            window.destroy()
            Doctor_Welcome_Page() #COnstructor Called
        def Patient():
            window.destroy()
            Patient_Welcome_Page()


        # Buttons
        Patient_Welcome_Button = Button(window,text="Patient", command=Patient,font=("Helvetica", 15,"bold"),
            background="#00796b",  # Teal color
            foreground="white",
            padx=20,  # Horizontal padding
            pady=10,  # Vertical padding
            bd=3,  # No border
            relief="raised",
            overrelief="ridge",
            cursor="hand2" )
        
        Patient_Welcome_Button.pack(side=LEFT,anchor="center")

        Doctor_Welcome_Button = Button(text="Doctor", command=Doctor,font=("Helvetica", 15,"bold"),
            background="#00796b",  # Teal color
            foreground="white",
            padx=20,  # Horizontal padding
            pady=10,  # Vertical padding
            bd=3,  # No border
            relief="raised",
            overrelief="ridge",
            cursor="hand2" )
        Doctor_Welcome_Button.pack(side=RIGHT,anchor="center")

        window.mainloop()

#Object
MainPage()
