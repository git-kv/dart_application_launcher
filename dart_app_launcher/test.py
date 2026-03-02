from tkinter import *
from PIL import Image
import customtkinter
import os

root = customtkinter.CTk()

root.title('Dart Application Window')
root.geometry('500x500')

my_frame = customtkinter.CTkScrollableFrame(root)
my_frame.pack(fill="both", expand=1)

for x in range(5):
    img_path = './assets/penguin_48.png'
    icon = customtkinter.CTkImage(Image.open(img_path), size=(48, 48))
    my_button = customtkinter.CTkButton(
        my_frame,
        image=icon,
        text='D4K',
        compound='left',
        anchor='nw',
        font=('calibre', -24)
    )

    my_button.pack(
        anchor='nw',
        fill="x",
        pady=10,
        padx=30
    )

d4k_path = 'd4k2001.exe'
d4k_avail = os.path.exists(d4k_path)

if (d4k_avail):
    img_path = './assets/penguin_48.png'
    icon = customtkinter.CTkImage(Image.open(img_path), size=(48, 48))
    my_button = customtkinter.CTkButton(
        my_frame,
        image=icon,
        text='D4K Valid',
        compound='left',
        anchor='nw',
        font=('calibre', -24)
    )

    my_button.pack(
        anchor='nw',
        fill="x",
        pady=10,
        padx=30
    )

root.mainloop()
