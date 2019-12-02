import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
    
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk, filedialog

import pandas as pd
import numpy as np

from PIL import ImageTk, Image

import sys
import os




    
class GeoViewerapp(tk.Tk):
    
    def __init__(self):
        
        tk.Tk.__init__(self)
        tk.Tk.title(self,'GeoViewer (Version 1.0)')
        tk.Tk.state(self,'zoomed')
        
        #toolbar
        toolbar = tk.Frame(self, height=50, relief='raised', borderwidth=2)
        toolbar.pack(side='top', fill='x')
        #sidebar
        sidebar = tk.Frame(self, width=300, bg='white', height=500, relief='sunken', borderwidth=3)
        sidebar.pack(side='left', fill='y')
        sidebar.grid_rowconfigure(0, weight=1)
        sidebar.grid_columnconfigure(0, weight=1)
        #working window
        container = tk.Frame(self, bg='white', relief='sunken')
        container.pack(side='right', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #filemenu
        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='New Project', command=lambda: self.show_frame(PageOne))
        filemenu.add_separator()
        filemenu.add_command(label='Save', command =save)
        filemenu.add_command(label='Save as', command =lambda: popupmsg('not supported just yet'))
        filemenu.add_command(label='Save as Template', command =lambda: popupmsg('not supported just yet'))
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=Exit)
        menubar.add_cascade(label='File', menu=filemenu)
        
        #datamenu
        DataMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Data", menu=DataMenu)
        DataMenu.add_command(label="Data Options")
        DataMenu.add_separator()
        DataMenu.add_command(label="Add Instrument")
        
        #helpmenu
        helpMenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About")
        
        tk.Tk.config(self, menu=menubar)

        topbar = tk.Frame(self, bg='white', height=50)
        topbar.pack(side='top', fill='x', pady=50, padx=160)
        
        button1 = ttk.Button(topbar, text="Instrument")
        button1.pack(side='left', anchor='center', padx=20)
        
        button1 = ttk.Button(topbar, text="Select Data1", command=selectdata1)
        button1.pack(side='left', anchor='center', padx=20)
        
        button5 = ttk.Button(topbar, text="Select Duration")
        button5.pack(side='top', anchor='center')
        
        f = Figure(figsize=(10,30), dpi=80)
        f.suptitle('Peak Particle Velocity vs. Time', fontsize=20)
        a = f.add_subplot(1,1,1)
        
        aData = pd.read_excel('Slope_Movement_SSR.xlsx', sheet_name='Sheet1')
        vDeformation  = aData['Deformation']
        vDates        = aData['Time']
         
        a.plot(vDates,vDeformation)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side='bottom', pady=20, expand=True, fill='both', anchor='s')

def selectdata1(): 
    C = filedialog.askopenfilename(initialdir = "/",title = "Select Data",filetypes = (("Excel files","*.xlsx"),("all files","*.*")))
    data = pd.read_excel(C, sheet_name='Sheet1')
    df = pd.DataFrame(data, columns=['Time','PPVX'])
    vDates = df['Time']
    vPPVX  = df['PPVX']       

def popupmsg():
    popup = tk.Toplevel()
    popup.wm_title("!")
    label = ttk.Label(popup, text="msg")
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
def Exit():
    app.destroy()

def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
    file = filedialog.asksaveasfile(filetypes = files, defaultextension = '.txt') 
    

 
app = GeoViewerapp()
app.configure(background='white', relief='sunken')
app.iconbitmap(r'icon.ico')
app.mainloop()
