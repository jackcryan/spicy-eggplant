from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

root = Tk()
root.title("Title")
root.geometry('600x600')

def close_window(): 
    root.destroy()
    
def openfile():
    C = filedialog.askopenfilename(parent=root, initialdir = "/",title = "Select Image",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    image = Image.open(C)
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)
    
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo
        
menu = Menu(root) #The name of the Menu is menu, located in root#
root.config(menu=menu) #Telling tkinter that our menu is a menu#

subMenu = Menu(menu) #The dropdown menu is named subMenu, located in the menu#
menu.add_cascade(label="File", menu=subMenu) #Adds dropdown functionality to the "File" subMenu#
subMenu.add_command(label="Open", command=openfile) #Adds the Open option in the file dropdown menu#
subMenu.add_separator() #Adds a seperator between File Open and Exit options#
subMenu.add_command(label="Exit", command=close_window) #Adds the Exit option in the file dropdown menu#

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About")

root.mainloop()