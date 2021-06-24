#this includes only the functions needed for the image recognition, such as extracting the pixels, encoding/decoding, and the predict function
#load the existing model using var = tfk.models.load_model('baybayin.h5')
#copy paste niyo lang lagi ito hehe

from PIL import Image
import cv2
import numpy as np
import tensorflow.keras as tfk

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

def argmax(probability_logits):
    return np.argmax(probability_logits)

model = tfk.models.load_model('baybayin.h5')

def neural_net_prediction(image):
    return model.predict(np.expand_dims(image, axis=0))

#predict function to use

def predict(filename):
    return decode_label(argmax(neural_net_prediction(extract_pixels(filename))))

# print(predict('sampletest.jpg'))

