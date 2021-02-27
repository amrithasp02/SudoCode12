
import cv2

from tkinter import *
from tkinter import ttk
from PIL import *

#defining the interface structure
root=Tk()
root.geometry('1080x720')
root.config(bg="#CCCCCC")
root.title("SUDOCODE")

#adding lables
label=Label(root, text="ASL to Text Converter", font = "arial 20 bold",bg='#808080')
label.pack()

#creating button
trans_btn=Button(root,text="Translate",bg = "blue")
trans_btn.place(x = 540, y= 680)

#definig camera stream (output) structure
cam=Frame(root, bg="white", width=100, height=100,)
cam.pack()
camlab=Label(cam)
camlab.pack()

cap=cv2.VideoCapture(0)

def video_stream():
   
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow("Result", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


video_stream()

root.mainloop()