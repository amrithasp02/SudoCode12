
# coding: utf-8

# In[1]:


from keras.models import load_model
import cv2
import numpy as np
from random import choice


# In[2]:


REV_CLASS_MAP = {}
c = 0
for i in range(65,91):
        REV_CLASS_MAP[c] = chr(i)
        c += 1
REV_CLASS_MAP[26] = 'none'
print(REV_CLASS_MAP)


# In[3]:


def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("asl-model2.h5")

cap = cv2.VideoCapture(0)

text_msg = ''

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    
    cv2.rectangle(frame, (50, 50), (250, 250), (255, 255, 255), 2)
    
    # extract the region of image within the user rectangle
    roi = frame[50:250, 50:250]
    img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))

    # predict the sign made
    pred = model.predict(np.array([img]))
    sign_code = np.argmax(pred[0])
    sign_name = mapper(sign_code)
    
    text_msg += sign_name
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Your Sign: " + sign_name,
                (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.putText(frame, "Text Message: " + text_msg,
                (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow("ASL Sign to Text", frame)

    k = cv2.waitKey(10)
    if k == ord('q'):
        break
    #putting identified text into a text file
    def text_add():
        f=open("output.txt", mode='w', encoding='utf-8')
        if text_msg != 'none':
            f.write(text_msg)
    text_add()
        
f.close()
cap.release()
cv2.destroyAllWindows()

file = open('output.txt')
l = file.readlines()

# filtering through the output message

print(l)
f2 = open('output_modified.txt', mode='w', encoding='utf-8')
lst = []
for i in l[0]:
    lst.append(i)
print(lst)
lst2 = []
c = 0
for i in range(len(lst)):
    if i == 0:
        sign_prev = ''
    else:
        sign_prev = lst[i-1]
    sign_present = lst[i]
    if sign_present == sign_prev:
        c += 1
        if c>8:
            if sign_present not in lst2:
                lst2.append(sign_present)
        else:
            continue
    else:
        c = 0
        continue
print(lst2)

msg = ''
for i in lst2:
    msg+=i
f2.write(msg)
        
f2.close()

#final message stored in output_modified.txt
