#Source This is mostly from PyImageSearch.com
# python capture.py
# import the necessary packages
from __future__ import print_function
from imutils.video import WebcamVideoStream
from imutils.video import FPS
#import numpy as np
#import argparse
#import imutils
import time
import cv2

# created a *threaded* video stream, allow the camera sensor to warmup,
# and start the FPS counter
print("[INFO] sampling THREADED frames from webcam...")
vs1 = WebcamVideoStream(src=0).start()
vs2 = WebcamVideoStream(src=1).start()
time.sleep(2.0)

fps = FPS().start()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out1 = cv2.VideoWriter('frame1.avi',fourcc, 30, (640,480))
out2 = cv2.VideoWriter('frame2.avi',fourcc, 30, (640,480))

# loop over frames from the video file stream
while True:
	frame1 = vs1.read()
	frame2 = vs2.read()
	
	# write the frame
	out1.write(frame1)
	out2.write(frame2)
	# show the frame and update the FPS counter
	cv2.imshow("Frame1", frame1)
	cv2.imshow("Frame2", frame2)
	cv2.waitKey(1)
	fps.update()
	key = cv2.waitKey(30) & 0xFF
	
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
		
# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs1.stop()
vs2.stop()