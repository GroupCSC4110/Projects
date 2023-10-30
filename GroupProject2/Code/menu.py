import subprocess
import tkinter as tk
from tkinter import ttk,PhotoImage
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

def start_game():
    # Use subprocess to run your game
    subprocess.Popen(["python", "Projects\GroupProject2\Code\game.py"])
    root.destroy()

def quit_game():
    root.destroy()


def update_frame():
    try:
        # Get the next frame from the GIF
        animation.seek(animation.tell() + 1)
        img = ImageTk.PhotoImage(animation)
        gif_label.config(image=img)
        gif_label.image = img
        root.after(animation_speed, update_frame)
    except EOFError:
        animation.seek(0)  # Go back to the first frame when the animation ends
        update_frame()



# Create the main window
root = tk.Tk()
root.title("Game Menu")
root.geometry("600x400")
root.config(bg="#000000")

#style object
style=ttk.Style()
theme=ThemedStyle(root)

#confige style
theme.set_theme("plastik")
style.configure("TButton",
                foreground="orange",
                background="black",
                padding=(10,5),
                font=("Helvetica",12),
                borderwidth=2,
                relief="raised")
style.configure("TLabel",
                foreground="#ff6600",  
                background="black", 
                padding=(10, 5))     

#make gif work
animation=Image.open("GroupProject2/Code/1062854907.gif")
img=ImageTk.PhotoImage(animation)
animation_speed=100

#label for gif
gif_label=ttk.Label(root, image=img)

# Create a label for the title
title=PhotoImage(file="GroupProject2/Code/stardefender.png")
title_label = ttk.Label(root, image=title)
title_label.pack(pady=20)
gif_label.pack()
# Create buttons for starting the game and quitting
start_button = ttk.Button(root, text="Start Game", command=start_game)
quit_button = ttk.Button(root, text="Quit", command=quit_game)

start_button.pack()
quit_button.pack()

root.after(0, update_frame)

# Run the Tkinter main loop
root.mainloop()