from tkinter import *
from tkinter import messagebox , ttk

class Room:

    def ConsultRoom(self,Doc,Pat):
        self.window = Tk()
        self.window.geometry("1280x720")
        self.window.config(bg="#2F4F4F")
        self.window.title("MedCare - Doctor Consultation Room")
        self.window.iconbitmap("./Static/MedCareLogo.ico")

        self.Doctor_Frame = Frame(self.window,height=700,width=600,bg='cyan')
        self.Doctor_Frame.place(x=10,y=10)
        self.DocName = Label(self.Doctor_Frame,font=('Arial',10,'bold'))
        self.DocName.place(x=20,)



        self.Patient_Frame = Frame(self.window,height=700,width=600,bg='cyan')
        self.Patient_Frame.place(x=670,y=10)

        self.window.mainloop()


