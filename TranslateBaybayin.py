from PIL import Image
import numpy as np
import tensorflow.keras as tfk
import cv2

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

def classify(path):
    image = cv2.imread(path)

    # Image Processing
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
    dilate = cv2.dilate(thresh, kernal, iterations=1)
    contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 

    # Translate each baybayin characters into text
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10:
            x,y,w,h = cv2.boundingRect(cnt)
            crop_img = image[y:y+h, x:x+w]
            cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
            cv2.putText(image, predict(crop_img), (x,y+h + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

    img = Image.fromarray(image)

    # resize image
    resized1 = img.resize((360, 200), Image.ANTIALIAS)
    return resized1