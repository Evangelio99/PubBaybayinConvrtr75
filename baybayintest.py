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
icn=PhotoImage(file="icon.png")
window.iconphoto(False,icn)
window.resizable(False, False) # para mawala yung full screen button hehe
#window.configure(bg='blue')

# setting switch state:
btnState = False

# creating frames
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

for frame in (frame1, frame2, frame3, frame4):
    frame.grid(row=0,column=0,sticky='nsew')

# loading of images:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")
logoleft = PhotoImage(file="baybayin.png")
logoright = PhotoImage(file="iconright.png")
box = PhotoImage(file="box.png")
navbar = PhotoImage(file="navbar.png")
#Buttons
uploadbtn1 = PhotoImage(file="uploadbtn1.png")
extractbtn1= PhotoImage(file="translatebtn1.png")
homebtn = PhotoImage(file="homebtn.png")
translatebtn = PhotoImage(file="translatebtn.png")
helpbtn = PhotoImage(file="helpbtn.png")
aboutbtn = PhotoImage(file="aboutbtn.png")
#Backgrounds
homepage = PhotoImage(file="homepage_with_buttons.png")
translate = PhotoImage(file="translate_page_bg.png")
help = PhotoImage(file="help_page_pg.png")
about = PhotoImage(file="about_page_bg.png")
bgg = PhotoImage(file="bg.png")




# assets
# box_label = Label(frame2, image=box)
# box_label.place(x=22,y=360)

# bg = Label(frame2, image=bgg)
# bg.place(x=0,y=0)

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

#assigning the syllables to integers
for i in range(len(syllables)):
    syllable_encoding[syllables[i]] = i

#encoding the label
def encode_label(label):
    return syllable_encoding[label]

#decoding the label
def decode_label(i):
    return syllables[i]

#extracting pixels function
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

#argmax
def argmax(probability_logits):
    return np.argmax(probability_logits)

model = tfk.models.load_model('baybayin.h5')

def neural_net_prediction(image):
    return model.predict(np.expand_dims(image, axis=0))

#predict function to use
def predict(filename):
    return decode_label(argmax(neural_net_prediction(extract_pixels(filename))))

def upload():
    try:
        path=filedialog.askopenfilename()
        # open image 
        image=Image.open(path)

        # resize image
        resized = image.resize((400, 317), Image.ANTIALIAS)

        img=ImageTk.PhotoImage(resized)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        uploaded_img.configure(background="white")
        uploaded_img.image=img
        uploaded_img.place(x=22,y=405)

        # show_extract_button(path)
        extractBtn["state"] = tkinter.NORMAL
        extractBtn["command"] = lambda: classify(path)

    except:
        pass  

extractBtn= Button(frame2,image=extractbtn1,state=tkinter.DISABLED, fg="gray",borderwidth=0,font=('Times',15,'bold'))
extractBtn.place(x=600,y=300) 


#for buttons and classification
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
    imgtk = ImageTk.PhotoImage(image=img)
    processed_img.configure(image=imgtk)
    processed_img.image=imgtk
    processed_img.place(x=450,y=420)
    # cv2.imshow('image', image)
    # cv2.waitKey()
    # extracted_text = predict(path)
    # Label(root,text=extracted_text,font=('Times',32,'bold')).pack()


uploadbtn = Button(frame2,image=uploadbtn1,command=upload,borderwidth=0 ,font=('Times',15,'bold'))
uploadbtn.place(x=153,y=300)

# setting switch function:
# def switch():
#     global btnState
#     if btnState is True:
#         # create animated Navbar closing:
#         for x in range(301):
#             navRoot.place(x=-x, y=0)
#             topFrame.update()

#         # resetting widget colors:
#         #brandLabel.config(bg="#f0f0f0", fg="green")
#         instructions.config(bg="#f0f0f0",fg="black")
#         homeLabel.config(bg="white")
#         topFrame.config(bg="white")
#         frame2.config(bg="#f0f0f0")

#         # turning button OFF:
#         btnState = False
#     else:
#         # make root dim:
#         #brandLabel.config(bg="#f0f0f0", fg="#5F5A33")
#         #homeLabel.config(bg=color["nero"])
#         #topFrame.config(bg=color["nero"])
#         #root.config(bg=color["nero"])
#         instructions.config(bg="#f0f0f0",fg="#858585")
        
#         # created animated Navbar opening:
#         for x in range(-300, 0):
#             navRoot.place(x=x, y=0)
#             topFrame.update()

#         # turning button ON:
#         btnState = True

#open new window for instruction 
def openwindow():
    new_window= Tk()
    new_window.eval('tk::PlaceWindow . center') #centered window
    new_window.geometry("250x250")
    new_window.title("Instructions")
    new_window.resizable(False,False)
    lbl = Label(new_window, text="Baybayin Image Converter intructions")
    lbl.pack()


#==================Frame 1 Homepage
# f1_box_label = tk.Label(frame1, image=box)
# f1_box_label.place(x=100,y=10)

uploadbtn = Button(frame2,image=uploadbtn1,command=upload,borderwidth=0 ,font=('Times',15,'bold'))
uploadbtn.place(x=153,y=300)

homepage1 = Label(frame1, image=homepage)
homepage1.place(x=0,y=0)

f1_btnhome = tk.Button(frame1, image=homebtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame1))
f1_btnhome.place(x=280,y=40)

f1_btntranslate = tk.Button(frame1, image=translatebtn,bg="white",borderwidth=0 ,command=lambda:[show_frame(frame2),openwindow()])
f1_btntranslate.place(x=450,y=10)

f1_btnhelp = tk.Button(frame1, image=helpbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame3))
f1_btnhelp.place(x=550,y=10)

f1_btnabout = tk.Button(frame1, image=aboutbtn,bg="white",borderwidth=0 ,command=lambda:show_frame(frame4))
f1_btnabout.place(x=650,y=10)

#==================Frame 2 Translate page
translate1 = Label(frame2, image=translate)
translate1.place(x=0,y=0)

f2_btnhome = tk.Button(frame2, text='Home',command=lambda:show_frame(frame1))
f2_btnhome.place(x=350,y=10)

f2_btntranslate = tk.Button(frame2, text='Translate',command=lambda:[show_frame(frame2),openwindow()])
f2_btntranslate.place(x=450,y=10)

f2_btnhelp = tk.Button(frame2, text='Help',command=lambda:show_frame(frame3))
f2_btnhelp.place(x=550,y=10)

f2_btnabout = tk.Button(frame2, text='About',command=lambda:show_frame(frame4))
f2_btnabout.place(x=650,y=10)

# # logo
# logo = Image.open('logo.png')
# logo = ImageTk.PhotoImage(logo)
# logo_label = Label(frame2, image=logo)
# logo_label.image = logo
# logo_label.place(x=312,y=100)

# instruction label
# instructions = Label(frame2, text="Select an Image file on your computer to extract all its text", font=('Bahnschrift',10),bg="#f0f0f0",fg="black")
# instructions.place(x=280,y=250)

# logo_right = Label(frame2, image=logoright, bg="white")
# logo_right.place(x=810,y=10)
# logo_left = Label(frame2, image=logoleft, bg="white")
# logo_left.place(x=50,y=8)

#==================Frame 3 Help page
help1 = Label(frame3, image=help)
help1.place(x=0,y=0)

# f3_title=  tk.Label(frame3, text='Insert Help page',font='times 35')
# f3_title.place(x=0,y=50)

f3_btnhome = tk.Button(frame3, text='Home',command=lambda:show_frame(frame1))
f3_btnhome.place(x=350,y=10)

f3_btntranslate = tk.Button(frame3, text='Translate',command=lambda:[show_frame(frame2),openwindow()])
f3_btntranslate.place(x=450,y=10)

f3_btnhelp = tk.Button(frame3, text='Help',command=lambda:show_frame(frame3))
f3_btnhelp.place(x=550,y=10)

f3_btnabout = tk.Button(frame3, text='About',command=lambda:show_frame(frame4))
f3_btnabout.place(x=650,y=10)

#==================Frame 4 About page
about1 = Label(frame4, image=about)
about1.place(x=0,y=0)

# f4_title=  tk.Label(frame4, text='Insert About page',font='times 35')
# f4_title.place(x=0,y=50)

f4_btnhome = tk.Button(frame4, text='Home',command=lambda:show_frame(frame1))
f4_btnhome.place(x=350,y=10)

f4_btntranslate = tk.Button(frame4, text='Translate',command=lambda:[show_frame(frame2),openwindow()])
f4_btntranslate.place(x=450,y=10)

f4_btnhelp = tk.Button(frame4, text='Help',command=lambda:show_frame(frame3))
f4_btnhelp.place(x=550,y=10)

f4_btnabout = tk.Button(frame4, text='About',command=lambda:show_frame(frame4))
f4_btnabout.place(x=650,y=10)

# navbar button:
# navbarBtn = Button(frame2, image=navIcon, bg="white", activebackground="#1cbdbd", bd=0, padx=20, command=switch)
# navbarBtn.place(x=10, y=10)

# # setting Navbar frame:
# navRoot = Frame(frame2, bg="#cecece", height=1000, width=300)
# navRoot.place(x=-300, y=0)
# Label(navRoot, font="Bahnschrift 15", bg="white", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# # set y-coordinate of Navbar widgets:
# y = 80

# # option in the navbar:

# # Navbar Option Buttons:
# b1 = tk.Button(navRoot, text='Home', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame1)).place(x=25, y=80)
# b2 = tk.Button(navRoot, text='Translate', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame2)).place(x=25, y=120)
# b3 = tk.Button(navRoot, text='Help', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame3)).place(x=25, y=160)
# b4 = tk.Button(navRoot, text='About', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame3)).place(x=25, y=200)

# # Navbar Close Button:
# closeBtn = Button(navRoot, image=closeIcon, bg="white", activebackground="red", bd=0, command=switch)
# closeBtn.place(x=250, y=10)

show_frame(frame1)

window.mainloop()
