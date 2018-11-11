import tkinter as tk
from tkinter import *
import client_db_functions
from console import *
import main_page as mp
from login_page import *
from create_account_page import *
from agency_page import *
from admin_page import *
from file_upload_page import *

class TEQPage(tk.Frame):
    def __init__(self, parent, controller, name):
        self.cont = controller
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hello " + name +
                         ". What would you like to do?")
        label.pack(side=TOP,fill=X)

        back = Button(self, text="Back",
                            command=lambda: self.cont.display(mp.MainPage))
        back.pack(side=TOP,fill=X)