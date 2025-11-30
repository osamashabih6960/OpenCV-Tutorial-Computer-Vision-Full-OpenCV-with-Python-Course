import cv2
import matplotlib.pyplot as plt 

# Fixed correct image path
image_path = '1. Image Processing and Enhancement/dog-cats.webp'

# Read image
image = cv2.imread(image_path)
if image is None:
    print("Image not found! Check path.")
    exit()

# Resize
resized_image = cv2.resize(image, (1900, 800))

# Apply Gaussian Blur
median = cv2.medianBlur(resized_image, 11)

# Convert to RGB
median_rgb = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)

# Show Gaussian Blurred Image
plt.imshow(median_rgb)
plt.title('Median Blurred Image')
plt.axis('off')
plt.show()
