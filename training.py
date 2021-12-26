from tkinter import *
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import cv2
import os
import numpy as np

class Trainng:
    def __init__(self,window):
        # window
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.title("Train Data")

        # Bg image
        bg=Image.open(r"C:\Users\mehro\Desktop\face recognition\pattern train.png")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
        # heading
        heading=Label(self.window,text="Training Data",font=("times new roman",40,"bold"),bg="white",fg="darkblue").place(x=0,y=0,relwidth=1)
        # training btn
        b1=Button(self.window,command=self.training,cursor="hand2").place(x=0,y=380,width=1530,height=60)
        b1_1=Button(self.window,text="Click Here To Train",command=self.training,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="red").place(x=0,y=380,width=1530,height=60)

  
        # bottom img
        img=Image.open(r"C:\Users\mehro\Desktop\face recognition\photos.jpg")
        img=img.resize((1280,200),Image.ANTIALIAS)
        self.img=ImageTk.PhotoImage(img)
        imglbl=Label(self.window,image=self.img).place(x=0,y=65,relwidth=1,height=320)

    def training(self):
        data_folder=('PhotosSample')
        path=[ os.path.join(data_folder,file) for file in os.listdir(data_folder)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') # converting into grayscale image
            imgnp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imgnp)
            ids.append(id)
            cv2.imshow("Training",imgnp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # training the classifier
        classifr=cv2.face.LBPHFaceRecognizer_create()
        classifr.train(faces,ids)
        classifr.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Successful!!!",parent=self.window)

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=Trainng(window)
    window.mainloop()