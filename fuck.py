import cv2

def nothing():
    pass


vid = cv2.VideoCapture('example.avi')
# vid = cv2.VideoCapture(0)
# cv2.namedWindow('ct')
# cv2.createTrackbar('H1','ct',0,255,nothing)
# cv2.createTrackbar('S1','ct',0,255,nothing)
# cv2.createTrackbar('V1','ct',0,255,nothing)

while True:
    ret, img = vid.read()
    if ret:
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        first_range = cv2.inRange(img_hsv, (0,int(0.2*255),int(255/2)), (4,int(0.6*255),255))
        sex_range = cv2.inRange(img_hsv, (145,int(0.2*255),int(255/2)), (179,int(0.6*255),255))
        robdeaw = first_range+sex_range

        blured = cv2.medianBlur(robdeaw,9)

        im2, ct, hrc = cv2.findContours(blured,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        dalargest = None
        fuck_largest_size = 0
        loc_largest = [None for _ in range(4)]
        for pussy in ct:
            x,y,w,h = cv2.boundingRect(pussy)
            if w*h >fuck_largest_size:
                dalargest=pussy
                fuck_largest_size=w*h
                loc_largest = [x,y,w,h]
        if dalargest is not None:
            peri = cv2.arcLength(dalargest, True)
            approx = cv2.approxPolyDP(dalargest, 0.005 * peri, True)
            # cv2.rectangle(img,(x,y), (x+h, y+w), (0,0,255),4)
            print(img.shape)
            x_pos_ref = ((x+h/2)-(img.shape[1]/2))/img.shape[1]*2
            y_pos_ref = ((y+w/2)-(img.shape[0]/2))/img.shape[0]*2
            print((x_pos_ref,y_pos_ref,fuck_largest_size/img.shape[1]/img.shape[0]),len(approx))
            cv2.drawContours(img,[dalargest],0,(0,255,255),3)
        cv2.imshow('ct', img)
        cv2.waitKey(1)
