# Camera-Calibrate-Capture

Requirements
  Python 3.5
  OpenCV 3.3.0
  Numpy 1.13.3
  matplatlib 2.1.1
  imutils 0.4.5
  Ubuntu 16.04
## Display and Record video from USB Cameras
First we need to setup OpenCV to read and show and record the Video Stream/s from the camera/s.The way it is written it saves the video to the same location as the "Capture.py"

This was done using 
**Capture.py.**

## Calibrate
For this there were a few differetn methods that I tested. However, prior to any calibrating we must first print off the checkerd board pattern. I also relied heavily on https://docs.opencv.org/3.3.1/dc/dbb/tutorial_py_calibration.html for help. 

   **Method "A"**
   Method "A" was the easiest, however I did not find it to be as accurate. This lets you automatically capture the patteren and when it senses enough captures of the patterns it then attempts to create the calibration correction data.
   
This was done using **calibrateA.py**  

  **Method "B"**
    Method "B" was the method for the best accuracy, it took a little longer, however it forces a better statistically solution. I first capture 60 images of the checker board from 60 different locations using **captureB.py**
    After images are collected **calibrateB.py** should be used to read and create the calibration correction data. Note with this many images it took around 4-5 minutes. This prints the correction data that needs to be placed into **MT.py** file.
    
 ## Capturing Dual Calibrated Video
 Used **MT.py** as a reference file and **CalCapture.py** as the call program. Note my overall project required the video to be square, so I clipped some of the frame off the sides in this file as well.  
