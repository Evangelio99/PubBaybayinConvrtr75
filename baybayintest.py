from tkinter import *
from tkinter import filedialog
import tkinter
import tkinter as tk
from PIL import ImageTk, Image
from numpy import left_shift
import pytesseract
from tkinter import PhotoImage
import tensorflow as tf
import numpy as np
import tensorflow.keras as tfk
import cv2
from tkinter.filedialog import askopenfile
from tkinter import messagebox

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# frames
def show_frame(frame):
    frame.tkraise()

window = tk.Tk()

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# window config
width_of_window=900
height_of_window=750
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_height()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)+395
window.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))

window.title('Baybayin Image Translator')
icn=PhotoImage(file="Assets/icon.png")
window.iconphoto(False,icn)
window.resizable(False, False) # para mawala yung full screen button hehe

# creating frames
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

# for loop for creating 4 frames
for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0,column=0,sticky='nsew')

# loading of images:
navIcon = PhotoImage(file="Assets/menu.png")
closeIcon = PhotoImage(file="Assets/close.png")
logoleft = PhotoImage(file="Assets/baybayin.png")
logoright = PhotoImage(file="Assets/iconright.png")
box = PhotoImage(file="Assets/box.png")
navbar = PhotoImage(file="Assets/navbar.png")
# buttons
uploadbtn1 = PhotoImage(file="Assets/uploadbtn1.png")
extractbtn1= PhotoImage(file="Assets/translatebtn1.png")
homebtn = PhotoImage(file="Assets/homebtn.png")
translatebtn = PhotoImage(file="Assets/translatebtn.png")
helpbtn = PhotoImage(file="Assets/helpbtn.png")
aboutbtn = PhotoImage(file="Assets/aboutbtn.png")
# backgrounds
homepage = PhotoImage(file="Assets/home_page_bg.png")
translate = PhotoImage(file="Assets/translate_page_bg.png")
help = PhotoImage(file="Assets/help_page_pg.png")
about = PhotoImage(file="Assets/about_page_bg.png")
bgg = PhotoImage(file="Assets/bg.png")

# background of Frame 1
translate1 = Label(frame2, image=translate)
translate1.place(x=0,y=0)

# declaring new var for images for placing
upload_label = Label(image=uploadbtn1)
extract_label = Label(image=extractbtn1)

# vars
newline= Label(frame2)
uploaded_img=Label(frame2)
processed_img=Label(frame2) 

#image processing and prediction
input_shape = (64,64)

syllables = ["a", "ba", "dara", "ei", "ga", "ha", "ka", "kuw", "la", "ma", "na", "nga", "ou", "pa", "sa", "ta", "tul", "wa", "ya"]

syllable_encoding = {}

# assigning the syllables to integers
for i in range(len(syllables)):
    syllable_encoding[syllables[i]] = i

# encoding the label
def encode_label(label):
    return syllable_encoding[label]

# decoding the label
def decode_label(i):
    return syllables[i]

# extracting pixels function
def extract_pixels(filename):
    # image_pil = Image.open(filename)
    # image_np = np.asarray(image_pil)
    image_np = np.asarray(filename)
    image_res = cv2.resize(image_np,
                          dsize=input_shape,
                          interpolation=cv2.INTER_CUBIC)
    if len(image_res.shape) == 3:
        image_res = cv2.cvtColor(image_res, cv2.COLOR_BGR2GRAY)
    return image_res / 255.0

# argmax
def argmax(probability_logits):
    return np.argmax(probability_logits)

model = tfk.models.load_model('baybayin.h5')

def neural_net_prediction(image):
    return model.predict(np.expand_dims(image, axis=0))

# predict function to use
def predict(filename):
    return decode_label(argmax(neural_net_prediction(extract_pixels(filename))))

def upload():
    try:
        path=filedialog.askopenfilename()
        # open image 
        image=Image.open(path)

        # resize image
        resized = image.resize((370, 317), Image.ANTIALIAS)

        img=ImageTk.PhotoImage(resized)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        uploaded_img.configure(background="white")
        uploaded_img.image=img
        uploaded_img.place(x=40,y=373)

        # show_extract_button(path)
        extractBtn["state"] = tkinter.NORMAL
        extractBtn["command"] = lambda: classify(path)

    except:
        pass  

# translate button
extractBtn= Button(frame2,image=extractbtn1,state=tkinter.DISABLED, activebackground="#d1d1cb", fg="gray",borderwidth=0,font=('Times',15,'bold'),bg="#d1d1cb")
extractBtn.place(x=600,y=280) 

# for buttons and classification
def classify(path):
    image = cv2.imread(path)
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
            cv2.putText(image, predict(crop_img), (x,y+h + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)
        # plt.imshow(crop_img)
        # plt.show()


    img = Image.fromarray(image)

    # resize image
    resized1 = img.resize((360, 200), Image.ANTIALIAS)

    imgtk = ImageTk.PhotoImage(image=resized1)
    processed_img.configure(image=imgtk)
    processed_img.image=imgtk
    processed_img.place(x=492,y=433)
    # cv2.imshow('image', image)
    # cv2.waitKey()
    # extracted_text = predict(path)
    # Label(root,text=extracted_text,font=('Times',32,'bold')).pack()

# open message box instructions in translate page
def openwindow():
    messagebox.showinfo("Instructions", "Upload Baybayin Image/s only. There should be enough spaces between Baybayin scripts and it should not be small and pixelated for better translation.")

#==============================================================FRAMES=======================================================================
#==================Frame 1 Homepage
# homepage background
homepage1 = Label(frame1, image=homepage)
homepage1.place(x=0,y=0)

# static buttons
f1_btnhome = tk.Button(frame1, image=homebtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame1))
f1_btnhome.place(x=263,y=37)

f1_btntranslate = tk.Button(frame1, image=translatebtn,bg="white",borderwidth=0 ,command=lambda:[show_frame(frame2),openwindow()])
f1_btntranslate.place(x=394,y=35)

f1_btnhelp = tk.Button(frame1, image=helpbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame3))
f1_btnhelp.place(x=593,y=39)

f1_btnabout = tk.Button(frame1, image=aboutbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame4))
f1_btnabout.place(x=730,y=38)


#==================Frame 2 Translate page
#Bg is at line 72 and 73 ata

# upload button of Baybayin Image
uploadbtn = Button(frame2,image=uploadbtn1,activebackground="#d1d1cb",command=upload,borderwidth=0,bg="#d1d1cb",font=('Times',15,'bold'))
uploadbtn.place(x=153,y=280)

# static buttons
f2_btnhome = tk.Button(frame2, image=homebtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame1))
f2_btnhome.place(x=263,y=37)

f2_btntranslate = tk.Button(frame2, image=translatebtn,bg="white",borderwidth=0 ,command=lambda:[show_frame(frame2),openwindow()])
f2_btntranslate.place(x=394,y=35)

f2_btnhelp = tk.Button(frame2, image=helpbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame3))
f2_btnhelp.place(x=593,y=39)

f2_btnabout = tk.Button(frame2, image=aboutbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame4))
f2_btnabout.place(x=730,y=38)


#==================Frame 3 Help page
# help background
help1 = Label(frame3, image=help)
help1.place(x=0,y=0)

# static buttons
f3_btnhome = tk.Button(frame3, image=homebtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame1))
f3_btnhome.place(x=263,y=37)

f3_btntranslate = tk.Button(frame3, image=translatebtn,bg="white",borderwidth=0 ,command=lambda:[show_frame(frame2),openwindow()])
f3_btntranslate.place(x=394,y=35)

f3_btnhelp = tk.Button(frame3, image=helpbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame3))
f3_btnhelp.place(x=593,y=39)

f3_btnabout = tk.Button(frame3, image=aboutbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame4))
f3_btnabout.place(x=730,y=38)


#==================Frame 4 About page
# about us background
about1 = Label(frame4, image=about)
about1.place(x=0,y=0)

# static buttons
f4_btnhome = tk.Button(frame4, image=homebtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame1))
f4_btnhome.place(x=263,y=37)

f4_btntranslate = tk.Button(frame4, image=translatebtn,bg="white",borderwidth=0 ,command=lambda:[show_frame(frame2),openwindow()])
f4_btntranslate.place(x=394,y=35)

f4_btnhelp = tk.Button(frame4, image=helpbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame3))
f4_btnhelp.place(x=593,y=39)

f4_btnabout = tk.Button(frame4, image=aboutbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame4))
f4_btnabout.place(x=730,y=38)

show_frame(frame1)

window.mainloop()
