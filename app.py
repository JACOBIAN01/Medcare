from tkinter import *
from tkinter import messagebox
from modules.auth import AuthSystem # type: ignore
import modules.dashboard import Dashboard

class MainApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Medcare Plus")
        self.root.geometry("800x600")

        self.auth_system = AuthSystem(self.root,self.show_dashboard)

    def show_dashboard(self,user_type,username):
        #Clear window and show appropriate dashboard
        for widget in self.root.winfo_children():
            widget.destroy()
        
        if user_type == 'patient':
            Dashboard(self.root,user_type='patient',username=username)
        elif user_type =='Doctor':
            Dashboard()
        

        