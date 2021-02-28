
# coding: utf-8

# In[2]:


from tkinter import *

f = open('output_modified.txt')
text_msg = f.readlines()
#create button to perform an action
root = Tk()
root.geometry('200x200')
lab = Label(root)
lab.grid(row=0,column=25)

def onclick():
    l = Label(root,text=text_msg)
    l.grid(row=100,column=150)
    #l.config(anchor=CENTER)
    #l.pack()
    
bt1 = Button(root, text='Click here to translate!', command=onclick, fg='green', bg='red') #callback
bt1.place(relx=0.5, rely=0.5, anchor=CENTER)
#bt1.place(relx=0, rely=0, anchor=CENTER)
#bt1.grid(row=0,column=20)
root.mainloop()

