
import os
if (os.name) != "nt":
    print("Not using Windows")
    !sudo apt install tesseract-ocr

!pip install numpy==1.19.5
!pip install pytesseract==0.3.7

import cv2
import pytesseract

img = cv2.imread("/content/Screenshot (130).png")

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))