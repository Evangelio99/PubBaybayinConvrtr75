from tkinter import *
from tkinter import filedialog
import tkinter
import tkinter as tk
from PIL import ImageTk, Image
import cv2
from numpy import left_shift
import pytesseract
from tkinter import PhotoImage
from tkinter.filedialog import askopenfile

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Kin\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

# frames
def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
#window.state('zoomed')

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
uploadbtn1 = PhotoImage(file="uploadbtn.png")
extractbtn1= PhotoImage(file="extractbtn.png")
logoleft = PhotoImage(file="baybayin.png")
logoright = PhotoImage(file="iconright.png")
box = PhotoImage(file="box.png")
navbar = PhotoImage(file="navbar.png")
red = PhotoImage(file="red.png")
sour = PhotoImage(file="sour.png")
folklore = PhotoImage(file="taylor.png")

# assets
box_label = Label(frame2, image=box)
box_label.place(x=22,y=360)


# declaring new var for images for placing
upload_label = Label(image=uploadbtn1)
extract_label = Label(image=extractbtn1)

# assets
box_label = Label(frame2, image=box)
box_label.place(x=22,y=360)

# vars
newline = Label(frame2)
uploaded_img = Label(frame2)

# uploading of picture
def upload():
    try:
        path=filedialog.askopenfilename()
        # open image 
        image=Image.open(path)

        # resize image
        resized = image.resize((400, 317), Image.ANTIALIAS)

        img=ImageTk.PhotoImage(resized)
        uploaded_img.configure(image=img)
        uploaded_img.configure(background="white")
        uploaded_img.image=img
        uploaded_img.place(x=22,y=405)

        # show_extract_button(path)
        extractBtn["state"] = tkinter.NORMAL
        extractBtn["command"] = lambda: extract(path)

    except:
        pass 

extractBtn = Button(frame2,image=extractbtn1,state=tkinter.DISABLED, fg="gray", borderwidth=0,font=('Times',15,'bold'))
extractBtn.place(x=600,y=300)

# extraction
def extract(path):
    Actual_image = cv2.imread(path)
    Sample_img = cv2.resize(Actual_image,(400,350))
    Image_ht,Image_wd,Image_thickness = Sample_img.shape
    Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_data(Sample_img) 
    mytext=""
    prevy=0
    newl = 420
    for cnt,text in enumerate(texts.splitlines()):
        if cnt==0:
            continue
        text = text.split()
        if len(text)==12:
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            if(len(mytext)==0):
                prey=y
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext)
                #Label(root,text=mytext,font=('Times',15,'bold')).pack(padx=5, pady=15, side=RIGHT)
                Label(frame2,text=mytext,bg="white",font=('Bahnschrift',15,'bold')).place(x=450,y=newl)
                mytext=""
                newl += 30
            mytext = mytext + text[11]+" "
            prevy=y
    print(mytext)
    Label(frame2,text=mytext,bg="white",font=('Bahnschrift',15,'bold')).place(x=450,y=newl)
    #Label(root,text=mytext,font=('Times',15,'bold')).pack(padx=5, pady=30, side=RIGHT)

# upload button
uploadbtn = Button(frame2,image=uploadbtn1,command=upload, borderwidth=0 ,fg="gray",font=('Times',15,'bold'))
uploadbtn.place(x=153,y=300)

# setting switch function:
def switch():
    global btnState
    if btnState is True:
        # create animated Navbar closing:
        for x in range(301):
            navRoot.place(x=-x, y=0)
            topFrame.update()

        # resetting widget colors:
        #brandLabel.config(bg="#f0f0f0", fg="green")
        instructions.config(bg="#f0f0f0",fg="black")
        homeLabel.config(bg="white")
        topFrame.config(bg="white")
        frame2.config(bg="#f0f0f0")

        # turning button OFF:
        btnState = False
    else:
        # make root dim:
        #brandLabel.config(bg="#f0f0f0", fg="#5F5A33")
        #homeLabel.config(bg=color["nero"])
        #topFrame.config(bg=color["nero"])
        #root.config(bg=color["nero"])
        instructions.config(bg="#f0f0f0",fg="#858585")
        
        # created animated Navbar opening:
        for x in range(-300, 0):
            navRoot.place(x=x, y=0)
            topFrame.update()

        # turning button ON:
        btnState = True

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
#f1_box_label = tk.Label(frame1, image=box)
#f1_box_label.place(x=100,y=10)
taylor1 = Label(frame1, image=red)
taylor1.place(x=0,y=0)

topFrame = Frame(frame1, bg="white")
topFrame.pack(side="top", fill=X)

# header label text:
homeLabel = Label(topFrame, font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

f1_btnhome = tk.Button(frame1, text='Home',command=lambda:show_frame(frame1))
f1_btnhome.place(x=350,y=10)

f1_btntranslate = tk.Button(frame1, text='Translate',command=lambda:[show_frame(frame2), openwindow()])
f1_btntranslate.place(x=450,y=10)

f1_btnhelp = tk.Button(frame1, text='Help',command=lambda:show_frame(frame3))
f1_btnhelp.place(x=550,y=10)

f1_btnabout = tk.Button(frame1, text='About',command=lambda:show_frame(frame4))
f1_btnabout.place(x=650,y=10)

#==================Frame 2 Translate page
topFrame = Frame(frame2, bg="white")
topFrame.pack(side="top", fill=X)

# header label text:
homeLabel = Label(topFrame, font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

f2_btnhome = tk.Button(frame2, text='Home',command=lambda:show_frame(frame1))
f2_btnhome.place(x=350,y=10)

f2_btntranslate = tk.Button(frame2, text='Translate',command=lambda:[show_frame(frame2), openwindow()])
f2_btntranslate.place(x=450,y=10)

f2_btnhelp = tk.Button(frame2, text='Help',command=lambda:show_frame(frame3))
f2_btnhelp.place(x=550,y=10)

f2_btnabout = tk.Button(frame2, text='About',command=lambda:show_frame(frame4))
f2_btnabout.place(x=650,y=10)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(frame2, image=logo)
logo_label.image = logo
logo_label.place(x=312,y=100)

# instruction label
instructions = Label(frame2, text="Select an Image file on your computer to extract all its text", font=('Bahnschrift',10),bg="#f0f0f0",fg="black")
instructions.place(x=280,y=250)

logo_right = Label(frame2, image=logoright, bg="white")
logo_right.place(x=810,y=10)
logo_left = Label(frame2, image=logoleft, bg="white")
logo_left.place(x=50,y=8)

#==================Frame 3 Help page
olivia = Label(frame3, image=sour)
olivia.place(x=0,y=0)

f3_title=  tk.Label(frame3, text='Insert Help page',font='times 35')
f3_title.place(x=0,y=50)

topFrame = Frame(frame3, bg="white")
topFrame.pack(side="top", fill=X)

# header label text:
homeLabel = Label(topFrame, font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

f3_btnhome = tk.Button(frame3, text='Home',command=lambda:show_frame(frame1))
f3_btnhome.place(x=350,y=10)

f3_btntranslate = tk.Button(frame3, text='Translate',command=lambda:[show_frame(frame2),openwindow()])
f3_btntranslate.place(x=450,y=10)

f3_btnhelp = tk.Button(frame3, text='Help',command=lambda:show_frame(frame3))
f3_btnhelp.place(x=550,y=10)

f3_btnabout = tk.Button(frame3, text='About',command=lambda:show_frame(frame4))
f3_btnabout.place(x=650,y=10)

#==================Frame 4 About page
taylor2 = Label(frame4, image=folklore)
taylor2.place(x=0,y=0)

f4_title=  tk.Label(frame4, text='Insert About page',font='times 35')
f4_title.place(x=0,y=50)

topFrame = Frame(frame4, bg="white")
topFrame.pack(side="top", fill=X)

# header label text:


homeLabel = Label(topFrame, font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

f4_btnhome = tk.Button(frame4, text='Home',command=lambda:show_frame(frame1))
f4_btnhome.place(x=350,y=10)

f4_btntranslate = tk.Button(frame4, text='Translate',command=lambda:[show_frame(frame2), openwindow()])
f4_btntranslate.place(x=450,y=10)

f4_btnhelp = tk.Button(frame4, text='Help',command=lambda:show_frame(frame3))
f4_btnhelp.place(x=550,y=10)

f4_btnabout = tk.Button(frame4, text='About',command=lambda:show_frame(frame4))
f4_btnabout.place(x=650,y=10)

# navbar button:
navbarBtn = Button(frame2, image=navIcon, bg="white", activebackground="#1cbdbd", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = Frame(frame2, bg="#cecece", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15", bg="white", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80

# option in the navbar:

# Navbar Option Buttons:
b1 = tk.Button(navRoot, text='Home', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame1)).place(x=25, y=80)
b2 = tk.Button(navRoot, text='Translate', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame2)).place(x=25, y=120)
b3 = tk.Button(navRoot, text='Help', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame3)).place(x=25, y=160)
b4 = tk.Button(navRoot, text='About', font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0, command=lambda:show_frame(frame3)).place(x=25, y=200)

# Navbar Close Button:
closeBtn = Button(navRoot, image=closeIcon, bg="white", activebackground="#1cbdbd", bd=0, command=switch)
closeBtn.place(x=250, y=10)


show_frame(frame1)

window.mainloop()
