import cv2

img = cv2.imread('lena.jpg' , 1)


cv2.line(img , (0,0), (255,255), (0,255,0), 5)
cv2.arrowedLine(img , (0,255), (255,255), (0,255,0), 5)

cv2.rectangle(img , (384,0) , (510,128) , (255,0,0) , 5)
cv2.circle(img , (447, 63), 63, (0,255,0) , 2)


cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()