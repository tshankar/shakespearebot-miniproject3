########################################
# CS/CNS/EE 155 2018
# Miniproject 3

# Team: Ostrich 
# Members: Anna Resnick, Tara Shankar, Rona Yu
# Description:  Recurrent Neural Network (RNN) Implementation
########################################

# Character-based LSTM model (single model of 100-200 LSTM units) 

# Fully connected layer with softmax nonlinearity
# minimize categorical cross-entropy
# train of a sufficient number of epochs so losss converges
# training data: sequences of fixed length (40 characters)
# Take all possible subsequences of 40 consecutive characters from dataset
# use semi-redundant sequences (sequences that start every n-th character)

# draw softmax samples from trained model
# play around with temperature parameter (control variance) 

import keras 
from keras.layers import LSTM
import numpy
import pandas
import math
# take in sequences of 40 characters 
# normalize the data

# 

model = Sequential()
# 150 LSTM units 
model.add(LSTM(150, input_shape = (1, )))
# add a dense layer 
model.add(Dense(1))
model.compile(loss = 'categorical_crossentropy', optimizer = '')
# train for 100 epochs 
model.fit(trainX, trainY, epochs = 100)
