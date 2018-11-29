import cv2
import numpy as np
# Reading the input image and convert it into the grayscale
img=cv2.imread("95.png",cv2.IMREAD_GRAYSCALE)
#Image denoising using Non-local Means Denoising algorithm 
img = cv2.fastNlMeansDenoising(img, None, 9, 13)
#Morphological operations to an image
#Kernel is created and convolved with the input image
kernel = np.ones((5,5), np.uint8) 
# The first parameter is the original image, 
# kernel is the matrix with which image is  
# convolved and third parameter is the number  
# of iterations, which will determine how much  
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1) 
img = cv2.dilate(img_erosion, kernel, iterations=1)
#Image blurring is achieved by convolving the image with a low-pass filter kernel. 
#It is useful for removing noises.
img = cv2.GaussianBlur(img, (5, 5), 0)
#threshold is created for the given image.all pixel value above 150 would be white.
ret, threshold=cv2.threshold( img, 150, 255, cv2.THRESH_BINARY)
#To detct the shape a contour is created around the threshold image
cp, contours, heir=cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
font=cv2.FONT_HERSHEY_COMPLEX
#for each contour
for cnt in contours:
    #the contour is approximated arround the image and then closed contour is formed 
    #across the boundary of the image.
    approx=cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [cnt], 0 , (0), 5)
    #determining the number of approximate sides around the given contour
    print(len(approx))
    #detemining the coordintes to put the text around the image 
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    # by calculating  the number of sides from the we approximated that the given figure 
    #would be either circle, ellipse and unidentified
    if 12<=len(approx) <=14:
        cv2.putText(img, "Circle", (x,y), font, 1, (0))
    elif 8 < len(approx) <=11:
        cv2.putText(img, "Ellipse", (x,y), font, 1, (0))
    elif len(approx)==3:
        cv2.putText(img, "Triangle", (x,y), font, 1, (0))
    elif  len(approx)==4:
        cv2.putText(img, "Square", (x,y), font, 1, (0))
    else:
        cv2.putText(img, "Unidentified", (x,y), font, 1, (0))
#the number of sides are approximated from the len(approx) function

#Show the final Output Image
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
