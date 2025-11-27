import cv2
import numpy as np

# ---------- Load Image ----------
image = cv2.imread(r"Color Spaces\parrot.webp")

# Check if image loaded
if image is None:
    print("Image not found!")
    exit()

# Convert to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Red Color Range
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create Mask
mask = cv2.inRange(image_hsv, lower_red, upper_red)

# Apply mask
result = cv2.bitwise_and(image, image, mask=mask)

# Show output
cv2.imshow("Masked Result", result)

cv2.waitKey(0)          # ✔ Correct function
cv2.destroyAllWindows()

