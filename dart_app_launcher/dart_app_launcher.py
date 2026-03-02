from tkinter import ttk
import customtkinter
import tkinter as tk

root = tk.Tk()

root.title('Dart Applications Window')
root.geometry('500x500')

icon = tk.PhotoImage(file='./assets/penguin_48.png')
test_button = ttk.Button(
        root,
        image=icon,
        text='test text',
        compound='left',
        width=100
)

test_button.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor='nw',
        expand=True
)

test_button2 = ttk.Button(
        root,
        image=icon,
        text='test text',
        compound='left',
        width=100
)

test_button2.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor='nw',
        expand=True
)

root.mainloop()
