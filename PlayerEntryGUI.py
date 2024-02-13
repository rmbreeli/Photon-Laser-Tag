import tkinter as tk

root = tk.Tk()

root.title("Laser Tag Player Entries")

root.attributes('-fullscreen', True)  # Set fullscreen

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

    equipment_id_entry = tk.Entry(red_frame, bg="light gray", width=30)
    equipment_id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

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

    equipment_id_entry = tk.Entry(green_frame, bg="light gray", width=30)
    equipment_id_entry.grid(row=i+1, column=2, padx=5, pady=5, sticky="nsew")

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

root.mainloop()
