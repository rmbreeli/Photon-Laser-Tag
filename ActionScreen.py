import tkinter as tk
from tkinter import ttk
import time
import keyboard

class LaserTagGameScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Laser Tag Game Screen")

        # Variables for teams and scores
        self.red_team_score = tk.StringVar()
        self.green_team_score = tk.StringVar()
        self.action_text = tk.StringVar()
        self.time_remaining = tk.StringVar()  # Add this line to fix the error

        # Initialize GUI
        self.initialize_gui()

        # Start the game timer
        self.start_game_timer()
    

    def on_f12_pressed(e):
        print("F12 key pressed! Perform your action here.")

    keyboard.on_press_key("F12", on_f12_pressed)
        
    def initialize_gui(self):
        # Create labels for red team, green team, scores, and action
        ttk.Label(self.root, text="Red Team", font=("Helvetica", 14)).grid(row=0, column=0, padx=10, pady=5)
        ttk.Label(self.root, text="Green Team", font=("Helvetica", 14)).grid(row=0, column=2, padx=10, pady=5)

        ttk.Label(self.root, textvariable=self.red_team_score, font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
        ttk.Label(self.root, textvariable=self.green_team_score, font=("Helvetica", 12)).grid(row=1, column=2, padx=10, pady=5)

        ttk.Label(self.root, text="Action:", font=("Helvetica", 14)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        ttk.Label(self.root, textvariable=self.action_text, font=("Helvetica", 14)).grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky="w")

        ttk.Label(self.root, text="Time Remaining:", font=("Helvetica", 14)).grid(row=3, column=2, padx=10, pady=5, sticky="e")
        ttk.Label(self.root, textvariable=self.time_remaining, font=("Helvetica", 14)).grid(row=3, column=3, padx=10, pady=5, sticky="e")

    def update_scores(self, red_score, green_score):
        self.red_team_score.set(f"Red: {red_score}")
        self.green_team_score.set(f"Green: {green_score}")

    def update_action(self, action_text):
        self.action_text.set(action_text)

    def start_game_timer(self):
        self.remaining_time = 600  # 10 minutes in seconds

        def update_timer():
            if self.remaining_time > 0:
                minutes, seconds = divmod(self.remaining_time, 60)
                self.time_remaining.set(f"{minutes:02d}:{seconds:02d}")
                self.remaining_time -= 1
                self.root.after(1000, update_timer)
            else:
                self.time_remaining.set("Time's up!")

        update_timer()


# Example usage:
if __name__ == "__main__":

    
    root = tk.Tk()
    game_screen = LaserTagGameScreen(root)

    # Example updates (replace with your actual game logic)
    game_screen.update_scores(0, 0)
    game_screen.update_action("Game started!")

    root.mainloop()




