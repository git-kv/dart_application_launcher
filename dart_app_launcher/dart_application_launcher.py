from tkinter import *
from PIL import Image
import customtkinter
import os
import subprocess

# Create main window
root = customtkinter.CTk()

root.title('Dart Applications')
root.iconbitmap("C:\\Program Files\\Dart Applications\\Dart Application Launcher\\assets\\dart_apps_icon.ico")
root.geometry('375x500')

# Create scrollable window
my_frame = customtkinter.CTkScrollableFrame(root)
my_frame.pack(fill="both", expand=1)

# Declare installer file paths and check to see if app is not being masked by FSLogix
d4k_primary_installer_path = "C:\\Program Files\\Dart Applications\\d4k_primary_installer.exe"
d4k_primary_avail = os.path.exists(d4k_primary_installer_path)

d4hub_primary_installer_path = "C:\\Program Files\\Dart Applications\\d4hub_primary_installer.exe"
d4hub_primary_avail = os.path.exists(d4hub_primary_installer_path)

d4ap_primary_installer_path = "C:\\Program Files\\Dart Applications\\d4ap_primary_installer.exe"
d4ap_primary_avail = os.path.exists(d4ap_primary_installer_path)

def launch_d4k_primary():
    subprocess.run([d4k_primary_installer_path])

def launch_d4hub_primary():
    subprocess.run([d4hub_primary_installer_path])

def launch_d4ap_primary():
    subprocess.run([d4ap_primary_installer_path])

# Create icon for D4K Primary if available
if (d4k_primary_avail):
    img_path = 'C:\\Program Files\\Dart Applications\\Dart Application Launcher\\assets\\penguin_48.png'
    icon = customtkinter.CTkImage(Image.open(img_path), size=(48, 48))
    my_button = customtkinter.CTkButton(
        my_frame,
        image=icon,
        text='D4K Primary',
        compound='left',
        anchor='nw',
        font=('calibre', -24),
        command=launch_d4k_primary
    )

    my_button.pack(
        anchor='nw',
        fill="x",
        pady=10,
        padx=30
    )

# Create icon for D4Hub Primary if available
if (d4hub_primary_avail):
    img_path = 'C:\\Program Files\\Dart Applications\\Dart Application Launcher\\assets\\d4hub_icon.png'
    icon = customtkinter.CTkImage(Image.open(img_path), size=(48, 48))
    my_button = customtkinter.CTkButton(
        my_frame,
        image=icon,
        text='D4Hub Primary',
        compound='left',
        anchor='nw',
        font=('calibre', -24),
        command=launch_d4hub_primary
    )

    my_button.pack(
        anchor='nw',
        fill="x",
        pady=10,
        padx=30
    )

if (d4ap_primary_avail):
    img_path = 'C:\\Program Files\\Dart Applications\\Dart Application Launcher\\assets\\d4ap_icon.png'
    icon = customtkinter.CTkImage(Image.open(img_path), size=(48, 48))
    my_button = customtkinter.CTkButton(
        my_frame,
        image=icon,
        text='D4AP Primary',
        compound='left',
        anchor='nw',
        font=('calibre', -24),
        command=launch_d4ap_primary
    )

    my_button.pack(
        anchor='nw',
        fill="x",
        pady=10,
        padx=30
    )

root.mainloop()