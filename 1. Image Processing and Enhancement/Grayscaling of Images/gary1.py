import cv2

# Correct cv2 usage
#.Using the cv2.imread() function with flag=zero
image = cv2.imread('1. Image Processing and Enhancement/Grayscaling of Images/Tomatoes.png',0)

# Check if image loaded
if image is None:
    print("Image not found! Check path.")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
