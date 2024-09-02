from tkinter import *
import webbrowser
from tkinterweb import *


class Patient_Dashboard:
    def __init__(self):
            window = Tk()
            window.config(bg="lightblue")
            window.title("Welcome to Medcare")
            window.geometry("1000x600")
            global meet_url
            meet_url = "https://meet.google.com/ade-jgfs-esc"

            
            def open_meet():
                 webbrowser.open(meet_url)

            meet_button = Button(window, text="Consult with DOctor", command=open_meet, font=("Helvetica", 15), bg='gray')
            meet_button.pack(pady=50)

    

            self.window.mainloop()