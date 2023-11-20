import tkinter as tk
from tkinter import PhotoImage, ttk, simpledialog, messagebox
import csv
import json
import random

def generate_employee_number():
    return str(random.randint(10000, 99999))

def add_employee(role, employees):
    name = simpledialog.askstring("Input", f"Enter {role} name:")
    if name is not None:
        if name.isalpha():
            employee_number = generate_employee_number()
            while any(emp[2] == employee_number for emp in employees):
                employee_number = generate_employee_number()

            employees.append((name.lower(), role.lower(), employee_number))
            write_to_csv(employees)
            convert_to_json(employees)  # Automatically convert to JSON after adding
            messagebox.showinfo("Success", f"{name} added successfully to {role}!\nEmployee Number: {employee_number}")
        else:
            messagebox.showerror("Error", "Invalid characters in the employee name! Only letters are allowed.")

def view_employees(role, employees):
    role_employees = [(emp[0], emp[1], emp[2]) for emp in employees if emp[1] == role.lower()]
    counter = len(role_employees)
    if role_employees:
        info = "\n".join([f"Name: {name.title()}\nRole: {role.title()}\nEmployee Number: {emp_num}\n{'-'*20}" for name, role, emp_num in role_employees])
        messagebox.showinfo(f"{role} Employees", f"Total Employees: {counter}\n\n{info}")
    else:
        messagebox.showinfo(f"{role} Employees", f"No {role} employees found!")

def search_employee(role, employees):
    name = simpledialog.askstring("Input", f"Enter {role} name:")
    if name is not None:
        search_result = [(emp[0], emp[1], emp[2]) for emp in employees if name.lower() in emp[0] and emp[1] == role.lower()]
        if search_result:
            info = "\n".join([f"Name: {name}\nRole: {role}\nEmployee Number: {emp_num}\n{'-'*20}" for name, role, emp_num in search_result])
            messagebox.showinfo("Search Result", info)
        else:
            messagebox.showinfo("Search Result", f"No {role} employee with the name '{name}' found!")

def update_employee(role, employees):
    old_name = simpledialog.askstring("Input", f"Enter current {role} name:")
    if old_name is not None:
        old_name_lower = old_name.lower()
        role_employees = [emp for emp in employees if emp[1] == role.lower()]
        if any(old_name_lower in emp for emp in role_employees):
            # Find the employee with the given name and role
            for i, emp in enumerate(employees):
                if emp[0] == old_name_lower and emp[1] == role.lower():
                    # Ask the user which information to update
                    update_choice = simpledialog.askstring("Input", f"Update name or role for {old_name}?\nEnter 'name' or 'role':")
                    if update_choice is not None:
                        if update_choice.lower() == 'name':
                            new_name = simpledialog.askstring("Input", f"Enter new {role} name:")
                            if new_name is not None:
                                employees[i] = (new_name.lower(), role.lower(), emp[2])
                                write_to_csv(employees)
                                convert_to_json(employees)  # Automatically convert to JSON after updating
                                messagebox.showinfo("Success", f"{old_name} updated to {new_name} successfully!")
                        elif update_choice.lower() == 'role':
                            new_role = simpledialog.askstring("Input", f"Enter new role for {old_name}:")
                            if new_role is not None:
                                employees[i] = (emp[0], new_role.lower(), emp[2])
                                write_to_csv(employees)
                                convert_to_json(employees)  # Automatically convert to JSON after updating
                                messagebox.showinfo("Success", f"Role for {old_name} updated to {new_role} successfully!")
                        else:
                            messagebox.showerror("Error", "Invalid choice. Please enter 'name' or 'role'.")
                    break
        else:
            messagebox.showinfo("Error", f"No {role} employee with the name '{old_name}' found!")

def delete_employee(role, employees):
    name = simpledialog.askstring("Input", f"Enter {role} name to delete:")
    if name is not None:
        name_lower = name.lower()
        role_employees = [emp for emp in employees if emp[1] == role.lower()]
        if any(name_lower in emp for emp in role_employees):
            employees[:] = [emp for emp in employees if not (name_lower in emp and emp[1] == role.lower())]
            write_to_csv(employees)
            convert_to_json(employees)  # Automatically convert to JSON after deleting
            messagebox.showinfo("Success", f"{name} deleted successfully!")
        else:
            messagebox.showinfo("Error", f"No {role} employee with the name '{name}' found!")

def write_to_csv(employees):
    with open('employee_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Employee Name', 'Role', 'Employee Number'])
        for emp in employees:
            csv_writer.writerow([emp[0], emp[1], emp[2]])

def convert_to_json(employees):
    json_data = {
        "employees": [
            {"name": emp[0], "role": emp[1], "employee_number": emp[2]} for emp in employees
        ]
    }
    with open('employee_data.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

def read_csv_data():
    try:
        with open('employee_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            return [tuple(row) for row in csv_reader]
    except FileNotFoundError:
        return []

def generate_role_window(role, employees):
    role_window = tk.Toplevel(root)
    role_window.title(f"{role} Window")
    role_window.geometry("500x500")

    add_button = ttk.Button(role_window, text=f"Add {role} Employee", command=lambda: add_employee(role, employees))
    view_button = ttk.Button(role_window, text=f"View {role} Employees", command=lambda: view_employees(role, employees))
    search_button = ttk.Button(role_window, text=f"Search {role} Employee", command=lambda: search_employee(role, employees))
    update_button = ttk.Button(role_window, text=f"Update {role} Employee", command=lambda: update_employee(role, employees))
    delete_button = ttk.Button(role_window, text=f"Delete {role} Employee", command=lambda: delete_employee(role, employees))

    add_button.pack(fill=tk.BOTH, padx=10, pady=5)
    view_button.pack(fill=tk.BOTH, padx=10, pady=5)
    search_button.pack(fill=tk.BOTH, padx=10, pady=5)
    update_button.pack(fill=tk.BOTH, padx=10, pady=5)
    delete_button.pack(fill=tk.BOTH, padx=10, pady=5)

root = tk.Tk()
root.title("Main Window")
root.geometry("800x800")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", padding=6, relief="flat", background="#FFFDD0")
style.configure("TLabel", padding=6, background="#FFFDD0", font=("Helvetica", 24))
style.configure("TFrame", padding=6, background="#FFFDD0")
style.configure("TEntry", padding=6)
root.configure(bg="#0089BB")

image_1 = PhotoImage(file="./images/GD_new.png")
image_2 = PhotoImage(file="./images/SD_new.png")
image_3 = PhotoImage(file="./images/J_new.png")
image_4 = PhotoImage(file="./images/HR_new.png")
image_5 = PhotoImage(file="./images/MK_new.png")

def on_button_click(role):
    employees = read_csv_data()
    generate_role_window(role, employees)

label_title = ttk.Label(root, text="Employee Tracker")

button_GD = ttk.Button(root, image=image_1, command=lambda: on_button_click("Graphic Design"), text="Graphic Design", compound=tk.TOP)
button_SD = ttk.Button(root, image=image_2, command=lambda: on_button_click("Software Developers"), text="Software Developers", compound=tk.TOP)
button_J = ttk.Button(root, image=image_3, command=lambda: on_button_click("Janitorial"), text="Janitorial", compound=tk.TOP)
button_HR = ttk.Button(root, image=image_4, command=lambda: on_button_click("Human Resources"), text="Human Resources", compound=tk.TOP)
button_MK = ttk.Button(root, image=image_5, command=lambda: on_button_click("Marketing"), text="Marketing", compound=tk.TOP)

label_title.grid(row=0, column=1, padx=10, pady=10)
button_GD.grid(row=1, column=0, padx=10, pady=10)
button_SD.grid(row=1, column=1, padx=10, pady=10)
button_J.grid(row=1, column=2, padx=10, pady=10)
button_HR.grid(row=2, column=0, padx=10, pady=10)
button_MK.grid(row=2, column=1, padx=10, pady=10)

# Automatically convert to JSON when the application starts
convert_to_json(read_csv_data())

root.mainloop()
