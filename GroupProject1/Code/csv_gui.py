"""
Import file, print data, append data, query data, and reverse data
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox  # Import the messagebox module
import csv

# Global variable to store the file path
FILE_PATH = None

# Import data function
def import_csv_file():
    """
    param: None
    typeParam: None
    rReturn: List of data
    rtype: List
    """
    data = []
    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return []
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row)

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{FILE_PATH}' was not found!")  # Show error
    except FileExistsError:
        messagebox.showerror("Error", f"{FILE_PATH} does not exist!")  # Show error

    return data

# Append to file function
def append_csv_file(data_list):
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    try:
        with open(FILE_PATH, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for line in data_list:
                row = line.split(",")
                csv_writer.writerow(row)

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{FILE_PATH}' was not found!")  # Show error
    except FileExistsError:
        messagebox.showerror("Error", f"{FILE_PATH} does not exist!")  # Show error

# Search functions
def query_csv_file():
    """
    param: None
    typeParam: None
    rReturn: List of data
    rtype: List
    """

    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return []
    data = []
    text_widget_query2.config(state=tk.DISABLED)
    data_input = text_widget_query.get()
    try:
        with open(FILE_PATH, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row and row[0] == data_input:
                    data.append(row)

    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{FILE_PATH}' was not found!")  # Show error
        return []
    except FileExistsError:
        messagebox.showerror("Error", f"{FILE_PATH} does not exist!")  # Show error
        return []

    return data

custom_font = ("Times New Roman", 12)
app = tk.Tk()
app.configure(bg="slategray2")
app.title("Customer Application")
app.geometry("700x700")
app.resizable(0, 0)
label = tk.Label(app, text="Welcome to the GUI!",
                 font=custom_font, bg="slategray2")
import_button = tk.Button(app, text="Import Data from CSV File",
                          font=custom_font, fg="white", bg="skyblue3", height=2, width=20)
query_button = tk.Button(app, text="Query Data from CSV File",
                         font=custom_font, fg="white", bg="skyblue3", height=2, width=20)
add_button = tk.Button(app, text="Add Data to CSV File",
                       font=custom_font, fg="white", bg="skyblue3", height=2, width=20)
reorganize_button = tk.Button(app, text="Re-Organize Data in CSV File",
                              font=custom_font, fg="white", bg="skyblue3", height=2, width=20)
submit = tk.Button(app, text="Append to file",
                   font=custom_font, fg="white", bg="skyblue3", height=2, width=20)
search = tk.Button(app, text="Search",
                   font=custom_font, fg="white", bg="skyblue3", height=1, width=20)
text_widget_append = tk.Text(app, wrap=tk.WORD, width=52,
                             height=10, bg="slategray2")
text_widget = tk.Text(app, wrap=tk.WORD, width=52,
                      height=10, bg="slategray2")
text_widget_query = tk.Entry(app, width=50, bg="slategray2")
text_widget_query2 = tk.Text(app, wrap=tk.WORD, width=52,
                             height=10, bg="slategray2")

# Import button configuration
def import_button_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """
    global FILE_PATH
    search.place_forget()
    text_widget_query.place_forget()
    text_widget_query2.place_forget()
    submit.place_forget()
    label.config(text="Data Imported!")
    label.place(x=300, y=0)

    # Ask the user to select a file
    FILE_PATH = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    if not FILE_PATH:
        label.config(text="No file has been imported!")
        return

# Search button configuration
def search_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    label.config(text="Data Queried!")
    label.place_configure(x=300, y=0)
    data = query_csv_file()
    not_found = len(data) == 0
    text_widget_query2.config(state=tk.NORMAL)
    text_widget_query2.delete("1.0", tk.END)

    for string in data:
        text_widget_query2.config(state=tk.NORMAL)
        text_widget_query2.insert(tk.END, ", ".join(string) + "\n")
        text_widget_query2.config(state=tk.DISABLED)

    if not_found:
        text_widget_query2.config(state=tk.NORMAL)
        text_widget_query2.delete("1.0", tk.END)
        text_widget_query2.insert(tk.END, "Not Found!\n")
        text_widget_query2.config(state=tk.DISABLED)
    text_widget_query.delete(0, "end")

# Submit button configuration for appending
def submit_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    label.place(x=300, y=0)
    user_input = text_widget_append.get("1.0", tk.END)
    input_list = [line.strip()
                  for line in user_input.split("\n") if line.strip()]

    if input_list:
        append_csv_file(input_list)
        text_widget_append.delete("1.0", tk.END)
        label.config(text="Data Added!")

# Append button configuration
def add_button_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        search.place_forget()
        text_widget_query2.place_forget()
        text_widget_query.place_forget()
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    search.place_forget()
    text_widget_query2.place_forget()
    text_widget_query.place_forget()
    label.config(
        text="Enter Data (separated by commas) You Wish to Append Into the Textbox!")
    label.place(x=150, y=0)
    text_widget.place_forget()
    text_widget_append.place(x=125, y=350)
    text_widget_append.delete("1.0", tk.END)
    submit.place(x=235, y=550)
    submit.config(command=submit_click)

# Query button configuration
def query_button_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        submit.place_forget()
        text_widget_query2.config(state=tk.NORMAL)
        text_widget_query2.delete("1.0", tk.END)
        text_widget_query2.config(state=tk.DISABLED)
        text_widget.place_forget()
        text_widget_append.place_forget()
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    submit.place_forget()
    text_widget_query2.config(state=tk.NORMAL)
    text_widget_query2.delete("1.0", tk.END)
    text_widget_query2.config(state=tk.DISABLED)
    label.place(x=300, y=0)
    text_widget.place_forget()
    text_widget_append.place_forget()
    label.config(
        text="Enter data (in first column) to search in small textbox!")
    label.place_configure(x=200, y=0)
    search.place(x=240, y=312)
    text_widget_query.place(x=185, y=290)
    text_widget_query2.place(x=125, y=350)
    search.config(command=search_click)

# Reorganize button configuration
def reorganize_button_click():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """

    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return
    label.config(text="Data Re-Organized!")
    label.place(x=300, y=0)
    text_widget.place_forget()
    submit.place_forget()
    search.place_forget()
    text_widget_append.place_forget()
    text_widget_query.place_forget()
    text_widget_query2.place_forget()
    label.place(x=300, y=0)
    try:
        with open(FILE_PATH, mode='r', newline='', encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            data = list(csv_reader)
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{FILE_PATH}' was not found!")  # Show error
    except FileExistsError:
        messagebox.showerror("Error", f"{FILE_PATH} does not exist!")  # Show error
    data.sort(key=lambda row: row[0])

    try:
        with open(FILE_PATH, mode='w', newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
            csv_writer.writerows(data)
    except FileNotFoundError:
        messagebox.showerror("Error", f"The file '{FILE_PATH}' was not found!")  # Show error
    except FileExistsError:
        messagebox.showerror("Error", f"{FILE_PATH} does not exist!")  # Show error

import_button.config(command=import_button_click)
add_button.config(command=add_button_click)
reorganize_button.config(command=reorganize_button_click)
query_button.config(command=query_button_click)

label.place(x=300, y=0)
import_button.place(x=100, y=100)
add_button.place(x=400, y=100)
reorganize_button.place(x=100, y=200)
query_button.place(x=400, y=200)

# New button to print data in CSV file
def print_csv_data():
    """
    param: None
    typeParam: None
    rReturn: None
    rtype: None
    """
    if not FILE_PATH:
        messagebox.showerror("Error", "No file has been imported!")  # Show error
        return

    csv_data = import_csv_file()
    text_widget.config(state=tk.DISABLED)
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)

    # Display the CSV data in the Text widget
    for row in csv_data:
        text_widget.insert(tk.END, ", ".join(row) + "\n")

    # Disable the Text widget after displaying the data
    text_widget.config(state=tk.DISABLED)
    text_widget.place(x=125, y=350)

print_button = tk.Button(app, text="Print Data in CSV File",
            font=custom_font, fg="white", bg="skyblue3", height=2, width=20, command=print_csv_data)
print_button.place(x=235, y=610)

app.mainloop()
