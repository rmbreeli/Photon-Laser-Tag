# Import Module
from tkinter import *
from PIL import Image, ImageTk
from supabase_py import create_client, Client
import time

splash = Tk()
splash.attributes('-fullscreen', True)  # Set fullscreen
splash.title("Splash image")        

width = splash.winfo_screenwidth()
height = splash.winfo_screenheight()

splash.geometry('{}x{}+{}+{}'.format(width*1, height*1, 0, 0))      

#how long the image stays
splash.after(4000, splash.destroy)  
#reads in the png
picture = PhotoImage(file = "splash_image1.png") 
# creates label
lab = Label(splash, image = picture)    
# packs label
lab.pack()     

splash.mainloop()

time.sleep(3)

# xZmV05zR7JaK9N8u DO NOT DELETE

#URL & Key to connect with Supabase
url = "https://gntzynfeplzsjtwuzwpb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdudHp5bmZlcGx6c2p0d3V6d3BiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNzAyMDMsImV4cCI6MjAyMjg0NjIwM30.WBravl32P51EEqg-BykO2QyUoxgfINwCpvnVGXIbazM"
print("Supabase URL:", url)

#Printing contents of the database
supabase: Client = create_client(url, key)
response = supabase.table('Users').select("*").execute()
print(response)

#Adding data to database
while True:
    user_name = input("Enter your name(or 0 to finish player entry)>> ")
    if user_name =='0':
        break
    else:
        supabase.table("Users").insert({"Name": user_name}).execute()



response = supabase.table('Users').select("*").execute()
print(response)

