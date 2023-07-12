import cv2
import numpy as np
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) 
enhanced_image = clahe.apply(image)
cv2.imshow('Original', image) 
cv2.imshow('Enhanced', enhanced_image)
_, threshold_image = cv2.threshold(enhanced_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('Thresholded', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()