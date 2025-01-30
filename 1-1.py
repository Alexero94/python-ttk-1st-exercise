import tkinter as tk
from tkinter import ttk

# create the main window
root = tk.Tk()
root.title("hi bitch")

# create a Label and button using ttk 
Label = ttk.Label(root, text="hello bitch")
Label.grid(row=50, column=50, padx=0, pady=0)

button = ttk.Button(root, text="click me")
button.grid(row=5, column=50, padx=10, pady=10)

# run the window event loop
root.mainloop()