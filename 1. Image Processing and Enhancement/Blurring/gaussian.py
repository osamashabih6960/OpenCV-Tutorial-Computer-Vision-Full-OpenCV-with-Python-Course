import cv2
import matplotlib.pyplot as plt 

# Fixed correct image path
image_path = '1. Image Processing and Enhancement/dog-cats.webp'

# Read image
image = cv2.imread(image_path)
if image is None:
    print("Image not found! Check path.")
    exit()
    
#.resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
 
    
    

# Resize
resized_image = cv2.resize(image, (1900, 800))

# Apply Gaussian Blur
Gaussian = cv2.GaussianBlur(resized_image, (15, 15), 0)

# Convert to RGB
Gaussian_rgb = cv2.cvtColor(Gaussian, cv2.COLOR_BGR2RGB)

# Show Gaussian Blurred Image
plt.imshow(Gaussian_rgb)
plt.title('Gaussian Blurred Image')
plt.axis('off')
plt.show()
