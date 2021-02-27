
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from keras.optimizers import Adam
from keras.utils import np_utils
import os
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
from keras.layers import Dropout


# In[2]:


IMG_SAVE_PATH = 'asl_alphabet_train/asl_alphabet_train'

CLASS_MAP = {}
c = 0
for i in range(65,91):
        CLASS_MAP[chr(i)] = c
        c += 1
CLASS_MAP['none'] = 26
print(CLASS_MAP)
NUM_CLASSES = len(CLASS_MAP)


def mapper(val):
    return CLASS_MAP[val]


# In[ ]:


dataset = []
for directory in os.listdir(IMG_SAVE_PATH):
    print(directory)
    path = os.path.join(IMG_SAVE_PATH, directory)
    a = 0
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        if a<2000:
            # to make sure no hidden files get in our way
            if item.startswith("."):
                continue
            img = cv2.imread(os.path.join(path, item))
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (227, 227))
            dataset.append([img, directory])
            a += 1
print(len(dataset))


# In[ ]:


data, labels = zip(*dataset)
labels = list(map(mapper, labels))

# one hot encode the labels
labels = np_utils.to_categorical(labels)

