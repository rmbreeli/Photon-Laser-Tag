import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import socket
from supabase_py import create_client, Client

# xZmV05zR7JaK9N8u DO NOT DELETE

#URL & Key to connect with Supabase
url = "https://gntzynfeplzsjtwuzwpb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdudHp5bmZlcGx6c2p0d3V6d3BiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNzAyMDMsImV4cCI6MjAyMjg0NjIwM30.WBravl32P51EEqg-BykO2QyUoxgfINwCpvnVGXIbazM"
supabase: Client = create_client(url, key)


name_counter = 0
red_player_entries = []
green_player_entries = []
red_ID_entries = []
green_ID_entries =[]

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

time.sleep(1)
root = tk.Tk()

root.title("Laser Tag Player Entries")

# Create a black canvas for the fullscreen window
black_canvas = tk.Canvas(root, bg="black", highlightthickness=0)
black_canvas.grid(row=0, column=0, sticky="nsew")

root.title_label = tk.Label(black_canvas, text="Edit Current Game", fg="medium purple", borderwidth=2, relief=tk.SOLID, bg="black")
titleFont = ("ariel", 20, "bold")
root.title_label.grid(row=0, column=0, columnspan=5, sticky="n")
root.title_label.configure(font=titleFont)

# Define the frames
blank_frame1 = tk.Frame(black_canvas, bg="black", width=100, height=750)
blank_frame2 = tk.Frame(black_canvas, bg="black", width=100, height=750)
red_frame = tk.Frame(black_canvas, bg="red4", width=300, height=750)
green_frame = tk.Frame(black_canvas, bg="dark green", width=300, height=750)
lower_frame = tk.Frame(black_canvas, bg="black", width=100, height=50)

# Grid layout for the frames
blank_frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
red_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
green_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
blank_frame2.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
lower_frame.grid(row=2, column=0, columnspan=5, pady=10, sticky="nsew")

black_canvas.grid_columnconfigure(0, weight=1)
black_canvas.grid_columnconfigure(1, weight=2)
black_canvas.grid_columnconfigure(2, weight=2)
black_canvas.grid_columnconfigure(3, weight=1)

TeamTitleFont = ("Tekton pro", 15)

# Function to create a hollow square
def create_hollow_square(canvas, size):
    canvas.create_rectangle(1, 1, size-1, size-1, outline="light gray", width=2)

# Grid layout for the red frame
redTitle = tk.Label(red_frame, text="RED TEAM", fg="light gray", relief=tk.SOLID, bg="red4", highlightthickness=2)
redTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
redTitle.configure(font=TeamTitleFont)
red_frame.grid_columnconfigure(0, weight=1)

for i in range(20):
    # Create a canvas for each row
    canvas = tk.Canvas(red_frame, bg="red4", width=20, height=20, highlightthickness=0)
    canvas.grid(row=i+1, column=0, padx=5, pady=5, sticky="nsew")

    # Draw a hollow square
    create_hollow_square(canvas, 20)

    # Add the label with the number
    row_number_label = tk.Label(canvas, text=str(i), bg="red4", fg="light gray", width=1, height=1)
    row_number_label.place(relx=0.5, rely=0.5, anchor="center")

    player_id_entry = tk.Entry(red_frame, bg="light gray", width=18)
    player_id_entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="nsew")

    id_entry = tk.Entry(red_frame, bg="light gray", width=20)
    id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

    equipment_id_entry = tk.Entry(red_frame, bg ="light gray", width = 10)
    equipment_id_entry.grid(row=i+1, column=3, padx=5, pady=5, sticky="nsew")

    red_player_entries.append(player_id_entry)
    red_ID_entries.append(id_entry)

# Grid layout for the green frame
greenTitle = tk.Label(green_frame, text="GREEN TEAM", fg="light gray", relief=tk.SOLID, bg="dark green", highlightthickness=2)
greenTitle.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
greenTitle.configure(font=TeamTitleFont)
green_frame.grid_columnconfigure(0, weight=1)

for i in range(20):
    # Create a canvas for each row
    canvas = tk.Canvas(green_frame, bg="dark green", width=20, height=20, highlightthickness=0)
    canvas.grid(row=i+1, column=0, padx=5, pady=5, sticky="nsew")

    # Draw a hollow square
    create_hollow_square(canvas, 20)

    # Add the label with the number
    row_number_label = tk.Label(canvas, text=str(i), bg="dark green", fg="light gray", width=1, height=1)
    row_number_label.place(relx=0.5, rely=0.5, anchor="center")

    player_id_entry = tk.Entry(green_frame, bg="light gray", width=18)
    player_id_entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="nsew")
    
    id_entry = tk.Entry(green_frame, bg="light gray", width=20)
    id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

    equipment_id_entry = tk.Entry(green_frame, bg ="light gray", width = 10)
    equipment_id_entry.grid(row=i+1, column=3, padx=5, pady=5, sticky="nsew")
    

    green_player_entries.append(player_id_entry)
    green_ID_entries.append(id_entry)

# Grid layout for the lower section
def create_frames(frame, num_frames):
    for i in range(num_frames):
        box_frame = tk.Frame(frame, bg="black", width=20, height=50, borderwidth=1, relief=tk.SOLID)
        box_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
        frame.grid_columnconfigure(i, weight=1)

# Grid layout for the lower frame
create_frames(lower_frame, 12)

# Make the single row in the lower frame expand
lower_frame.grid_rowconfigure(0, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

def broadcast_udp_message(message, port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enable broadcasting
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Set the broadcast address and port
    broadcast_address = ('<broadcast>', port)

    try:
        # Send the UDP packet
        udp_socket.sendto(message.encode(), broadcast_address)
        print(f"Broadcasted message '{message}' to port {port}")

    finally:
        # Close the socket
        udp_socket.close()


def add_player_entry():
    player_name = player_name_entry.get()
    team_color = team_color_var.get()
    player_id = player_id_entry.get()
    equipment_id = equipment_id_entry.get()  # New line to get equipment ID
    not_in_database = 1

    if not player_name or not player_id or not equipment_id:  # Check for equipment ID
        messagebox.showerror("Error", "Please enter player name, ID, and equipment ID.")
        return
    
    supabase_data = supabase.table('Users').select("*").execute()
    
    for entry in supabase_data['data']:
        if (str)(entry['id']) == player_id:
            player_id = entry['id']
            player_name = entry['Name']
            not_in_database = 0

            
        if(not_in_database == 1):
            data_to_insert = {"id": player_id, "Name": player_name}
            supabase.table("Users").insert(data_to_insert).execute()


    if team_color == "Red":
        player_entries = red_player_entries
        color_frame = red_frame
    else:
        player_entries = green_player_entries
        color_frame = green_frame

    for i, entry in enumerate(player_entries, start=1):
        if not entry.get():
            #insert player name
            entry.insert(0, player_name)

            # Insert player ID
            id_entries = color_frame.grid_slaves(row=i, column=2)
            if id_entries:
                id_entries[0].insert(0, player_id)

            # Insert equipment ID
            equipment_id_entries = color_frame.grid_slaves(row=i, column=3)
            if equipment_id_entries:
                equipment_id_entries[0].insert(0, equipment_id)

            broadcast_udp_message(equipment_id, 7500)

            break

    player_name_entry.delete(0, tk.END)
    player_id_entry.delete(0, tk.END)
    equipment_id_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Laser Tag Player Entries")



window_width = 240 # Set width of the window
window_height = 200  # Set height of the window

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{window_width}x{window_height}+1025+0")


# Add player entry section
player_entry_frame = tk.LabelFrame(root, text="Player Entry", bg="black", fg="white")
player_entry_frame.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

tk.Label(player_entry_frame, text="Player Name:", fg="white", bg="black").grid(row=0, column=0, padx=5, pady=5)
player_name_entry = tk.Entry(player_entry_frame, bg="light gray", width=18)
player_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(player_entry_frame, text="Player ID:", fg="white", bg="black").grid(row=1, column=0, padx=5, pady=5)
player_id_entry = tk.Entry(player_entry_frame, bg="light gray", width=18)
player_id_entry.grid(row=1, column=1, padx=5, pady=5)

# Inside the GUI layout section
tk.Label(player_entry_frame, text="Equipment ID:", fg="white", bg="black").grid(row=2, column=0, padx=5, pady=5)
equipment_id_entry = tk.Entry(player_entry_frame, bg="light gray", width=18)
equipment_id_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(player_entry_frame, text="Team Color:", fg="white", bg="black").grid(row=3, column=0, padx=5, pady=5)
team_color_var = tk.StringVar(value="Red")
team_color_entry = tk.OptionMenu(player_entry_frame, team_color_var, "Red", "Green")
team_color_entry.grid(row=3, column=1, padx=5, pady=5)

def on_team_color_change(*args):
    selected_team_label.config(text=f"Selected Team: {team_color_var.get()}")

team_color_var.trace_add("write", on_team_color_change)

selected_team_label = tk.Label(player_entry_frame, text="Selected Team: Red", fg="white", bg="black")
selected_team_label.grid(row=4, column=0, columnspan=2, pady=5)

add_player_button = tk.Button(player_entry_frame, text="Add Player", command=add_player_entry)
add_player_button.grid(row=5, column=0, columnspan=2, pady=5)

player_entry_frame.lift()
root.attributes('-topmost', True)
# Adjusting the column weight for the new layout.
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()