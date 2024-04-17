import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import time
import socket
from supabase_py import create_client, Client
import keyboard
import pygame

# xZmV05zR7JaK9N8u DO NOT DELETE

#URL & Key to connect with Supabase
url = "https://gntzynfeplzsjtwuzwpb.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdudHp5bmZlcGx6c2p0d3V6d3BiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDcyNzAyMDMsImV4cCI6MjAyMjg0NjIwM30.WBravl32P51EEqg-BykO2QyUoxgfINwCpvnVGXIbazM"
supabase: Client = create_client(url, key)


game_end_code = '221'
game_start_code = '202'

brodcast_port = 7500
recieve_port = 7501

start_bool = False #used to start the 6 min timer after the 30 sec timer

name_counter = 0
red_player_entries = []
green_player_entries = []
red_ID_entries = []
green_ID_entries =[]
red_equipment_entries =[]
green_equipment_entries =[]
players_in_game_red = []
players_in_game_green = []


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

root.title_label = tk.Label(black_canvas, text="     PRESS F5 TO START              PRESS F12 TO CLEAR PLAYERS", fg="medium purple", borderwidth=2, relief=tk.SOLID, bg="black")
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

    player_id_entry = tk.Entry(red_frame, bg="light gray", fg = "black", width=18)
    player_id_entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="nsew")

    id_entry = tk.Entry(red_frame, bg="light gray", fg = "black", width=20)
    id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

    equipment_id_entry = tk.Entry(red_frame, bg ="light gray", fg = "black", width = 10)
    equipment_id_entry.grid(row=i+1, column=3, padx=5, pady=5, sticky="nsew")

    red_player_entries.append(player_id_entry)
    red_ID_entries.append(id_entry)
    red_equipment_entries.append(equipment_id_entry)

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

    player_id_entry = tk.Entry(green_frame, bg="light gray",fg = "black", width=18)
    player_id_entry.grid(row=i+1, column=1, padx=5, pady=5, sticky="nsew")
    
    id_entry = tk.Entry(green_frame, bg="light gray",fg = "black", width=20)
    id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

    equipment_id_entry = tk.Entry(green_frame, bg ="light gray",fg = "black", width = 10)
    equipment_id_entry.grid(row=i+1, column=3, padx=5, pady=5, sticky="nsew")
    

    green_player_entries.append(player_id_entry)
    green_ID_entries.append(id_entry)
    green_equipment_entries.append(equipment_id_entry)

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


def receive_udp_message(port):
    # Create a UDP socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the port
    udp_socket.bind(('127.0.0.1', port))

    try:
        print(f"Listening for UDP messages on port {port}...")
        while True:
            # Receive message
            message, address = udp_socket.recvfrom(1024)
            print(f"Received message '{message.decode()}' from {address}")

            
    finally:
        # Close the socket
        udp_socket.close()


def add_player_entry():
    player_name = player_name_entry.get()
    #team_color = team_color_var.get()
    player_id = player_id_entry.get()
    equipment_id = equipment_id_entry.get()  # New line to get equipment ID
    not_in_database = 1

    if not player_name or not player_id or not equipment_id:  # Check for equipment ID
        messagebox.showerror("Error", "Please enter player name, ID, and equipment ID.")
        return
    
    # Check if player name contains only alphabetic characters
    if not player_name.isalpha():
        messagebox.showerror("Error", "Player name must only contain alphabetic characters.")
        return
    
    for player in players_in_game_red:
        name, id , equip_id= player
        if name == player_name or id == player_id or equipment_id == equip_id:
            messagebox.showerror("Error", "Please enter a different Player name, ID, or Equipment ID.")
            return
    
    for player in players_in_game_green:
        name, id, equip_id = player
        if name == player_name or id == player_id or equipment_id == equip_id:
            messagebox.showerror("Error", "Please enter a different Player name, ID, or Equipment ID.")
            return

    supabase_data = supabase.table('Users').select("*").execute()

    for entry in supabase_data['data']:
        if str(entry['id']) == player_id:
            player_id = entry['id']
            player_name = entry['Name']
            not_in_database = 0

    if not_in_database == 1:
        data_to_insert = {"id": player_id, "Name": player_name}
        supabase.table("Users").insert(data_to_insert).execute()

    #if equipment ID is even automatically puts player on the green team
    if int(equipment_id) % 2 == 0:
        player_entries = green_player_entries
        color_frame = green_frame
        players_in_game_green.append([player_name, player_id, equipment_id])
        print(players_in_game_green)
    else:
        player_entries = red_player_entries
        color_frame = red_frame
        players_in_game_red.append([player_name, player_id, equipment_id])
        print(players_in_game_red)

    for i, entry in enumerate(player_entries, start=1):
        if not entry.get():
            # insert player name
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

tk.Label(player_entry_frame, text="Player ID:", fg="white", bg="black").grid(row=0, column=0, padx=5, pady=5)
player_id_entry = tk.Entry(player_entry_frame, bg="light gray", fg="black", width=18)
player_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(player_entry_frame, text="Player Name:", fg="white", bg="black").grid(row=1, column=0, padx=5, pady=5)
player_name_entry = tk.Entry(player_entry_frame, bg="light gray", fg="black", width=18)
player_name_entry.grid(row=1, column=1, padx=5, pady=5)

# Inside the GUI layout section
tk.Label(player_entry_frame, text="Equipment ID:", fg="white", bg="black").grid(row=2, column=0, padx=5, pady=5)
equipment_id_entry = tk.Entry(player_entry_frame, bg="light gray",fg = "black", width=18)
equipment_id_entry.grid(row=2, column=1, padx=5, pady=5)

add_player_button = tk.Button(player_entry_frame, text="Add Player", command=add_player_entry)
add_player_button.grid(row=5, column=0, columnspan=2, pady=5)

player_entry_frame.lift()
root.attributes('-topmost', True)

def play_music():
    pygame.init()
    mp3_file_path = "amazing (upload).mp3"
    pygame.mixer.music.load(mp3_file_path)
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()

    

class GameActionScreen(tk.Tk):
    def __init__(self, players_in_game_red, players_in_game_green):
        super().__init__()

        # Set up the main window
        self.title("Game Action Screen")
        self.geometry("800x600")
        self.configure(bg="black")
        self.attributes("-topmost", True)

        # Create and configure frames for red team, action, and green team
        self.red_frame = tk.Frame(self, bg="black")
        self.red_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ns")

        self.action_frame = tk.Frame(self, bg="black")
        self.action_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

        self.green_frame = tk.Frame(self, bg="black")
        self.green_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ns")

        # Configure column weights for layout flexibility
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Create labels for team titles
        self.red_title = tk.Label(self.red_frame, text="Red Team", fg="red", bg="black", font=("Helvetica", 16, "bold"))
        self.red_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.green_title = tk.Label(self.green_frame, text="Green Team", fg="green", bg="black", font=("Helvetica", 16, "bold"))
        self.green_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Create the action box (text area) for the action frame
        self.action_box = tk.Text(self.action_frame, height=30, width=40, bg="lightgray", fg="black", font=("Helvetica", 15))
        self.action_box.grid(row=0, column=0, padx=10, pady=10)

        # Create the timer label inside the action frame
        self.timer_label = tk.Label(self.action_frame, text="Time remaining:", fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.timer_label.grid(row=1, column=0, padx=10, pady=10)

        # Create and configure team score entry widgets in red and green frames
        self.red_score_var = tk.StringVar()
        self.red_score_var.set("0")
        self.red_score_entry = tk.Entry(self.red_frame, textvariable=self.red_score_var, fg="red", bg="black", font=("Helvetica", 14, "bold"), width=5)
        self.red_score_entry.grid(row=1, column=0, pady=10)

        self.green_score_var = tk.StringVar()
        self.green_score_var.set("0")
        self.green_score_entry = tk.Entry(self.green_frame, textvariable=self.green_score_var, fg="green", bg="black", font=("Helvetica", 14, "bold"), width=5)
        self.green_score_entry.grid(row=1, column=0, pady=10)

        # Play the music when the game starts
        play_music()

        # Create team slots (player names and scores) for the red and green frames
        self.create_team_slots(self.red_frame, "red", data=players_in_game_red)
        self.create_team_slots(self.green_frame, "green", data=players_in_game_green)

        # Bind key events to increase scores
        self.bind('<KeyPress-r>', self.increase_red_score)
        self.bind('<KeyPress-g>', self.increase_green_score)

        # Start the initial countdown
        self.start_initial_countdown()

    def create_team_slots(self, frame, color, data):
        # Create and populate team slots in a specific frame (red or green)
        tk.Label(frame, text="Name", fg=color, bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=0)
        tk.Label(frame, text="Score", fg=color, bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=1)

        count = 2
        for entry in data:
            name = entry[0]
            # score = entry[1]
            name_label = tk.Label(frame, text=name, fg=color, bg="black", font=("Helvetica", 12))
            name_label.grid(row=count, column=0, sticky="w")

            # score_label = tk.Label(frame, text=score, fg=color, bg="black", font=("Helvetica", 12))
            # score_label.grid(row=count, column=1, sticky="e")

            count += 1

    def start_initial_countdown(self):
        self.initial_time = 3  # Initial countdown duration in seconds

        # Configure a tag for centering text
        self.action_box.tag_configure("center", justify="center")
        
        # Insert the initial countdown message at the beginning of the action box
        # Use the "center" tag to center the text
        self.action_box.insert(tk.END, f"Prepare for battle! {self.initial_time} seconds remaining...\n", "center")

        def update_initial_timer():
            if self.initial_time > 0:
                # Move the cursor to the start of the first line in the action box
                self.action_box.delete("1.0", "1.0 lineend")  # Delete the existing line
                
                # Insert the updated countdown message at the start of the first line
                # Use the "center" tag to center the text
                self.action_box.insert("1.0", f"Prepare for battle! {self.initial_time} seconds remaining...", "center")
                
                # Decrease the initial time
                self.initial_time -= 1
                
                # Schedule the next update after one second
                self.after(1000, update_initial_timer)
            else:
                # Clear the initial countdown line when complete
                self.action_box.delete("1.0", "1.0 lineend")
                
                # Start the game timer
                self.start_game_timer()

        # Start the initial countdown
        update_initial_timer()



    def start_game_timer(self):
        self.remaining_time = 360  # 6 minutes in seconds

        # Configure a tag for centering text
        self.action_box.tag_configure("center", justify="center")

        def update_timer():
            if self.remaining_time > 0:
                # Calculate minutes and seconds from the remaining time
                minutes, seconds = divmod(self.remaining_time, 60)
                
                # Construct the updated time message
                time_message = f"Time remaining: {minutes:02d}:{seconds:02d}"
                
                # Determine the position of the last line of text in the `action_box`
                last_line_start = self.action_box.index("end-2l")  # Start of the last line
                
                # Update the existing time message at the bottom of the frame
                self.action_box.delete(last_line_start, tk.END)  # Remove current message
                
                # Insert the updated message with the center tag
                self.action_box.insert(last_line_start, f"{time_message}\n", "center")
                
                # Decrease the remaining time
                self.remaining_time -= 1
                
                # Schedule the next update in 1 second
                self.after(1000, update_timer)
            else:
                # Insert message when the time is up
                self.action_box.insert(tk.END, "\nTime's up!\n", "center")
                stop_music()

        # Start the main game timer
        update_timer()



    def increase_red_score(self, event):
        current_score = int(self.red_score_var.get())
        new_score = current_score + 100
        self.red_score_var.set(new_score)
        self.red_score_entry.delete(0, tk.END)
        self.red_score_entry.insert(0, str(new_score))

    def increase_green_score(self, event):
        current_score = int(self.green_score_var.get())
        new_score = current_score + 100
        self.green_score_var.set(new_score)
        self.green_score_entry.delete(0, tk.END)
        self.green_score_entry.insert(0, str(new_score))

game_screen = None

def on_f5_press(event):
    global game_screen
    
    if event.keysym == 'F5':
        if game_screen is not None:
            # Close the existing game screen
            # print("f5 pressed")
            game_screen.destroy()
            game_screen = None
            stop_music()
        else:
            # Open a new game screen
            game_screen = GameActionScreen(players_in_game_red, players_in_game_green)
            game_screen.mainloop()

def clear_players(event):
    if event.keysym == 'F12':
        print("f12 pressed")
        for entry in red_player_entries:
            entry.delete(0, tk.END)

        for entry in green_player_entries:
            entry.delete(0, tk.END)

        for entry in red_ID_entries:
            entry.delete(0, tk.END)

        for entry in green_ID_entries:
            entry.delete(0, tk.END)
        
        for entry in red_equipment_entries:
            entry.delete(0, tk.END)
        
        for entry in green_equipment_entries:
            entry.delete(0, tk.END)

        players_in_game_red.clear()
        players_in_game_green.clear()

    
root.bind("<F5>", on_f5_press)
root.bind("<F12>", clear_players)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
