#contains all of the methods used, from creating the ML model and the functions for image processing of input

from PIL import Image
import cv2
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow.keras as tfk
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

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

#loading all images from dataset and extracting their pixels
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

#assigning the image matrix and their respective label encoding in a list
X_raw, Y_raw = load_all_images(directory='Baybayin-Handwritten-Character-Dataset/raw')

#visualization of data

def display_image(image):
    plt.figure()
    plt.imshow(image, cmap=plt.cm.binary)
    plt.grid(False)
    plt.show()

#preprocessing of data
X_data = np.asarray(X_raw)
Y_data = np.asarray(Y_raw).reshape((-1,1))

#one hot encoding
def one_hot_encoding(data):
    return OneHotEncoder().fit_transform(data).toarray()

Y_data = one_hot_encoding(Y_data)
print(Y_data.shape)

#argmax

def argmax(probability_logits):
    return np.argmax(probability_logits)

#splitting the dataset into training set and test set
X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.20, random_state=0)

#building the ML model
model = tfk.Sequential([
    tfk.layers.Flatten(input_shape = input_shape),
    tfk.layers.Dense(1024, activation='relu'),
    tfk.layers.Dense(256, activation='relu'),
    tfk.layers.Dense(64, activation='relu'),
    tfk.layers.Dense(19, activation='softmax'),
])

#compiling the ML model
model.compile(optimizer='Adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#training the model
early_stopping = tfk.callbacks.EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(X_train, Y_train,
                    epochs=100,
                    validation_split=0.2,
                    callbacks=[early_stopping])

#testing
test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=2)

def neural_net_prediction(image):
    return model.predict(np.expand_dims(image, axis=0))

#predict function to use

def predict(filename):
    return decode_label(argmax(neural_net_prediction(extract_pixels(filename))))

#saving the model that has the best accuracy
model.save('baybayin.h5')
