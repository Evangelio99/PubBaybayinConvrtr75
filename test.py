from main import extract
from PIL import Image
import cv2
import os
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import tensorflow as tf
#import tensorflow.keras as tfk
#from sklearn.preprocessing import OneHotEncoder
#from sklearn.model_selection import train_test_split

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
        image_res = cv2.cvtColor(image_res)
    return image_res / 255.0

#loading all images from dataset
def load_all_images(directory):
    X_raw = []
    Y_raw = []

    for syllable in syllables:
        for filename in os.listdir(directory + '/' + syllable + '/'):
            image_matrix = extract_pixels(directory + '/' + syllable + '/' + filename)
            label_encoding = encode_label(syllable)

            X_raw.append(image_matrix)
            Y_raw.append(label_encoding)

    return X_raw, Y_raw

X_raw, Y_raw = load_all_images(directory='Baybayin-Handwritten-Character-Dataset/raw')
