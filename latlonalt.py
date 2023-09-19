import tkinter as tk
from tkinter import END

def latlongalt(name):
    global lon_entry, lat_entry, alt_entry
    # Create a frame for longitude, latitude, and altitude input boxes
    input_frame = tk.Frame(name, bg="#3D3D3D")
    input_frame.grid()

    # Longitude input box
    lon_label = tk.Label(input_frame, text="Longitude:", bg="#3D3D3D", fg="white")
    lon_label.grid(row=1, column=1, padx=10, pady=20)

    lon_entry = tk.Entry(input_frame)
    lon_entry.grid(row=1, column=3, padx=5, pady=5)

    # Latitude input box
    lat_label = tk.Label(input_frame, text="Latitude:", bg="#3D3D3D", fg="white")
    lat_label.grid(row=2, column=1, padx=10, pady=20)

    lat_entry = tk.Entry(input_frame)
    lat_entry.grid(row=2, column=3, padx=5, pady=5)

    # Altitude input box
    alt_label = tk.Label(input_frame, text="Altitude:", bg="#3D3D3D", fg="white")
    alt_label.grid(row=3, column=1, padx=10, pady=20)

    alt_entry = tk.Entry(input_frame)
    alt_entry.grid(row=3, column=3, padx=5, pady=10)

    return lon_entry, lat_entry, alt_entry

def submit_coordinates():
    # Get the values from the longitude, latitude, and altitude entry boxes
    longitude = lon_entry.get()
    latitude = lat_entry.get()
    altitude = alt_entry.get()

    # Perform the desired action with the submitted coordinates
    # For example, you can print them to the console
    print("Longitude:", longitude)
    print("Latitude:", latitude)
    print("Altitude:", altitude)

    # Clear the entry boxes after submitting the coordinates
    lon_entry.delete(0, END)
    lat_entry.delete(0, END)
    alt_entry.delete(0, END)