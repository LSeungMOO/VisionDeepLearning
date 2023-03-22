import cv2 as cv

def mouse_callback(event, x, y, flags, param):
    global refPt, cropping, img
    
    if event == cv.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        
        cv.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv.imshow("Original", img)
        
        patch = img[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0], :]
        patch1 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
        patch2 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
        patch3 = cv.resize(patch, dsize=(0,0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)
        
        cv.imshow('Resize nearest', patch1) 
        cv.imshow('Resize bilinear', patch2) 
        cv.imshow('Resize bicubic', patch3) 
        

img = cv.imread('C:/Users/WIN/Downloads/media/rose.png')
refPt = []
cropping = False

cv.namedWindow("Original")
cv.setMouseCallback("Original", mouse_callback)

while True:
    cv.imshow("Original", img)
    key = cv.waitKey(1) & 0xFF
    
    if key == ord("c"):
        break

cv.destroyAllWindows()