from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np
import tensorflow.keras as tfk
import cv2

#window
root = Tk()
root.title('Baybayin Image Translator')
root.geometry('800x600')
newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

#image processing and prediction
input_shape = (64,64)

syllables = ["a", "ba", "dara", "ei", "ga", "ha", "ka", "kuw", "la", "ma", "na", "nga", "ou", "pa", "sa", "ta", "tul", "wa", "ya"]

syllable_encoding = {}

#assigning the syllables to integers
for i in range(len(syllables)):
    syllable_encoding[syllables[i]] = i
print(syllable_encoding)

#encoding the label
def encode_label(label):
    return syllable_encoding[label]

#decoding the label
def decode_label(i):
    return syllables[i]

#extracting pixels function
def extract_pixels(filename):
    image_pil = Image.open(filename)
    image_np = np.asarray(image_pil)
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


#for buttons and classification
def classify(path):
    extracted_text = predict(path)
    Label(root,text=extracted_text,font=('Times',32,'bold')).pack()

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: classify(path),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.pack()  
def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  
uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()
root.mainloop()
