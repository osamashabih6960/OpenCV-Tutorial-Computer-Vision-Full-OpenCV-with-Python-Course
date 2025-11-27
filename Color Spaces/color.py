import cv2

# ---------- Load Image ----------
image = cv2.imread(r"Color Spaces\parrot.webp")

# Check if image loaded
if image is None:
    print("Image not found!")
    exit()

# ---------- Color Conversions ----------
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# ---------- Display All ----------
cv2.imshow("Original BGR", image)
cv2.imshow("RGB Image", image_rgb)
cv2.imshow("HSV Image", image_hsv)
cv2.imshow("Gray Image", image_gray)
cv2.imshow("LAB Image", image_lab)

cv2.waitKey(0)      # Wait for key press
cv2.destroyAllWindows()
