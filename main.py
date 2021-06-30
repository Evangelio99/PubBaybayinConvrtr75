from tkinter import *
from tkinter import filedialog
import tkinter
from PIL import ImageTk, Image
import cv2
from numpy import left_shift
import pytesseract
from tkinter import PhotoImage
from tkinter.filedialog import askopenfile

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

root = Tk()

# window
#root.geometry('900x750') #w x h
width_of_window=900
height_of_window=750
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_height()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)+395
root.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))
root.title('Baybayin Image Translator')
icn=PhotoImage(file="icon.png")
root.iconphoto(False,icn)
root.resizable(False, False) # para mawala yung full screen button hehe
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
#root.configure(bg='blue')

# dictionary of colors:
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

# setting switch state:
btnState = False

# loading of images:
navIcon = PhotoImage(file="menu.png")
closeIcon = PhotoImage(file="close.png")
uploadbtn1 = PhotoImage(file="uploadbtn.png")
extractbtn1= PhotoImage(file="extractbtn.png")
logoleft = PhotoImage(file="baybayin.png")
logoright = PhotoImage(file="iconright.png")
box = PhotoImage(file="box.png")

# declaring new var for images for placing
upload_label = Label(image=uploadbtn1)
extract_label = Label(image=extractbtn1)

box_label = Label(image=box)
box_label.place(x=15,y=360)



# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.place(x=312,y=100)

# instruction label
instructions = Label(root, text="Select an Image file on your computer to extract all its text", font=('Bahnschrift',10),bg="#f0f0f0",fg="black")
instructions.place(x=280,y=250)

# vars
newline= Label(root)
uploaded_img=Label(root)


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

# extract button
# def show_extract_button(path):
# extractBtn = Button(root,image=extractbtn1,command=lambda: extract(path),fg="gray", borderwidth=0,font=('Times',15,'bold'))
# extractBtn.place(x=600,y=300)

extractBtn = Button(root,image=extractbtn1,state=tkinter.DISABLED, fg="gray", borderwidth=0,font=('Times',15,'bold'))
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
                Label(root,text=mytext,bg="white",font=('Bahnschrift',15,'bold')).place(x=450,y=newl)
                mytext=""
                newl += 30
            mytext = mytext + text[11]+" "
            prevy=y
    print(mytext)
    Label(root,text=mytext,bg="white",font=('Bahnschrift',15,'bold')).place(x=450,y=newl)
    #Label(root,text=mytext,font=('Times',15,'bold')).pack(padx=5, pady=30, side=RIGHT)

# upload button
uploadbtn = Button(root,image=uploadbtn1,command=upload, borderwidth=0 ,fg="gray",font=('Times',15,'bold'))
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
        root.config(bg="#f0f0f0")

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


# top navigation bar:
topFrame = Frame(root, bg="white")
topFrame.pack(side="top", fill=X)

# header label text:
homeLabel = Label(topFrame, font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

# header label text:
homeLabel1 = Label(topFrame, text="        BAYBAYIN TRANSLATOR", font="Bahnschrift 15", bg="white", fg="gray17", height=2, padx=20)
homeLabel1.pack(side="left")
#logo_left = Label(topFrame, image=logoleft, bg="white")
#logo_left.place(x=50,y=8)
logo_right = Label(topFrame, image=logoright, bg="white")
logo_right.place(x=810,y=10)

# main label text:
#brandLabel = Label(root, font="System 30", bg="#f0f0f0", fg="green")
#brandLabel.place(x=100, y=250)

# navbar button:
navbarBtn = Button(topFrame, image=navIcon, bg="white", activebackground="#1cbdbd", bd=0, padx=20, command=switch)
navbarBtn.place(x=10, y=10)

# setting Navbar frame:
navRoot = Frame(root, bg="#cecece", height=1000, width=300)
navRoot.place(x=-300, y=0)
Label(navRoot, font="Bahnschrift 15", bg="white", fg="black", height=2, width=300, padx=20).place(x=0, y=0)

# set y-coordinate of Navbar widgets:
y = 80

# option in the navbar:
options = ["Home", "Settings", "Help", "About"]

# Navbar Option Buttons:
for i in range(4):
    Button(navRoot, text=options[i], font="BahnschriftLight 15", bg="#cecece", fg="white", activebackground="#9c9c9c", activeforeground="#1cbdbd", bd=0).place(x=25, y=y)
    y += 40

# Navbar Close Button:
closeBtn = Button(navRoot, image=closeIcon, bg="white", activebackground="#1cbdbd", bd=0, command=switch)
closeBtn.place(x=250, y=10)

# 
#newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

#uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()


root.mainloop()
