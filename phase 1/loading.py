import cv2

image  = cv2.imread("phase 1\image.webp")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")
    