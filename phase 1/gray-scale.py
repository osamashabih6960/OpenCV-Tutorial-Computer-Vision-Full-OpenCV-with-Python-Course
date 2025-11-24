import cv2

image  = cv2.imread("phase 1\image.webp")

if image is  not None:
     gray = cv2.cvtColor(image, cv2.COLOR_BGB2GRAY)
     cv2.imshow("Grayscale Image", gray)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     
else:
    print("Could not load the image")
    
    
     