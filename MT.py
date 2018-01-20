
import numpy as np
import cv2
         #Camera-1 Fix (Left)
mtx1 = [[563.36055746, 0, 311.06506052, 0,  562.85882975, 241.36068413,0, 0, 1]]
mtx1 = np.array(mtx1)
mtx1 = mtx1[0].reshape((3, 3))
dist1 = [[-0.4135498,   0.14687675,  0.00078966,  0.00166469,  0.06403798]]
dist1 = np.array(dist1)
        #Camera-2 Fix (Right)
#mtx2 = [[558.5044801, 0, 341.53353114, 0,  557.61804248, 209.74221674,0, 0, 1]]
#mtx2 = np.array(mtx2)
#mtx2 = mtx2[0].reshape((3, 3))
mtx2 = mtx1
#dist2 = [[-0.397139056,   0.117252300,  -0.0000345481288,  0.00115310976,  -0.00225083484]]
#dist2 = np.array(dist2)
dist2 = dist1

#=====================Camera1-Solving==============
img1 = cv2.imread('opencv_frame_5.png')
h1,  w1 = img1.shape[:2]
newcamera1mtx, roi1=cv2.getOptimalNewCameraMatrix(mtx1,dist1,(w1,h1),1,(w1,h1))
#====================Camera1 Undistortion==============
mapx1,mapy1 = cv2.initUndistortRectifyMap(mtx1,dist1,None,newcamera1mtx,(w1,h1),5)
#===================Camera2-Solving===================
img2 = cv2.imread('cam2_5.png')
h2,  w2 = img2.shape[:2]
newcamera2mtx, roi2=cv2.getOptimalNewCameraMatrix(mtx2,dist2,(w2,h2),1,(w2,h2))
#======================Camera2 Undistortion=====================
mapx2,mapy2 = cv2.initUndistortRectifyMap(mtx2,dist2,None,newcamera2mtx,(w2,h2),5)
# ====================Video Perameters================
#Camera 1 Region of Interest
x1,y1,w1,h1 = roi1
#Camera 2 Region of Interest
x2,y2,w2,h2 = roi2