import subprocess
import tkinter as tk

def start_game():
    # Use subprocess to run your game
    subprocess.Popen(["python", "Projects\GroupProject2\Code\main.py"])
    root.destroy()

def quit_game():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Game Menu")

# Create a label for the title
title_label = tk.Label(root, text="Welcome to My Game", font=("Helvetica", 24))
title_label.pack(pady=20)

# Create buttons for starting the game and quitting
start_button = tk.Button(root, text="Start Game", command=start_game)
quit_button = tk.Button(root, text="Quit", command=quit_game)

start_button.pack()
quit_button.pack()

# Run the Tkinter main loop
root.mainloop()