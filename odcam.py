#basic imports
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import tkinter as tk
from PIL import ImageTk, Image


class VideoPlayer:
	def __init__(self, parent_frame):
		self.parent_frame = parent_frame
		self.label = tk.Label(parent_frame)
		self.label.pack()

	def generate_video(self):

		'''ap = argparse.ArgumentParser()
		ap.add_argument("-p", "--prototxt", required=True,
			help="path to Caffe 'deploy' prototxt file")
		ap.add_argument("-m", "--model", required=True,
			help="path to Caffe pre-trained model")
		ap.add_argument("-c", "--confidence", type=float, default=0.2,
			help="minimum probability to filter weak detections")
		args = vars(ap.parse_args())'''

		#Classes that the model should detect
		CLASSES = ["" ,"", "bicycle", "bird", "",
			"", "bus", "car", "", "", "", "",
			"", "", "motorbike", "Person", "Tree", "",
			"", "building", ""]
		# Colours for drawing the rectangles
		COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
		# Just a basic command to say that we are loading the model
		print("loading model...")
		# Reading the Prebuilt model the absolute paths of MobileNetSSD_deploy.prototxt.txt and MobileNetSSD_deploy.caffemodel should be given
		net = cv2.dnn.readNetFromCaffe('C:\Ex_Python\TTL\MobileNetSSD_deploy.prototxt.txt','C:\Ex_Python\TTL\MobileNetSSD_deploy.caffemodel')
		# Basic command that says you are starting the web cam
		print("starting video stream...")
		# The below command is used to start the webcam
		vs = VideoStream(src=0).start()
		time.sleep(2.0)
		fps = FPS().start()


		while True:
		#Reading each frame
			frame = vs.read()
			# Resizing the frame
			frame = imutils.resize(frame, width=400)
			#Taking the height and width of the frame
			(h, w) = frame.shape[:2]
			#Blobing a 4 dimensional array from the frame
			blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
				0.007843, (300, 300), 127.5)


			net.setInput(blob)
			# We detect the objects using the webcam
			detections = net.forward()

			#iterating through the detection to draw rectangles
			for i in np.arange(0, detections.shape[2]):
				#finding the confidence in the detection
				confidence = detections[0, 0, i, 2]

				#if confidence>20 percent then we draw a rectangle tis is threshould and can be modified
				if confidence > 0.2:
					#we are taking the class label of the detection
					idx = int(detections[0, 0, i, 1])
					box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
					(startX, startY, endX, endY) = box.astype("int")
					#we are also labeling with the class name
					label = "{}".format(CLASSES[idx])
					if CLASSES[idx]!="":
						#Then we are drawing the boxes using Opencv
						cv2.rectangle(frame, (startX, startY), (endX, endY),
							COLORS[idx], 2)
						y = startY - 15 if startY - 15 > 15 else startY + 15
						cv2.putText(frame, label, (startX, y),
							cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

			#used to show the frame after drawing boxes
			# cv2.imshow("Frame", frame)
			frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			pil_image = Image.fromarray(frame_rgb)
			tk_image = ImageTk.PhotoImage(pil_image)
			self.label.config(image=tk_image)
			self.label.image = tk_image

			key = cv2.waitKey(1) & 0xFF

			#Press q to exit the webcam
			if key == ord("q"):
				break


			fps.update()

		#Details about how much time you used the webcam to capture frames 
		fps.stop()
		#Details about how much time you used the webcam to capture frames
		print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
		print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))


		cv2.destroyAllWindows()
		vs.stop()
	