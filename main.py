
from tkinter import *
from PIL import Image , ImageTk


class Patient_Welcome_Page:

    def __init__(self):
        # Window setup
        p_window = Tk()
        p_window.title("MedCare Plus Patient")
        p_window.geometry("1000x600")
        p_window.config(background='lightblue')

        Login_text = Label(p_window,text="LogIn to Medcare Plus",font=("Helvetica",30,"bold"))
        Login_text.pack()

        # Username Label and Entry
        username_text = Label(p_window, text="Enter Username", font=("Helvetica", 15), bg='lightblue')
        username_text.pack(pady=10)
        username_entry = Entry(p_window, font=("Helvetica", 13), width=30)
        username_entry.pack(pady=10)

        # Password Label and Entry
        password_text = Label(p_window, text="Enter Password", font=("Helvetica", 15), bg='lightblue')
        password_text.pack(pady=10)
        password_entry = Entry(p_window, show='*', font=("Helvetica", 13), width=30)
        password_entry.pack(pady=10)

        #Submit Button
        import Patient_Dashboard
        def Open_Patient_Dashboard():
            p_window.destroy()
            Patient_Dashboard.Patient_Dashboard()
            
        Submit = Button(text="LogIN",command=Open_Patient_Dashboard,font=("Helvetica", 15,"bold"), background="#00796b",  foreground="white", padx=20, pady=10, bd=3)
        Submit.pack()




        p_window.mainloop()

class Doctor_Welcome_Page:
    def __init__(self):
        # Window setup
        d_window = Tk()
        d_window.title("MedCare Plus - Doctor Portal")
        d_window.geometry("1000x600")
        d_window.config(background='lightblue')

        Login_text = Label(d_window,text="LogIn to Medcare Plus",font=("Helvetica",30,"bold"))
        Login_text.pack()

        # Username Label and Entry
        username_text = Label(d_window, text="Enter Username", font=("Helvetica", 15), bg='lightblue')
        username_text.pack(pady=10)
        username_entry = Entry(d_window, font=("Helvetica", 13), width=30)
        username_entry.pack(pady=10)

        # Password Label and Entry
        password_text = Label(d_window, text="Enter Password", font=("Helvetica", 15), bg='lightblue')
        password_text.pack(pady=10)
        password_entry = Entry(d_window, show='*', font=("Helvetica", 13), width=30)
        password_entry.pack(pady=10)

        #FUnction
        import Doctor_Dashboard
        def Open_Doctor_Dashboard():
            d_window.destroy()
            Doctor_Dashboard.Doctor_Dashboard()


        #Submit Button
        Submit = Button(text="LogIN",command=Open_Doctor_Dashboard,font=("Helvetica", 15,"bold"), background="#00796b",  foreground="white", padx=20, pady=10, bd=3)
        Submit.pack()



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
