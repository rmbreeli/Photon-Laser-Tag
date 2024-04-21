import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image
import time
import socket
from supabase_py import create_client, Client
import keyboard
import pygame
import threading
import random

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
player_names_by_equipment_id = {}

# Make a consistent UI/UX theme
# Define color constants
DARK_BG = "#282828"  # A dark gray
LIGHT_FG = "#E0E0E0"  # A light gray
ACCENT_COLOR = "#FF5733"  # A bright accent color for important elements

# Modern font choices
LARGE_FONT = ("Arial", 18, "bold")
MEDIUM_FONT = ("Roboto", 14)
SMALL_FONT = ("Helvetica", 12)

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

# GUI setup
root = tk.Tk()

root.title("Laser Tag Player Entries")

root.configure(bg=DARK_BG)  # Set the background color for the root window

# Standard padding
PADX = 10
PADY = 10

# Create a black canvas for the fullscreen window
black_canvas = tk.Canvas(root, bg=DARK_BG, highlightthickness=0)
black_canvas.grid(row=0, column=0, sticky="nsew")

# Title label
root.title_label = tk.Label(black_canvas, text="     PRESS F5 TO START              PRESS F12 TO CLEAR PLAYERS", fg=ACCENT_COLOR, borderwidth=2, relief=tk.SOLID, bg=DARK_BG)
titleFont = ("ariel", 20, "bold")
root.title_label.grid(row=0, column=0, columnspan=5, sticky="n", padx=PADX, pady=PADY)
root.title_label.configure(font=titleFont)

# Define the frames
blank_frame1 = tk.Frame(black_canvas, bg="black", width=100, height=750)
blank_frame2 = tk.Frame(black_canvas, bg="black", width=100, height=750)
red_frame = tk.Frame(black_canvas, bg="red4", width=300, height=750)
green_frame = tk.Frame(black_canvas, bg="dark green", width=300, height=750)
lower_frame = tk.Frame(black_canvas, bg="black", width=100, height=50)

# Grid layout for the frames
blank_frame1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
red_frame.grid(row=1, column=1, padx=PADX, pady=PADY, sticky="nsew")
green_frame.grid(row=1, column=2, padx=PADX, pady=PADY, sticky="nsew")
blank_frame2.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
lower_frame.grid(row=2, column=0, columnspan=5, pady=10, sticky="nsew")

black_canvas.grid_columnconfigure(0, weight=1)
black_canvas.grid_columnconfigure(1, weight=2)
black_canvas.grid_columnconfigure(2, weight=2)
black_canvas.grid_columnconfigure(3, weight=1)

TeamTitleFont = ("Tekton pro", 15)

def add_player(equipment_id, player_name):
    #Adds a player to the dictionary, mapping their equipment ID to their name.
    player_names_by_equipment_id[equipment_id] = player_name

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
    broadcast_address = ('127.0.0.1', port)

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
    player_id = player_id_entry.get()
    equipment_id = equipment_id_entry.get()  # New line to get equipment ID
    not_in_database = 1

    if not player_id or not equipment_id:  # Check for equipment ID
        messagebox.showerror("Error", "Please enter Player ID and Equipment ID.")
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
        if not player_name:
            messagebox.showerror("Error", "Please enter a Player Name, ID not found.")
            return
        else:
            data_to_insert = {"id": player_id, "Name": player_name}
            supabase.table("Users").insert(data_to_insert).execute()

        

    #if equipment ID is even automatically puts player on the green team
    if int(equipment_id) % 2 == 0:
        player_entries = green_player_entries
        color_frame = green_frame
        players_in_game_green.append([player_name, player_id, equipment_id])
        add_player(equipment_id, player_name)
        print("Current Player Names by Equipment ID:", player_names_by_equipment_id)
        print(players_in_game_green)
    else:
        player_entries = red_player_entries
        color_frame = red_frame
        players_in_game_red.append([player_name, player_id, equipment_id])
        add_player(equipment_id, player_name)
        print("Current Player Names by Equipment ID:", player_names_by_equipment_id)
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

tk.Label(player_entry_frame, text="Player ID:", font=MEDIUM_FONT, fg="white", bg="black").grid(row=0, column=0, padx=5, pady=5)
player_id_entry = tk.Entry(player_entry_frame, font=MEDIUM_FONT, bg="light gray", fg="black", width=18)
player_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(player_entry_frame, text="Player Name:", font=MEDIUM_FONT, fg="white", bg="black").grid(row=1, column=0, padx=5, pady=5)
player_name_entry = tk.Entry(player_entry_frame, font=MEDIUM_FONT, bg="light gray", fg="black", width=18)
player_name_entry.grid(row=1, column=1, padx=5, pady=5)

# Inside the GUI layout section
tk.Label(player_entry_frame, text="Equipment ID:", fg="white", bg="black").grid(row=2, column=0, padx=5, pady=5)
equipment_id_entry = tk.Entry(player_entry_frame, bg="light gray",fg = "black", width=18)
equipment_id_entry.grid(row=2, column=1, padx=5, pady=5)

add_player_button = tk.Button(player_entry_frame, text="Add Player", font=SMALL_FONT, command=add_player_entry)
add_player_button.grid(row=5, column=0, columnspan=2, pady=5)

player_entry_frame.lift()
root.attributes('-topmost', True)

def play_music():
    pygame.mixer.init()  # Initialize the mixer module
    track_number = random.randint(1, 3)  # Generate a random number between 1 and 3
    
    
    tracks = {
        1: "music/Track01_edit.mp3",
        2: "music/Track06.mp3",
        3: "music/Track03.mp3"
    }
    
    track_to_play = tracks[track_number]  
    pygame.mixer.music.load(track_to_play)  
    pygame.mixer.music.play()  

def stop_music():
    pygame.mixer.music.stop()

class GameActionScreen(tk.Tk):
    def __init__(self, players_in_game_red, players_in_game_green):
        super().__init__()

        self.equipment_id_to_name = {} 
        self.player_score_vars = {}  
        self.player_score_entries = {}  
        self.player_name_labels = {}

        self.current_base_holder_red = None  # Track the current base holder for the red team
        self.current_base_holder_green = None  # Track the current base holder for the green team

        # Set up the main window
        self.title("Game Action Screen")
        self.geometry("800x600")
        self.configure(bg="black")
        self.attributes("-topmost", True)

        # Create and configure frames for red and green teams
        self.red_frame = tk.Frame(self, bg="black")
        self.red_frame.grid(row=0, column=0, padx=10, pady=10)

        self.green_frame = tk.Frame(self, bg="black")
        self.green_frame.grid(row=0, column=1, padx=10, pady=10)

        # Create labels for team titles
        self.red_title = tk.Label(self.red_frame, text="Red Team", fg="red", bg="black", font=("Helvetica", 16, "bold"))
        self.red_title.grid(row=0, column=0, columnspan=2)

        self.green_title = tk.Label(self.green_frame, text="Green Team", fg="green", bg="black", font=("Helvetica", 16, "bold"))
        self.green_title.grid(row=0, column=1, columnspan=2)

        # Create and configure action box
        self.action_box = tk.Text(self, height=20, width=40, bg="lightgray", fg="black", font=("Helvetica", 15))
        self.action_box.grid(row=0, column=2, padx=10, pady=10)

        # Create and configure team score entry widgets
        self.red_score_var = tk.StringVar()
        self.red_score_var.set("0")
        self.red_score_entry = tk.Entry(self, textvariable=self.red_score_var, fg="red", bg="black", font=("Helvetica", 14, "bold"), width=5)
        self.red_score_entry.grid(row=1, column=0, padx=10, pady=10)

        self.green_score_var = tk.StringVar()
        self.green_score_var.set("0")
        self.green_score_entry = tk.Entry(self, textvariable=self.green_score_var, fg="green", bg="black", font=("Helvetica", 14, "bold"), width=5)
        self.green_score_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create label for timer
        self.timer_label = tk.Label(self, text="Time remaining:", fg="white", bg="black", font=("Helvetica", 14, "bold"))
        self.timer_label.grid(row=1, column=2, padx=10, pady=10, sticky="e")

        self.red_score_entry.insert(0, "0")
        self.green_score_entry.insert(0, "0")


        #Play the beatz
        play_music()

        print("Red Team Data:", players_in_game_red)
        print("Green Team Data:", players_in_game_green)
        
        #putting players into the action screen.
        self.create_team_slots(self.red_frame, "red", players_in_game_red)
        self.create_team_slots(self.green_frame, "green", players_in_game_green)

        self.start_initial_countdown()
        self.listen_for_hits_thread = threading.Thread(target=self.listen_for_hits, daemon=True)
        self.listen_for_hits_thread.start()
        
        self.after(1000, self.check_high_score)

        print("Current Player Names by Equipment ID:", player_names_by_equipment_id)

    

    def listen_for_hits(self):
        """Listens for UDP messages indicating hits and updates the action box."""
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(('127.0.0.1', 7501))

        try:
            print(f"Listening for UDP messages on port {recieve_port}...")
            while True:
                message, address = udp_socket.recvfrom(1024)
                hit_message = message.decode()
                print(f"Received hit message: '{hit_message}'")
                self.display_hit_message(hit_message)
        finally:
            udp_socket.close()

    def display_hit_message(self, hit_message):
        
        formatted_message, equipment_id_hit = self.handle_hit_message(hit_message)
        self.update_scores(hit_message)
        if equipment_id_hit:
            
            self.after(0, lambda: self.action_box.insert(tk.END, f"{formatted_message}\n"))
            # Broadcast the equipment ID of the player who was hit
            self.after(0, lambda: broadcast_udp_message(equipment_id_hit, brodcast_port))

    def handle_hit_message(self, hit_message):
        """Parses the hit message, looks up player names, and returns a formatted string."""
        try:
            equipment_id_hit_by, equipment_id_hit = hit_message.split(":")
            player_hit_by = player_names_by_equipment_id.get(equipment_id_hit_by, "Unknown Player")
            if equipment_id_hit == "53":
                playerOrBase_hit = "Red Base" 
                formatted_message = f"{player_hit_by} hit {playerOrBase_hit}"
            elif equipment_id_hit == "43":
                playerOrBase_hit = "Green Base"
                formatted_message = f"{player_hit_by} hit {playerOrBase_hit}"
            else: 
                playerOrBase_hit = player_names_by_equipment_id.get(equipment_id_hit, "Unknown Player")
                formatted_message = f"{player_hit_by} hit {playerOrBase_hit}"
            
            self.action_box.see(tk.END)  # Auto-scroll to the bottom
            return formatted_message, equipment_id_hit
        except ValueError:
            return "Invalid message format."
        
        
    def update_scores(self, hit_message):
        try:
            equipment_id_hit_by, equipment_id_hit = hit_message.split(":")
            
            # Assign points based on whether it's a base hit or player hit
            if equipment_id_hit == "53" or equipment_id_hit == "43":  
                points = 100
            elif (int(equipment_id_hit_by) % 2 == 0) != (int(equipment_id_hit) % 2 == 0):
                points = 10  # Different teams - Increase score
            else:
                points = -10  # Same team - Decrease score

            self.after(0, lambda: self._adjust_score(equipment_id_hit_by, points))
            
        except ValueError:
            print("Invalid message format.")

    def adjust_score(self, equipment_id, points):
        # This method now only schedules the actual score adjustment to run on the main thread
        self.after(0, lambda: self._adjust_score(equipment_id, points))

    def _adjust_score(self, equipment_id, points, hit_base=False):
        player_name = self.equipment_id_to_name.get(equipment_id, "")
        if player_name:
            # Directly access the Entry widget for individual score
            if player_name in self.player_score_entries:
                score_entry = self.player_score_entries[player_name]
                current_score = int(score_entry.get() or 0)  
                new_score = max(0, current_score + points)   
                
                # Update the Entry widget for individual score
                score_entry.delete(0, tk.END)
                score_entry.insert(0, str(new_score))

            
                if points == 100:  # This indicates a base hit
                    is_red_team = int(equipment_id) % 2 != 0
                    current_base_holder = self.current_base_holder_red if is_red_team else self.current_base_holder_green
                    
                    # Remove "B" from the previous base holder's name, if any
                    if current_base_holder and current_base_holder in self.player_name_labels:
                        previous_label = self.player_name_labels[current_base_holder]
                        previous_label.config(text=current_base_holder)
                        
                    # Add "B" next to the current player's name
                    player_label = self.player_name_labels.get(player_name, None)
                    if player_label:
                        player_label.config(text=f"{chr(9399)} {player_name}")
                        # Update the current base holder tracker
                        if is_red_team:
                            self.current_base_holder_red = player_name
                        else:
                            self.current_base_holder_green = player_name

                
               
                if int(equipment_id) % 2 == 0:  
                    current_team_score = int(self.green_score_var.get() or 0)
                    new_team_score = current_team_score + points
                    self.green_score_var.set(str(new_team_score))
                    self.green_score_entry.delete(0, tk.END)
                    self.green_score_entry.insert(0, str(new_team_score))
                else:  
                    current_team_score = int(self.red_score_var.get() or 0)
                    new_team_score = current_team_score + points
                    self.red_score_var.set(str(new_team_score))
                    self.red_score_entry.delete(0, tk.END)
                    self.red_score_entry.insert(0, str(new_team_score))
                
                print(f"Adjusted score for {player_name}: {new_score}")
            else:
                print(f"Entry widget for {player_name} not found.")
        else:
            print("Player not found.")

    def start_initial_countdown(self):
        self.initial_time = 30  

        def update_initial_timer():
            self.action_box.delete('1.0', tk.END)

            if self.initial_time > 0:
               
                self.action_box.insert(tk.END, f"Prepare for battle! {self.initial_time} seconds remaining...\n")
                self.action_box.see(tk.END)  # Auto-scroll to the bottom
                self.initial_time -= 1
                self.after(1000, update_initial_timer)  # Update every second
                
            else:
                # Clear the action box and start the main game timer
                start_bool = True
                self.action_box.delete('1.0', tk.END)
                # Start the game timer
                self.start_game_timer()

        update_initial_timer()

    def start_game_timer(self):
        self.remaining_time = 360  # 6 minutes in seconds
        self.action_box.insert(tk.END, "The battle begins now!\n")
        broadcast_udp_message(game_start_code, brodcast_port)
        
            
        def update_timer():
            if self.remaining_time > 0:
                minutes, seconds = divmod(self.remaining_time, 60)
                time_str = f"{minutes:02d}:{seconds:02d}"
                self.timer_label.config(text=f"Time remaining: {time_str}")  # Update timer label
                self.remaining_time -= 1
                self.after(1000, update_timer)  # Update every second
            else:
                self.action_box.insert(tk.END, "Time's up!\n")
                stop_music()

                # Broadcast the game end message
                for i in range(3):
                    broadcast_udp_message(str(game_end_code), brodcast_port)

        update_timer()
        
    

    def create_team_slots(self, frame, color, data):
        local_equipment_id_to_name = {}
        local_player_score_vars = {}
        
        row = 2
        for name, player_id, equipment_id in data:
            local_equipment_id_to_name[equipment_id] = name
            score_var = tk.StringVar(value="0")
            local_player_score_vars[name] = score_var
            self.create_player_slot(frame, row, name, score_var, color)
            row += 1
        
        # After creating slots for the team, update the global mappings
        self.equipment_id_to_name.update(local_equipment_id_to_name)
        self.player_score_vars.update(local_player_score_vars)

        print(f"Equipment ID to Name Mapping ({color} team):", local_equipment_id_to_name)
        print(f"Player Score Variables ({color} team):", local_player_score_vars)


    def create_player_slot(self, frame, row, name, score_var, color):
        player_name_label = tk.Label(frame, text=name, fg=color, bg="black", font=("Helvetica", 12))
        player_name_label.grid(row=row, column=0, sticky="w")
        self.player_name_labels[name] = player_name_label  # Store reference to update later if needed


        # Instead of just creating an Entry and setting it aside, store it in the dictionary
        score_entry = tk.Entry(frame, textvariable=score_var, fg=color, bg="black", font=("Helvetica", 10), width=10)
        score_entry.grid(row=row, column=1, sticky="w")
        self.player_score_entries[name] = score_entry

        score_entry.insert(0,"0")

    

    def check_high_score(self):
        highest_score = 0
        highest_player_name = ""
        color_flag = 0

        # Check scores for players in the red team
        for name, player_id, equipment_id in players_in_game_red:
            player_name = self.equipment_id_to_name.get(equipment_id, "")
            if player_name:
            # Directly access the Entry widget for individual score
                if player_name in self.player_score_entries:
                    score_entry = self.player_score_entries[player_name]
                    current_score = int(score_entry.get() or 0)
                    # print("CURRENT SCORE: ", current_score)
            if current_score is not None:
                if current_score > highest_score:
                    highest_score = current_score
                    highest_player_name = name
            else:
                print("No score_var found for player:", name)

        # # Check scores for players in the green team
        for name, player_id, equipment_id in players_in_game_green:
            player_name = self.equipment_id_to_name.get(equipment_id, "")
            if player_name:
            # Directly access the Entry widget for individual score
                if player_name in self.player_score_entries:
                    score_entry = self.player_score_entries[player_name]
                    current_score = int(score_entry.get() or 0)
                    # print("CURRENT SCORE: ", current_score)
            if current_score is not None:
                if current_score > highest_score:
                    color_flag = 1
                    highest_score = current_score
                    highest_player_name = name
            else:
                print("No score_var found for player:", name)

        # print("Highest score: " + highest_player_name)
        # Once you have the highest score and player name, you can handle flashing
        self.flash_player_name(highest_player_name, color_flag)

        # Call this method again after 1000 milliseconds (1 second)
        self.after(1000, self.check_high_score)

    def flash_player_name(self, player_name, color_flag):
        # print("MADE IT HERE")
        label = self.player_name_labels.get(player_name)
        if label:
            # print("MADE IT HERE TOO")
            # Flash the label by changing its background color
            for _ in range(5):  # Flash 5 times
                label.config(bg="black", fg="yellow")  # Change to yellow
                self.update()  # Update the GUI to reflect changes
                time.sleep(0.2)  # Wait 0.2 seconds
                if(color_flag == 0):
                    label.config(bg="black", fg="red")  # Change back to white

                if(color_flag == 1):
                    label.config(bg="black", fg="green")
                self.update()  # Update again
                time.sleep(0.2)  # Wait again

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


def create_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    
root.bind("<F5>", on_f5_press)
root.bind("<F12>", clear_players)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()
