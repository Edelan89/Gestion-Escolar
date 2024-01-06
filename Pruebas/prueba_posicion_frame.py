import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Frames Side by Side")

# Create the first frame
frame1 = tk.Frame(root, width=200, height=200, bg="red")
frame1.pack(side="left", padx=10)  # Place it on the left side

# Create the second frame
frame2 = tk.Frame(root, width=200, height=200, bg="blue")
frame2.pack(side="left", padx=10)  # Place it on the left side

root.mainloop()
