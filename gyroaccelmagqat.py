import tkinter as tk

# Function to display the selected axes
def show_selected_axes():
    selected_axes = []
    if x_gyro_var.get():
        selected_axes.append("Gyro X-axis")
    if y_gyro_var.get():
        selected_axes.append("Gyro Y-axis")
    if z_gyro_var.get():
        selected_axes.append("Gyro Z-axis")
    if x_accl_var.get():
        selected_axes.append("Accelerometer X-axis")
    if y_accl_var.get():
        selected_axes.append("Accelerometer Y-axis")
    if z_accl_var.get():
        selected_axes.append("Accelerometer Z-axis")
    if x_mag_var.get():
        selected_axes.append("Magnetometer X-axis")
    if y_mag_var.get():
        selected_axes.append("Magnetometer Y-axis")
    if z_mag_var.get():
        selected_axes.append("Magnetometer Z-axis")
    if x_qat_var.get():
        selected_axes.append("Quarternions X-axis")
    if y_qat_var.get():
        selected_axes.append("Quarternions Y-axis")
    if z_qat_var.get():
        selected_axes.append("Quarternions Z-axis")
    print("Selected Axes:", selected_axes)

# root = tk.Tk()
# root.title("TechTech Labs Monitoring Application")

# Gyro Frame
def gyro(name):
    global x_gyro_var, y_gyro_var, z_gyro_var, x_gyro_checkbox, y_gyro_checkbox, z_gyro_checkbox
    # Create a frame for gyro section with blue background and padding
    gyro_frame = tk.Frame(name, bg="#706f6f", padx=10, pady=10)
    #gyro_frame.pack(side="left")
    #
    gyro_frame.grid(row=1, column=0)
    # Label for gyro section
    gyro_label = tk.Label(gyro_frame, text="GYRO:", bg="blue", fg="white", font=("Arial", 12, "bold"))
    gyro_label.pack()

    # Variables to store the state of gyro checkboxes
    x_gyro_var = tk.BooleanVar()
    y_gyro_var = tk.BooleanVar()
    z_gyro_var = tk.BooleanVar()

    # Checkboxes for gyro axes
    x_gyro_checkbox = tk.Checkbutton(gyro_frame, text="X-axis", variable=x_gyro_var)
    y_gyro_checkbox = tk.Checkbutton(gyro_frame, text="Y-axis", variable=y_gyro_var)
    z_gyro_checkbox = tk.Checkbutton(gyro_frame, text="Z-axis", variable=z_gyro_var)

    x_gyro_checkbox.pack()
    y_gyro_checkbox.pack()
    z_gyro_checkbox.pack()

# Accelerometer Frame
def acc(name):
    global x_accl_var, y_accl_var, z_accl_var,x_accl_checkbox,y_accl_checkbox,z_accl_checkbox
    # Create a frame for accelerometer section with navy blue background and padding
    accl_frame = tk.Frame(name, bg="#706f6f", padx=10, pady=10)
    #accl_frame.pack(side="right")
    accl_frame.grid(row=1, column=1)

    # Label for accelerometer section
    accl_label = tk.Label(accl_frame, text="ACCL:", bg="navy blue", fg="white", font=("Arial", 12, "bold"))
    accl_label.pack()

    # Variables to store the state of accelerometer checkboxes
    x_accl_var = tk.BooleanVar()
    y_accl_var = tk.BooleanVar()
    z_accl_var = tk.BooleanVar()

    # Checkboxes for accelerometer axes
    x_accl_checkbox = tk.Checkbutton(accl_frame, text="X-axis", variable=x_accl_var)
    y_accl_checkbox = tk.Checkbutton(accl_frame, text="Y-axis", variable=y_accl_var)
    z_accl_checkbox = tk.Checkbutton(accl_frame, text="Z-axis", variable=z_accl_var)

    x_accl_checkbox.pack()
    y_accl_checkbox.pack()
    z_accl_checkbox.pack()

# Magnetometer frame
def mag(name):
    global x_mag_var, y_mag_var, z_mag_var
    # Create a frame for mag section with breen background and padding
    mag_frame = tk.Frame(name, bg="#706f6f", padx=10, pady=25)
    #mag_frame.pack(side="left")
    mag_frame.grid(row=2, column=0)
    # Label for mag section
    mag_label = tk.Label(mag_frame, text="MAG:", bg="green", fg="white", font=("Arial", 12, "bold"))
    mag_label.pack()

    # Variables to store the state of mag checkboxes
    x_mag_var = tk.BooleanVar()
    y_mag_var = tk.BooleanVar()
    z_mag_var = tk.BooleanVar()

    # Checkboxes for mag axes
    x_mag_checkbox = tk.Checkbutton(mag_frame, text="X-axis", variable=x_mag_var)
    y_mag_checkbox = tk.Checkbutton(mag_frame, text="Y-axis", variable=y_mag_var)
    z_mag_checkbox = tk.Checkbutton(mag_frame, text="Z-axis", variable=z_mag_var)

    x_mag_checkbox.pack()
    y_mag_checkbox.pack()
    z_mag_checkbox.pack()

# Qarternions frame
def qat(name):
    global x_qat_var, y_qat_var, z_qat_var
    # Create a frame for qat section with blue background and padding
    qat_frame = tk.Frame(name, bg="#706f6f", padx=10, pady=25)
    #qat_frame.pack(side="right")
    qat_frame.grid(row=2, column=1)
    # Label for qat section
    qat_label = tk.Label(qat_frame, text="QAT:", bg="orange", fg="white", font=("Arial", 12, "bold"))
    qat_label.pack()

    # Variables to store the state of qat checkboxes
    x_qat_var = tk.BooleanVar()
    y_qat_var = tk.BooleanVar()
    z_qat_var = tk.BooleanVar()

    # Checkboxes for qat axes
    x_qat_checkbox = tk.Checkbutton(qat_frame, text="X-axis", variable=x_qat_var)
    y_qat_checkbox = tk.Checkbutton(qat_frame, text="Y-axis", variable=y_qat_var)
    z_qat_checkbox = tk.Checkbutton(qat_frame, text="Z-axis", variable=z_qat_var)

    x_qat_checkbox.pack()
    y_qat_checkbox.pack()
    z_qat_checkbox.pack()
# Calling the gyro and acc functions
# gyro(root)
# acc(root)

# root.mainloop()