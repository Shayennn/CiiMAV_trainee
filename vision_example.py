import cv2
import numpy as np
from vision_lib import * # import all function from vision_lib
# Colors Value (Red)
upper = np.array([179, 255, 255])
lower = np.array([141, 115, 110])

# CV Variables (initial)
area_res = -1
wh = (-1,-1)
xRes = 100
yRes = 100
w, h = wh

cv2.namedWindow('result') # create window named result
cap = cv2.VideoCapture(0) # 0 = Default, can also be path of files
# cap = cv2.VideoCapture('example.avi')

# Main
while True :
    ret, img = cap.read()
    if img is None : # if image is None make sure device is connected
        print('image is None')
        continue    
    r, c, ch = img.shape # row = vertical axis (px), column = horizon axis (px), channel(s)
    frame = img
    result = frame

    #Finding Contours (read FAQ)    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert BGR to HSV (read FAQ)
    mask = cv2.inRange(hsv, lower, upper) # create mask (binary image)
    kernel = get_kernel('rect', (5, 5)) # reduce noise (read FAQ)
    mask = cv2.dilate(mask, kernel)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(mask,127,255,0) 
    frame, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(frame, cnt, -1, (0,255,0), 1)
        rect = cv2.minAreaRect(cnt)
        center, wh, angle = cv2.minAreaRect(cnt)
        x, y = center
        w, h = wh
        area = cv2.contourArea(cnt)
    area_res = area/(r*c) # area_res (read FAQ)

    # Feature Conditions (read FAQ)
    '''
    if area_res < ..... and area_res > .....
        if (w/h) > ..... and (w/h) < ..... :
            xRes = 2*(x - int(c/2))/c
            yRes = 2*(y - int(r/2))/r
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            result = cv2.drawContours(result,[box],0,(0,0,255),2)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
    cv2.imshow('result', result)
    '''
    #Manual Break
    if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to break program
        break
cv2.destroyAllWindows()
cap.release()
