#Source python capture.py
#This streams and records two video sources as declared in Left and Right
# import the necessary packages
#W1 and W2=598, H1 and H2 =416
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
from matplotlib import pyplot as plt
from MT import *
import numpy as np
import imutils
import time
import cv2
# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling frames from cameras...")
Left = WebcamVideoStream(src=1).start()
Right = WebcamVideoStream(src=2).start()
#Left = cv2.VideoCapture(1)
#Right = cv2.VideoCapture(2)
time.sleep(2.0)
fps = FPS().start()
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('CamLeft5.avi',fourcc, 30, (h1,h1))
out2 = cv2.VideoWriter('CamRight5.avi',fourcc, 30, (h1,h1))
# loop over frames from the video file stream
while True:
	left = Left.read()
	right = Right.read()
	left = cv2.remap(left,mapx1,mapy1,cv2.INTER_LINEAR)
	right = cv2.remap(right,mapx2,mapy2,cv2.INTER_LINEAR)
	left = left[y1:y1+h1, y1:y1+h1]
	right = right[y1:y1+h1, y1:y1+h1]
	#left = cv2.rectangle(left, (x1,y1), (x1+w1, y1+h1), (0, 0, 0), 2)
	#right = cv2.rectangle(right, (x2,y2), (x2+w2, y2+h2), (0, 0, 0), 2)
	# write the frames
	out1.write(left)
	out2.write(right)
	# show the frames and update the FPS counter
	cv2.imshow("Left Camera", left)
	cv2.imshow("RIght Camera", right)
	cv2.waitKey(1)
	fps.update()
	key = cv2.waitKey(30) & 0xFF
	# if the `ESC` key was pressed, break from the loop
	if key%256 == 27:
		break
#cleanup
print("[INFO] cleaning up...")
Left.stop()
Right.stop()
cv2.destroyAllWindows()