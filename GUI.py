from tkinter import *
from tkinter import filedialog
import tkinter
import tkinter as tk
from PIL import ImageTk, Image
from numpy import left_shift
from tkinter import PhotoImage
from tkinter.filedialog import askopenfile
from tkinter import messagebox
from TranslateBaybayin import *

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

        # remove the current processed image
        processed_img.configure(image='')

        # show_extract_button(path)
        extractBtn["state"] = tkinter.NORMAL
        extractBtn["command"] = lambda: processImg(path)

    except:
        pass  

# translate button
extractBtn= Button(frame2,image=extractbtn1,state=tkinter.DISABLED, activebackground="#d1d1cb", fg="gray",borderwidth=0,font=('Times',15,'bold'),bg="#d1d1cb")
extractBtn.place(x=600,y=280)

def processImg(path):
    img = classify(path)

    # convert cv image to ImageTk
    imgtk = ImageTk.PhotoImage(image=img)
    processed_img.configure(image=imgtk)
    processed_img.image=imgtk
    processed_img.place(x=492,y=433)

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
