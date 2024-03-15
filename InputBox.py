import tkinter as tk
from tkinter import messagebox

def display_color(name, color):
    message = f"Hello, {name}! You selected {color}."

    # Display a message box with the selected color
    messagebox.showinfo("Color Selection", message)

def main():
    # Function to handle the button click event
    def on_button_click():
        selected_name = name_entry.get()
        selected_color = color_var.get()

        # Check if a name is entered
        if not selected_name:
            messagebox.showwarning("Input Error", "Please enter a name.")
            return

        # Check if a color is selected
        if not selected_color:
            messagebox.showwarning("Input Error", "Please select a color.")
            return

        # Display the selected color in a message box
        display_color(selected_name, selected_color)

    # Create the main window
    root = tk.Tk()
    root.title("Color Selector")

    # Entry for user to input their name
    name_label = tk.Label(root, text="Enter your name:")
    name_label.pack()

    #aidan made this comment
    name_entry = tk.Entry(root)
    name_entry.pack()

    # Radio buttons for color selection
    color_label = tk.Label(root, text="Select a color:")
    color_label.pack()

    color_var = tk.StringVar()
    red_button = tk.Radiobutton(root, text="Red", variable=color_var, value="Red")
    red_button.pack()

    green_button = tk.Radiobutton(root, text="Green", variable=color_var, value="Green")
    green_button.pack()

    # Button to submit the form
    submit_button = tk.Button(root, text="Submit", command=on_button_click)
    submit_button.pack()

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
