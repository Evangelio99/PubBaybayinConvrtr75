# from baybayintest import *
import cv2

image = cv2.imread("C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
dilate = cv2.dilate(thresh, kernal, iterations=1)

contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

cv2.imshow('image', dilate)
cv2.waitKey()

# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     if area > 10:
#         x,y,w,h = cv2.boundingRect(cnt)
#         crop_img = image[y:y+h, x:x+w]
#         cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
#         cv2.putText(image, predict(crop_img), (x,y+h + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)
#         # plt.imshow(crop_img)
#         # plt.show()


# cv2.imshow('image', image)
# cv2.waitKey()
