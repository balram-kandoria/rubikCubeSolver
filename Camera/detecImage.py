import os
import cv2
from PIL import Image
import natsort
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import KDTree
from webcolors import (
    CSS3_HEX_TO_NAMES,
    hex_to_rgb,
)
import imageio as iio
 
srcLoc = "~/Desktop/Rubik/rubikCubeSolver/Main/"

image = cv2.imread("/home/pi1/Desktop/Rubik/rubikCubeSolver/Camera/Images/output0.png")
# read an image 

# print(image)
# Coordinates = [
#     [150, 150], # Top most Corner
#     [200, 210], # Right most Corner
#     [100, 275] # Bottom most Corner
# ]
# Real_Colors = ['Orange', 'Yellow', 'Blue']
Coordinates = [[100, 190]]
Real_Colors = ['Orange']
for i in range(50):
    for j in range(50):
        Coordinates.append([Coordinates[0][0]+i, Coordinates[0][1]+j])
        Real_Colors.append('Orange')



# for i in range(len(Coordinates)):
#     cv2.circle(image,(Coordinates[i][0],Coordinates[i][1]), 10, (255,0,0), 3)

# image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imwrite("../Camera/image.png",image)



def determineColor(center_pixel_hue, center_pixel_saturation):
    if center_pixel_saturation < 15:
        return("White")
    elif center_pixel_hue < 5:
        return("Red")
    elif center_pixel_hue < 41:
        return('Orange')
    elif center_pixel_hue < 75:
        return('Yellow')
    elif center_pixel_hue < 157:
        return('Green')
    elif center_pixel_hue < 265:
        return('Blue')
    else:
        return('Red')

def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value
    delta = 20
    # Handle red hue wrap-around
    if hue >= 165:  # Upper limit for divided red hue
        lowerLimit = np.array([hue - delta, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + delta, 255, 255], dtype=np.uint8)
    else:
        lowerLimit = np.array([hue - delta, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + delta, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit

# Convert BGR to HSV
# hue_vals = []

# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# cv2.imwrite("../Camera/HSVConvertedImage.png",hsv)
# for i in range(len(Coordinates)):
#     pixel_center = hsv[Coordinates[i][0], Coordinates[i][1]]
#     print(image[Coordinates[i][0], Coordinates[i][1]])
#     center_pixel_hue = pixel_center[0]

#     normal_Image_Center = img[Coordinates[i][0], Coordinates[i][1]]
#     hue_vals.append(normal_Image_Center)

#     center_pixel_saturation = pixel_center[1]

#     detectedColor = determineColor(center_pixel_hue, center_pixel_saturation)
    
#     if Real_Colors[i] != detectedColor:
#         print(f"Colors did not match. Got {detectedColor} instead of {Real_Colors[i]}")
        
#     else:
#         print(f"Color matched: {detectedColor}")

# plt.plot(hue_vals, '*')
# plt.savefig('../Camera/HueValues.png')
# breakpoint()


hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite("../Camera/HSVImage.png",hsvImage)
yellow = [255,0,0]
lowerLimit, upperLimit = get_limits(color=yellow)

mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
res = cv2.bitwise_and(image,image, mask=mask)
cv2.imwrite("../Camera/MaskedImage.png",res)

'''Edge Detection'''
img = image

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# edges = cv2.Canny(img_blur,0,45)
# cv2.imwrite('edges1.png', edges)

# Sobel Edge Detection
# sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
# sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
# sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
# cv2.imwrite('Sobel_X', sobelx)

# cv2.imwrite('Sobel Y', sobely)

# cv2.imwrite('Sobel X Y using Sobel() function', sobelxy)

 
# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=0, threshold2=45) # Canny Edge Detection
# Display Canny Edge Detection Image
cv2.imwrite(srcLoc+'Canny_Edge_Detection.png', edges)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

CounteredImage = cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite(srcLoc+'Countoured_Image.png', CounteredImage)