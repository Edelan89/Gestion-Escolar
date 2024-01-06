# modules
from tkinter import *
from tkinter import ttk

# create window
ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x200')

# frames to store separators with different geometry managers
frame1 = Frame(ws)
frame1.pack(side=LEFT, expand=True, fill=BOTH)

frame2 = Frame(ws)
frame2.pack(side=LEFT, expand=True, fill=BOTH)

frame3 = Frame(ws)
frame3.pack(side=LEFT, expand=True, fill=BOTH)

# style to add colors on separators
styl = ttk.Style()
styl.configure('red.TSeparator', background='red')
styl.configure('blue.TSeparator', background='blue')
styl.configure('yellow.TSeparator', background='yellow')

# # vertical separator with pack geometry manager
# ttk.Separator(
#     frame1,
#     orient=VERTICAL,
#     style="blue.TSeparator"
# ).pack(fill=Y, expand=True)

# vertical separator with grid geometry manager
ttk.Separator(
    frame2,
    orient=VERTICAL,
    style="red.TSeparator"
).grid(row=0, column=0, ipady=200)

# # vertical separator with place geometry manager
# ttk.Separator(
#     frame3,
#     orient=VERTICAL,
#     style="yellow.TSeparator"
# ).place(x=10, y=0, relheight=1)

# infinite loop
ws.mainloop()