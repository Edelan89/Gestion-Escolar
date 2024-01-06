import tkinter as tk
from tkinter import ttk

def toggle_checkbox(day):
    checkboxes[day].toggle()

root = tk.Tk()
root.title("Calendar with Checkboxes")

# Create a list of days in a month (for simplicity, we'll use 1 to 31)
days_in_month = list(range(1, 32))

# Create a dictionary to hold the checkboxes
checkboxes = {}

# Create labels for the days of the week
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
for col, day in enumerate(days_of_week):
    label = tk.Label(root, text=day)
    label.grid(row=0, column=col)

# Create checkboxes for each day in the month
row = 1
col = 0
for day in days_in_month:
    checkboxes[day] = ttk.Checkbutton(root, text=str(day))
    checkboxes[day].grid(row=row, column=col)
    col += 1
    if col == 7:
        col = 0
        row += 1

# Create a button to toggle all checkboxes
toggle_button = tk.Button(root, text="Toggle All", command=lambda: [toggle_checkbox(day) for day in days_in_month])
toggle_button.grid(row=row, column=col, columnspan=7)

root.mainloop()
