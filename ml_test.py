#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 19:09:46 2018

@author: rpmcandrew
"""
import tkinter
import numpy as np
np.random.seed(123)
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()


from matplotlib import pyplot as plt
plt.imshow(X_train[1080])
