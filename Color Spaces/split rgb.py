import cv2
import numpy as np

image = cv2.imread('Color Spaces\parrot.webp')

B,G,R = cv2.split(image)
cv2.imshow("Original image", image)
cv2.waitKey(0)

cv2.imshow("Original Blue",B)
cv2.waitKey(0)

cv2.imshow("Original Green",G)
cv2.waitKey(0)

cv2.imshow("Original Red",R)
cv2.waitKey(0)

cv2.destroyAllWindows()