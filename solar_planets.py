import cv2

img = cv2.imread("solar_system.jpg")

cv2.putText(img,  
           "Sun",
           (20, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (120, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (220, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (320, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (420, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Jupiter",
           (520, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Saturn",
           (620, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Uranus",
           (720, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.putText(img,  
           "Neptune",
           (820, 300),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           (255,255,255)
           )

cv2.imshow("output",img)

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.waitKey(0)