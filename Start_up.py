# Import Module
from tkinter import *
from PIL import Image, ImageTk

splash = Tk()
splash.title("Splash image")        

width = splash.winfo_screenwidth()
height = splash.winfo_screenheight()

splash.geometry('{}x{}+{}+{}'.format(width*1, height*1, 0, 0))      

#how long the image stays
splash.after(10000, splash.destroy)  
#reads in the png
picture = PhotoImage(file = "splash_image.png") 
# creates label
lab = Label(splash, image = picture)    
# packs label
lab.pack()     

splash.mainloop()

print("Hello")

print("testing saving from vscode12345")