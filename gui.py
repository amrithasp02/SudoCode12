import cv2

from tkinter import *
from tkinter import ttk
from PIL import *
root=Tk()
root.geometry('1080x720')
root.config(bg="#CCCCCC")
root.title("SUDOCODE")

label=Label(root, text="ASL to Text Converter", font = "arial 20 bold",bg='#808080')
label.pack()

def video_stream():
    
   
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        cv2.imshow("Result", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


vid_btn=Button(root,text="Enable Webcam",command=video_stream, bg = "#808080")
vid_btn.place(x = 540, y= 620)


cam=Frame(root, bg="white", width=100, height=100,)
cam.pack()
camlab=Label(cam)
camlab.pack()

cap=cv2.VideoCapture(0)

f = open('output_modified.txt')
text_msg = f.readlines()


def onclick():
    l = Label(root,text=text_msg)
    l.grid(row=100,column=150)

trans_btn=Button(root,text="Translate",command=onclick, bg = "#808080")
trans_btn.place(x = 540, y= 680)

root.mainloop()











