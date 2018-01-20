# -*- coding: utf-8 -*-
import numpy as np
import cv2
import glob
#import matplotlib


print("Initializing Cameras...")

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((5*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:5].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('cam2*.png')

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (8,5),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (8,5), corners,ret)
        cv2.imshow('img',img)
        cv2.waitKey(10)

        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        data = []
        #np.savez("/home/jason/CameraCalibration/Cam1/cam1_calibration_ouput", ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
        img = cv2.imread('cam2_5.png')
        h,  w = img.shape[:2]
        newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
        # undistort
        mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)

        dst = cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
        #np.save = ("/home/jason/CameraCalibration/Cam1/mapcam1", mapx, mapy, dst)



print ("Mtx:",mtx)
print ("Dist:",dist)




print ("Collections")

#data = np.load('/home/jason/CameraCalibration/Cam1/cam1_calibration_ouput.npz')

# crop the image
x,y,w,h = roi
dst = dst[y:y+h, x:x+w]
#cv2.imwrite('calibresult.png',dst)

cam = cv2.VideoCapture(1)
#cv2.namedWindow("cal")

while True:
    ret, frame = cam.read()
    #frame = frame[y:y+h, x:x+w]
    frame = cv2.remap(frame,mapx,mapy,cv2.INTER_LINEAR)
    #Crop Video Stream
    frame = frame[y:y+h, x:x+w]
    cv2.imshow("camm", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()