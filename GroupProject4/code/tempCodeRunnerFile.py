    def search_by_name():
        name_to_search = role_search_var.get().lower()

        # Find employees matching the name
        matching_employees = [employee for employee in employee_data if name_to_search in employee["name"].lower()]

        # Clear the Listbox
        employee_listbox.delete(0, tk.END)

        # Add all employee names to the Listbox
        for employee in employee_data:
            employee_listbox.insert(tk.END, employee["name"])

        # Move the matching employee names to the top of the Listbox
        for employee in matching_employees:
            employee_listbox.delete(employee_listbox.get(0, tk.END).index(employee["name"]))
            employee_listbox.insert(0, employee["name"])

            # Move the matching employees to the top of the employee_data list
            employee_data.remove(employee)
            employee_data.insert(0, employee)