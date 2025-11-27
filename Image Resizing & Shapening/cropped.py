import cv2 

image = cv2.imshow("OpenCV-Tutorial-Computer-Vision-Full-OpenCV-with-Python-Course\Image Resizing & Shapening\Airplane.img")

if image is None:
    cropped = image[100:200, 50:150]
    
    cv2.imshow("cropped", cropped)
    cv2.imshow("Original", image)
    cv2.waitkey(0)
    cv2.destroyAllWindows()
    
    
    
    