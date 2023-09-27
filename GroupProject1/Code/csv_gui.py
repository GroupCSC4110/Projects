"""
Import, append, reverse, and query data from/to CSV Files.
"""
import tkinter as tk
import csv

# Import data function
def import_csv_file(file_path):
    """
    :param param1: File path of CSV File
    :type param1: String
    "return: List of data
    rtype: List
    """
    data = []

    # Open file to read
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row)

    # Error handling
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except FileExistsError:
        print(f"{file_path} does not exist.")

    return data

# Append to file function
def append_csv_file(file_path, data_list):
    """
    :param param1: File path of CSV File
    :param param2: Data List of data to append to file
    :type param1: String
    :type param2: List
    "return: Nothing
    rtype: Nothing
    """

    # Open file to append
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for line in data_list:
                row = line.split(",")  # Split each line by comma to create a list
                csv_writer.writerow(row)

    # Error handling
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except FileExistsError:
        print(f"{file_path} does not exist.")

# Search functions
def query_csv_file(file_path):
    """
    :param param1: File path of CSV File
    :type param1: String
    "return: List of data
    rtype: List
    """
    data = []
    text_widget_query2.config(state=tk.DISABLED)
    data_input = text_widget_query.get()

    # Open file to read and gather data
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[0] == data_input:
                    data.append(row)

    # Error handling
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except FileExistsError:
        print(f"{file_path} does not exist.")
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
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    search.place_forget()
    text_widget_query.place_forget()
    text_widget_query2.place_forget()
    submit.place_forget()
    label.config(text="Data Imported!")
    label.place(x=300, y=0)
    file_path = "order-details.csv"
    csv_data = import_csv_file(file_path)
    text_widget.config(state=tk.DISABLED)
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)

    # Display the CSV data in the Text widget
    for row in csv_data:
        text_widget.insert(tk.END, ", ".join(row) + "\n")

    # Disable the Text widget after displaying the data
    text_widget.config(state=tk.DISABLED)
    text_widget.place(x=125, y=350)

# Search button configuration
def search_click():
    """
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    label.config(text="Data Queried!")
    label.place_configure(x=300, y=0)
    data = query_csv_file(file_path="order-details.csv")
    not_found = len(data) == 0
    text_widget_query2.config(state=tk.NORMAL)
    text_widget_query2.delete("1.0", tk.END)

    # Add data from list to text box
    for string in data:
        text_widget_query2.config(state=tk.NORMAL)
        text_widget_query2.insert(tk.END, ", ".join(string) + "\n")
        text_widget_query2.config(state=tk.DISABLED)

    # If nothing found, print 'Not Found'
    if not_found:
        text_widget_query2.config(state=tk.NORMAL)
        text_widget_query2.delete("1.0", tk.END)
        text_widget_query2.insert(tk.END, "Not Found!\n")
        text_widget_query2.config(state=tk.DISABLED)
    text_widget_query.delete(0, "end")

# Submit button configuration for appending
def submit_click():
    """
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    label.place(x=300, y=0)
    user_input = text_widget_append.get("1.0", tk.END)  # Get the text from the Text widget
    input_list = [line.strip() for line in user_input.split("\n") if line.strip()]

    if input_list:
        append_csv_file("order-details.csv", input_list)
        text_widget_append.delete("1.0", tk.END)  # Clear the Text widget after appending data
        label.config(text="Data Added!")

# Append button configuration
def add_button_click():
    """
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    search.place_forget()
    text_widget_query2.place_forget()
    text_widget_query.place_forget()
    label.config(text="Enter Data (separated by commas) You Wish to Append Into the Textbox!")
    label.place(x=150, y=0)
    text_widget.place_forget()
    text_widget_append.place(x=125, y=350)
    text_widget_append.delete("1.0", tk.END)
    submit.place(x=235, y=550)
    submit.config(command=submit_click)

# Query button configuration
def query_button_click():
    """
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    submit.place_forget()
    text_widget_query2.config(state=tk.NORMAL)
    text_widget_query2.delete("1.0", tk.END)
    text_widget_query2.config(state=tk.DISABLED)
    label.place(x=300, y=0)
    text_widget.place_forget()
    text_widget_append.place_forget()
    label.config(text="Enter data (in first column) to search in small textbox!")
    label.place_configure(x=200, y=0)
    search.place(x=240, y=312)
    text_widget_query.place(x=185, y=290)
    text_widget_query2.place(x=125, y=350)
    search.config(command=search_click)

# Reorganize button configuration
def reorganize_button_click():
    """
    :param param1: None
    :type param1: None
    "return: None
    rtype: None
    """
    label.config(text="Data Re-Organized!")
    label.place(x=300, y=0)
    text_widget.place_forget()
    submit.place_forget()
    search.place_forget()
    text_widget_append.place_forget()
    text_widget_query.place_forget()
    text_widget_query2.place_forget()
    label.place(x=300, y=0)
    csv_file_path = 'order-details.csv'

    # Read the CSV file into a list of lists
    with open(csv_file_path, mode='r', newline='', encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    # Sort the data based on the values in the first column (assuming they are strings)
    data.sort(key=lambda row: row[0])

    # Overwrite the original CSV file with the sorted data
    with open(csv_file_path, mode='w', newline='', encoding="utf-8") as file:
        csv_writer = csv.writer(file)

        # Write the sorted data
        csv_writer.writerows(data)





import_button.config(command=import_button_click)
add_button.config(command=add_button_click)
reorganize_button.config(command=reorganize_button_click)
query_button.config(command=query_button_click)

label.place(x=300, y=0)
import_button.place(x=100, y=100)
add_button.place(x=400, y=100)
reorganize_button.place(x=100, y=200)
query_button.place(x=400, y=200)


app.mainloop()
