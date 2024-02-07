# Import Module
from tkinter import *

splash = Tk()
splash.title("Welcome")                 # assigning title for splash screen
splash.geometry("500x300+50+50")      # set geometry for splash screen
splash.after(10000, splash.destroy)      # splash screen will destroy after 4 sec 
bg = PhotoImage(file = "splash_image.png") # insert file name to be display
lab = Label(splash, image = bg)         # create label
lab.pack()                              # pack the label

splash.mainloop()

print("Hello")
