import tkinter as tk
from tkinter import PhotoImage,ttk

def Graphic_desgin():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("500x500")
    new_window_style=ttk.Style()
    new_window_style.theme_use("clam")
    new_window_style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
    new_window_style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
    new_window_style.configure("TFrame", padding=6, background="#FFFDD0")
    new_window_style.configure("TEntry", padding=6)
    new_window.configure(bg="#0089BB")
        # Define functions for button actions
    def add_employee():
        # Add code here to add a new employee to the tracker
        pass

    def view_employees():
        # Add code here to view the list of employees
        pass

    def search_employee():
        # Add code here to search for a specific employee
        pass

    def update_employee():
        # Add code here to update employee information
        pass

    def delete_employee():
        # Add code here to delete an employee from the tracker
        pass

    # Create buttons for different actions
    add_button = ttk.Button(new_window, text="Add Employee", command=add_employee)
    add_button.pack(fill=tk.BOTH, padx=10, pady=5)

    view_button = ttk.Button(new_window, text="View Employees", command=view_employees)
    view_button.pack(fill=tk.BOTH, padx=10, pady=5)

    search_button = ttk.Button(new_window, text="Search Employee", command=search_employee)
    search_button.pack(fill=tk.BOTH, padx=10, pady=5)

    update_button = ttk.Button(new_window, text="Update Employee", command=update_employee)
    update_button.pack(fill=tk.BOTH, padx=10, pady=5)

    delete_button = ttk.Button(new_window, text="Delete Employee", command=delete_employee)
    delete_button.pack(fill=tk.BOTH, padx=10, pady=5)

    # Create a "Help" button
    help_button = ttk.Button(new_window, text="About")
    help_button.pack(fill=tk.BOTH, padx=10, pady=5)


def Human_resources():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("500x500")
    new_window_style=ttk.Style()
    new_window_style.theme_use("clam")
    new_window_style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
    new_window_style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
    new_window_style.configure("TFrame", padding=6, background="#FFFDD0")
    new_window_style.configure("TEntry", padding=6)
    new_window.configure(bg="#0089BB")
    label = ttk.Label(new_window, text="This is a new window!")
    label.pack()


def janitorial():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("500x500")
    new_window_style=ttk.Style()
    new_window_style.theme_use("clam")
    new_window_style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
    new_window_style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
    new_window_style.configure("TFrame", padding=6, background="#FFFDD0")
    new_window_style.configure("TEntry", padding=6)
    new_window.configure(bg="#0089BB")
    label = ttk.Label(new_window, text="This is a new window!")
    label.pack()

def Software_dev():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("500x500")
    new_window_style=ttk.Style()
    new_window_style.theme_use("clam")
    new_window_style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
    new_window_style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
    new_window_style.configure("TFrame", padding=6, background="#FFFDD0")
    new_window_style.configure("TEntry", padding=6)
    new_window.configure(bg="#0089BB")
    label = ttk.Label(new_window, text="This is a new window!")
    label.pack()

def Marketing():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("500x500")
    new_window_style=ttk.Style()
    new_window_style.theme_use("clam")
    new_window_style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
    new_window_style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
    new_window_style.configure("TFrame", padding=6, background="#FFFDD0")
    new_window_style.configure("TEntry", padding=6)
    new_window.configure(bg="#0089BB")
    label = ttk.Label(new_window, text="This is a new window!")
    label.pack()

root = tk.Tk()
root.title("Main Window")
root.geometry("800x800")

#Style thing
style=ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
style.configure("TLabel", padding=6, background="#FFFDD0",font=("Helvetica", 24))
style.configure("TFrame", padding=6, background="#FFFDD0")
style.configure("TEntry", padding=6)
root.configure(bg="#0089BB")

# Load the image
image_1 = PhotoImage(file="GroupProject3\code\GD_new.png")
image_2 = PhotoImage(file="GroupProject3\code\SD_new.png")
image_3 = PhotoImage(file="GroupProject3\code\J_new.png")
image_4 = PhotoImage(file="GroupProject3\code\HR_new.png")
image_5 = PhotoImage(file="GroupProject3\code\MK_new.png")


#labels for images
label_title=ttk.Label(root,text="Employee Tracker")


# Create a button with the loaded image for graphic design
button_GD= ttk.Button(root, image=image_1, command=Graphic_desgin,text="Graphic Design",compound=tk.TOP)


# Create a button with the loaded image for SD
button_SD= ttk.Button(root, image=image_2, command=Software_dev,text="Software developers",compound=tk.TOP)


# Create a button with the loaded image for J
button_J= ttk.Button(root, image=image_3, command=janitorial,text="Janitorial",compound=tk.TOP)


# Create a button with the loaded image for HR
button_HR= ttk.Button(root, image=image_4, command=Human_resources,text="Human resources",compound=tk.TOP)

# Create a button with the loaded image for HR
button_MK= ttk.Button(root, image=image_5, command=Marketing,text="Marketing",compound=tk.TOP)

#creates layout of buttons on app
label_title.grid(row=0, column=1, padx=10, pady=10)
button_GD.grid(row=1, column=0, padx=10, pady=10)
button_SD.grid(row=1, column=1, padx=10, pady=10)
button_J.grid(row=1, column=2, padx=10, pady=10)
button_HR.grid(row=2, column=0, padx=10, pady=10)
button_MK.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()