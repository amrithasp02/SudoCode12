
# coding: utf-8

# In[2]:


from keras.models import load_model
import cv2
import numpy as np
import sys


# In[1]:


REV_CLASS_MAP = {}
c = 0
for i in range(65,91):
        REV_CLASS_MAP[c] = chr(i)
        c += 1
REV_CLASS_MAP[26] = 'none'
print(REV_CLASS_MAP)


# testing for A


filepath = 'asl_alphabet_test/A_test.jpg'


def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model("asl-model2.h5")

# prepare the image
img = cv2.imread(filepath)
print(img)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (227, 227))

# predict the sign made
pred = model.predict(np.array([img]))
sign_code = np.argmax(pred[0])
sign_name = mapper(sign_code)

print("Predicted: {}".format(sign_name))


# testing for H


filepath = 'asl_alphabet_test/H_test.jpg'


def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model("asl-model2.h5")

# prepare the image
img = cv2.imread(filepath)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (227, 227))

# predict the sign made
pred = model.predict(np.array([img]))
sign_code = np.argmax(pred[0])
sign_name = mapper(sign_code)

print(pred)
print("Predicted: {}".format(sign_name))

