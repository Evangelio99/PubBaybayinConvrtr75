# from PIL import Image
# import pytesseract
# import matplotlib.pyplot as plt

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# img = Image.open("C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin.jpg")

# text = pytesseract.image_to_boxes(img).split("\n")

# for i in text:
#     if i:
#         (left, upper, right, lower) = list(map(int, i.split(" ")[1:-1]))
#         im_crop = img.crop((left, upper, right, lower))
#         plt.imshow(im_crop)
#         plt.show()

# import pytesseract
# import cv2
# from pytesseract import Output

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# img = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin2.jpg')

# height = img.shape[0]
# width = img.shape[1]

# d = pytesseract.image_to_boxes(img, output_type=Output.DICT)
# n_boxes = len(d['char'])

# for i in range(n_boxes):
#     (text,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
#     cv2.rectangle(img, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)
# cv2.imshow('img',img)
# cv2.waitKey(0)




# import cv2
# import numpy as np
# import pytesseract
# from pytesseract import Output
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# # img = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\imagetext02.jpg')
# img = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin2.jpg')
# image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# height = image.shape[0]
# width = image.shape[1]

# d = pytesseract.image_to_boxes(image, output_type=Output.DICT)
# n_boxes = len(d['char'])

# for i in range(n_boxes):
#     (text,x1,y2,x2,y1) = (d['char'][i],d['left'][i],d['top'][i],d['right'][i],d['bottom'][i])
#     cv2.rectangle(image, (x1,height-y1), (x2,height-y2) , (0,255,0), 2)

# cv2.imshow('img',image)
# cv2.waitKey(0)



# img = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\imagetext02.jpg')
# img = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin.jpg')
# image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# print("no of shape {0}".format(len(contours)))

# for cnt in contours:
#     rect = cv2.minAreaRect(cnt)
#     box = cv2.boxPoints(rect)
#     box = np.int0(box)
#     img = cv2.drawContours(img, [box], 0, (0,255,0), 3)

# plt.figure("Example 1")
# plt.imshow(image)
# plt.title('Binary Contours in an image')
# plt.show()


# import cv2
# from imutils import contours
# from PIL import Image
# import pytesseract
# import matplotlib.pyplot as plt

# # Load image, grayscale, Otsu's threshold
# image = cv2.imread('C:\\Users\\Evangelio\\Desktop\\test_img\\test2.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

# # Find contours, sort from left-to-right, then crop
# cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# cnts, _ = contours.sort_contours(cnts, method="left-to-right")

# ROI_number = 0
# for c in cnts:
#     area = cv2.contourArea(c)
#     if area > 10:
#         x,y,w,h = cv2.boundingRect(c)
#         ROI = 255 - image[y:y+h, x:x+w]
#         cv2.imwrite('ROI_{}.png'.format(ROI_number), ROI)
#         cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
#         ROI_number += 1

# cv2.imshow('thresh', thresh)
# cv2.imshow('image', image)
# cv2.waitKey()



# import cv2

# image = cv2.imread("C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin2.jpg")
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
# _,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# dilated = cv2.dilate(thresh,kernel,iterations = 0) 
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

# i=5
# for contour in contours:

#     [x,y,w,h] = cv2.boundingRect(contour)

#     cv2.imwrite(str(i)+".jpg",image[y:y+h,x:x+w])
#     i=i+1



#working!!
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# image = cv2.imread("C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin2.jpg")
# gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
# _,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
# kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
# dilated = cv2.dilate(thresh,kernel,iterations = 0) 
# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 


# print("no of shape {0}".format(len(contours)))

# i=1
# for cnt in contours:
#     area = cv2.contourArea(cnt)
#     if area > 10:
#         x,y,w,h = cv2.boundingRect(cnt)
#         # ROI = 255 - image[y:y+h, x:x+w]
#         # cv2.imwrite(str(i)+".jpg",image[y:y+h,x:x+w])
#         crop_img = image[y:y+h, x:x+w]
#         cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
#         plt.imshow(crop_img)
#         plt.show()


# # cv2.imshow('image', image)
# # cv2.waitKey()

image = cv2.imread("C:\\Users\\Evangelio\\Desktop\\test_img\\baybayin.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
dilate = cv2.dilate(thresh, kernal, iterations=1)

contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 10:
        x,y,w,h = cv2.boundingRect(cnt)
        crop_img = image[y:y+h, x:x+w]
        cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.putText(image, "A", (x,y+h + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)
        # plt.imshow(crop_img)
        # plt.show()


cv2.imshow('image', image)
cv2.waitKey()


