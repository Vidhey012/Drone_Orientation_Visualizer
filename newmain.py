from tkinter import *
# importing the python tkinter library for GUI
from gyroaccelmagqat import *
from odcam import *
import threading



from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd




from latlonalt import *
# importing gyroaccel.py file as "gyro" and "accl" section code is written in it
root=Tk()
# creating a window using tkinter library with title and initial startup dimensions
root.title("TronTech Labs Drone Flight Control Monitoring System")
root.geometry("1400x700")
# logo at img1.png
phologo = PhotoImage(file='img1.png')
root.iconphoto(False, phologo)

# setting up the label of the application
l1 = Label(root, text="TechTech Labs Monitoring Application")

# first vertical rectangle lighter grey
fra1 = Frame(root, bg="#222222", highlightbackground="#222222", highlightthickness=2)

# text on the right rectangle
lafra1 = Label(fra1, bg="#222222", fg="white", text="TronTech Labs Drone Flight Control System", font=("Arial", 15))

# second rectangle to the right darker grey

fra2 = Frame(root, bg="#3D3D3D", highlightbackground="#3D3D3D", highlightthickness=2)

fra3=Frame(fra2,bg="#3D3D3D")
fra4=Frame(fra2,bg="#3D3D3D")
# green Take Off and red KILL buttons
but2fra2=Button(fra2,text="Take Off", fg="white", bg="green",font=("Arial",10),width=20,height=2, command=submit_coordinates )
butfra2=Button(fra2,text="KILL", fg="white", bg="red",font=("Arial",10),width=20,height=2 )

# inserting logo in the left rectangle
laicfra2=Label(fra2,image=phologo,border=0)

# calling the gyroscope, accelerometer and magnetometer functions from the gyroaccel.py file
gyro(fra2)
acc(fra2)
mag(fra2)
qat(fra2)
lon_entry, lat_entry, alt_entry = latlongalt(fra2)
fra1.place(relx=0.24,rely=0 ,relheight=1,relwidth=0.76)
fra2.place(relx=0,rely=0,relheight=1,relwidth=0.24)

lafra1.pack(padx=100,pady=15,)

fra3.grid()


l1.place(relx=0.4 ,rely=0.4,relheight=0.2,relwidth=0.2)

laicfra2.grid(row=0, column=0, columnspan=2, padx=10)
but2fra2.grid(row=10, column=0, columnspan=2,padx=40, pady=10)
butfra2.grid(row=12, column=0, columnspan=2,padx=40, pady=0)

fr1= LabelFrame(root,text=" Accelerometer ", foreground = "white", background = "#222222", height="300", width="450")
fr2= LabelFrame(root,text=" Gyroscope ", foreground = "white", background = "#222222", height="300", width="450")
fr3= LabelFrame(root,text=" Camera ", foreground = "white", background = "#222222", height="300", width="450")
fr4= LabelFrame(root,text=" Orientation ", foreground = "white", background = "#222222", height="300", width="450")

fr1.grid(padx=(400,10),pady=(60,10), row=0, column=0)
fr2.grid(padx=(400,10),pady=(0,0), row=1, column=0)
fr3.grid(padx=(0,0),pady=(60,10), row=0, column=1)
fr4.grid(padx=(0,0),pady=(0,0), row=1, column=1)
fr1.pack_propagate(0) 
fr2.pack_propagate(0) 
fr3.pack_propagate(0) 
fr4.pack_propagate(0) 
# Camera section code
# label =Label(fr3, height="280", width="450")
# label.grid(row=0, column=0)
# cap= cv2.VideoCapture(0)

# Define function to show frame
def show_camera():
    video_player = VideoPlayer(fr3)
    video_thread = threading.Thread(target=video_player.generate_video)
    video_thread.start()
#    # Get the latest frame and convert into Image
#    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage 
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(20, show_camera)



# Graph 1
def graph1():
    empty_frame(fr1)
    from gyroaccelmagqat import x_accl_var,y_accl_var,z_accl_var
    df=pd.read_csv("accl_matrices.csv", header=None, names=['X', 'Y', 'Z'])
    figure1 = plt.Figure(figsize=(4.5,2.8), dpi=100)
    ax1 = figure1.add_subplot(111)
    if x_accl_var.get() == 1:
        y_values1 = df.iloc[:, 0].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='x-axis')
    if y_accl_var.get() == 1:
        y_values1 = df.iloc[:, 1].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='y-axis')
    if z_accl_var.get() == 1:
        y_values1 = df.iloc[:, 2].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='z-axis')
    ax1.legend()
    canvas = FigureCanvasTkAgg(figure1, master=fr1)
    canvas.draw()
    canvas.get_tk_widget().pack()
    fr1.after(5000, graph1)



# Graph 2
def graph2():
    empty_frame(fr2)
    from gyroaccelmagqat import x_gyro_var,y_gyro_var,z_gyro_var
    df=pd.read_csv("gyro_matrices.csv", header=None, names=['X', 'Y', 'Z'])
    figure1 = plt.Figure(figsize=(4.5,2.8), dpi=100)
    ax1 = figure1.add_subplot(111)
    if x_gyro_var.get() == 1:
        y_values1 = df.iloc[:, 0].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='x-axis')
    if y_gyro_var.get() == 1:
        y_values1 = df.iloc[:, 1].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='y-axis')
    if z_gyro_var.get() == 1:
        y_values1 = df.iloc[:, 2].values[-10:]
        x_values1 = list(range(1, len(y_values1)+1))
        ax1.plot(x_values1, y_values1, marker='o',label ='z-axis')
    ax1.legend()
    canvas = FigureCanvasTkAgg(figure1, master=fr2)
    canvas.draw()
    canvas.get_tk_widget().pack()
    fr2.after(5000, graph2)

#Clears the contents of the frame
def empty_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

from gyroaccelmagqat import x_gyro_checkbox,y_gyro_checkbox,z_gyro_checkbox, x_accl_checkbox,y_accl_checkbox,z_accl_checkbox
x_gyro_checkbox.config(command=graph2)
y_gyro_checkbox.config(command=graph2)
z_gyro_checkbox.config(command=graph2)
x_accl_checkbox.config(command=graph1)
y_accl_checkbox.config(command=graph1)
z_accl_checkbox.config(command=graph1)
graph1()
graph2()
show_camera()
# start the tkinter event loop
root.mainloop() 