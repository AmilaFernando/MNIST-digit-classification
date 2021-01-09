# -*- coding: utf-8 -*-
"""1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cKqti0C1IBQr4YXk1q9HqeEIfQhogNQ4
"""

## Import libraries
import numpy as np
from matplotlib import pyplot as plt
from tensorflow import keras
from keras.datasets import mnist
from tensorflow.keras import layers
from keras.layers import Dense, Conv2D, Flatten

# Load test and train data
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Understanding test and train data
print(type(X_train))
print(type(Y_train))
print(type(X_test))
print(type(Y_test))

print(X_train.shape) 
print(Y_train.shape) 
print(X_test.shape) 
print(Y_test.shape)

X_train = np.expand_dims(X_train, -1)
X_test = np.expand_dims(X_test, -1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# check the min and max values
np.min(X_train), np.max(X_train)
#np.min(Y_train), np.max(Y_test)

# Normalize the data
X_train /= 255
X_test /= 255

# Check min and max values
np.min(X_train), np.max(X_train)

# make y data categorical
no_of_classes = 10
Y_train = keras.utils.to_categorical(Y_train, no_of_classes)
Y_test = keras.utils.to_categorical(Y_test, no_of_classes)

# Model
model = keras.Sequential()

# Add Layers
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

# Model summary
model.summary()

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit the model
model.fit(X_train, Y_train, batch_size=128, epochs=15, validation_split=0.1)

# Evaluate the model
score = model.evaluate(X_test, Y_test, verbose=0)

print("Model accuracy: ", score[1])