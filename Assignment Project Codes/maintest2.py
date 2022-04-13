'''

Write a python program using the library opencv,numpy and matplotlib to show the output of number of license plate detected and also the output using
Haar Cascade (Link to file given below)
'''















import cv2
import numpy as np
import matplotlib.pyplot as plt

cascade=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cars=cv2.imread('car_1.jpeg')
gray=cv2.cvtColor(cars,cv2.COLOR_BGR2GRAY)

def convertRGB(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cars_detected=cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(20,20)
)
print('Found_NUmber_Plate',len(cars_detected))

for (x,y,w,h) in cars_detected:
    cv2.rectangle(cars,(x,y),(x+w,y+h),(145,60,255),5)

plt.imshow(convertRGB(cars))
plt.imsave('Detected_Cars.png',convertRGB(cars))
plt.waitforbuttonpress()