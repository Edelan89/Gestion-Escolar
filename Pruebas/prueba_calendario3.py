from tkinter import *
from tkcalendar import DateEntry

root = Tk()

cal = DateEntry(root, width = 30, bg= "darkblue", fg= "white", year = 2023)

cal.grid()

root.mainloop()