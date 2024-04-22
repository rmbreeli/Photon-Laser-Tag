import tkinter as tk
import keyboard

x = True
G_FONT = ("Helvetica", 16, "bold")


class GameScreen(tk.Tk):
    def __init__(self):
        super().__init__()

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
        self.red_title = tk.Label(self.red_frame, text="Red Team", fg="red", bg="black", font=(G_FONT))
        self.red_title.grid(row=0, column=0, columnspan=2)

        self.green_title = tk.Label(self.green_frame, text="Green Team", fg="green", bg="black", font=(G_FONT))
        self.green_title.grid(row=0, column=1, columnspan=2)

        # Create and populate red team slots
        red_data = [
            {"name": "John", "ID": 1, "equipment_id": "E001"},
            {"name": "Alice", "ID": 2, "equipment_id": "E002"},
            {"name": "Bob", "ID": 3, "equipment_id": "E003"},
            # Add more data as needed
        ]
        self.create_team_slots(self.red_frame, "red", column=0, data=red_data)

        # Create and populate green team slots
        green_data = [
            {"name": "Charlie", "ID": 4, "equipment_id": "E004"},
            {"name": "Diana", "ID": 5, "equipment_id": "E005"},
            {"name": "Edward", "ID": 6, "equipment_id": "E006"},
            # Add more data as needed
        ]
        self.create_team_slots(self.green_frame, "green", column=1, data=green_data)

        # Create and configure action box
        self.action_box = tk.Text(self, height=10, width=40, bg="lightgray", fg="black", font=("Helvetica", 15))
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

    def create_team_slots(self, frame, color, column, data):
        # Create and populate team slots
        tk.Label(frame, text="Name", fg=color, bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=column)
        tk.Label(frame, text="Score", fg=color, bg="black", font=("Helvetica", 12, "bold")).grid(row=1, column=column + 1)

        count = 2
        for entry in data:
            tk.Label(frame, text=entry["name"], fg=color, bg="black", font=("Helvetica", 10)).grid(row=count, column=column)
            tk.Entry(frame, textvariable=tk.StringVar(), fg=color, bg="black", font=("Helvetica", 10), width=10).grid(row=count, column=column + 1)
            count += 1

def on_f12_pressed(e):
    print("F12 key pressed")
    game_screen = GameScreen()
    game_screen.mainloop()

keyboard.on_press_key("F12", on_f12_pressed)

if __name__ == "__main__":
    while x:
        y = 1
