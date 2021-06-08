from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Progressbar
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
root = Tk()
#root.title('Baybayin Image Translator')

#root.geometry('900x750') #w x h
#SPLASH
width_of_window=427
height_of_window=250
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_height()
x_coordinate=(screen_width/2)-(width_of_window/2)
y_coordinate=(screen_height/2)-(height_of_window/2)+395
root.geometry("%dx%d+%d+%d"%(width_of_window,height_of_window,x_coordinate,y_coordinate))

root.overrideredirect(1)

#newline= Label(root)
#uploaded_img=Label(root)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(root,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

def new_win():
  # w.destroy()
    q=Tk()
    newline= Label(q)
    uploaded_img=Label(q)
    q.title('Baybayin Image Translator')
    q.geometry('900x750')

    #l1=Label(q,text='ADD TEXT HERE ',fg='grey',bg=None)
    #l=('Calibri (Body)',24,'bold')
    #l1.config(font=l)
    #l1.place(x=80,y=100)

    q.scrollbar = Scrollbar(q)
    q.scrollbar.pack( side = RIGHT, fill = Y )

    #b1=Button(root,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
    #b1.place(x=170,y=200)

    uploadbtn = Button(q,text="Upload an imageee",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
    #uploadbtn.place(x=170,y=200)
    newline.configure(text='\n')
    newline.pack()
    uploaded_img.pack()

    q.mainloop()

def bar():

    l4=Label(root,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        root.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    root.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)

a='#249794'
Frame(root,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(root,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)

######## Label

l1=Label(root,text='SPLASH',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(root,text='SCREEN',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)

l3=Label(root,text='PROGRAMMED',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)

def extract(path):
    Actual_image = cv2.imread(path)
    Sample_img = cv2.resize(Actual_image,(400,350))
    Image_ht,Image_wd,Image_thickness = Sample_img.shape
    Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_data(Sample_img) 
    mytext=""
    prevy=0
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
                Label(root,text=mytext,font=('Times',15,'bold')).pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
    Label(root,text=mytext,font=('Times',15,'bold')).pack()

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

def upload():
    s=Tk()
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        l1=Label(s,text='ADD TEXT HERE ',fg='grey',bg=None)
        l=('Calibri (Body)',24,'bold')
        l1.config(font=l)
        l1.place(x=80,y=100)

#uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
#newline.configure(text='\n')
#newline.pack()
#uploaded_img.pack()


root.mainloop()
