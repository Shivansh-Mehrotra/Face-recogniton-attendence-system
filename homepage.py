from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk
from student import student
from training import Trainng
from Recognizer import recognize
from attendance import Attendance
import os

class face_recognition:
    def __init__(self,window):

        # window
        self.window=window
        self.window.geometry("1530x790-0+0")
        self.window.state('zoomed')
        self.window.title("Face Recognition Attendance System")
        
        # Bg image
        bg=Image.open(r"C:\Users\mehro\Desktop\face recognition\background.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        # top frame
        self.f1=Frame(self.window,bg="white")
        self.f1.place(x=0,y=40,relwidth=1,height=150)
        
        # top frame -> Heading
        heading=Label(self.f1,text="Face Recognition Attendance System",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=380,y=20)
        

        # Buttons
        # Student_Detail_Button
        btn_img1=Image.open(r"C:\Users\mehro\Desktop\face recognition\random 2.jpg")
        btn_img1=btn_img1.resize((220,220),Image.ANTIALIAS)
        self.btn_img1=ImageTk.PhotoImage(btn_img1)
        b1=Button(self.window,image=self.btn_img1,cursor="hand2",command=self.student_detail).place(x=200,y=250,width=220,height=220)
        b1_1=Button(self.window,text="Student Detail",cursor="hand2",command=self.student_detail,font=("times new roman",15,"bold"),fg="red").place(x=200,y=450,width=220,height=40)

        # Detect_Image_Button
        btn_img2=Image.open(r"C:\Users\mehro\Desktop\face recognition\face recognition.jpg")
        btn_img2=btn_img2.resize((220,220),Image.ANTIALIAS)
        self.btn_img2=ImageTk.PhotoImage(btn_img2)
        b2=Button(self.window,image=self.btn_img2,command=self.recognize_window,cursor="hand2").place(x=650,y=250,width=220,height=220)
        b2_2=Button(self.window,text="Recognize Face",command=self.recognize_window,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=650,y=450,width=220,height=40)

        # Attendance_Button
        btn_img3=Image.open(r"C:\Users\mehro\Desktop\face recognition\attendence.jpg")
        btn_img3=btn_img3.resize((220,220),Image.ANTIALIAS)
        self.btn_img3=ImageTk.PhotoImage(btn_img3)
        b3=Button(self.window,image=self.btn_img3,command=self.attendance_window,cursor="hand2").place(x=1100,y=250,width=220,height=220)
        b3_3=Button(self.window,text="Attendance",command=self.attendance_window,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=1100,y=450,width=220,height=40)

        # Train_Data_Button
        btn_img4=Image.open(r"C:\Users\mehro\Desktop\face recognition\model train.jpg")
        btn_img4=btn_img4.resize((220,220),Image.ANTIALIAS)
        self.btn_img4=ImageTk.PhotoImage(btn_img4)
        b4=Button(self.window,image=self.btn_img4,command=self.training_window,cursor="hand2").place(x=200,y=500,width=220,height=220)
        b4_4=Button(self.window,text="Train Data",command=self.training_window,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=200,y=700,width=220,height=40)

        # Photos_Button
        btn_img5=Image.open(r"C:\Users\mehro\Desktop\face recognition\photos.jpg")
        btn_img5=btn_img5.resize((220,220),Image.ANTIALIAS)
        self.btn_img5=ImageTk.PhotoImage(btn_img5)
        b5=Button(self.window,image=self.btn_img5,command=self.open_photos,cursor="hand2").place(x=650,y=500,width=220,height=220)
        b5_5=Button(self.window,text="Photos",command=self.open_photos,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=650,y=700,width=220,height=40)

        # Exit_Button
        btn_img6=Image.open(r"C:\Users\mehro\Desktop\face recognition\exit.jpg")
        btn_img6=btn_img6.resize((220,220),Image.ANTIALIAS)
        self.btn_img6=ImageTk.PhotoImage(btn_img6)
        b6=Button(self.window,image=self.btn_img6,command=self.windexit,cursor="hand2").place(x=1100,y=500,width=220,height=220)
        b6_6=Button(self.window,text="Exit",command=self.windexit,cursor="hand2",font=("times new roman",15,"bold"),fg="red").place(x=1100,y=700,width=220,height=40)

    # to open student window
    def student_detail(self):
        self.new_window=Toplevel(self.window)
        self.new=student(self.new_window)

    # to open training window
    def training_window(self):
        self.new_window=Toplevel(self.window)
        self.new=Trainng(self.new_window)

    # to open recognize window
    def recognize_window(self):
        self.new_window=Toplevel(self.window)
        self.new=recognize(self.new_window)

    # to open attendance window
    def attendance_window(self):
        self.new_window=Toplevel(self.window)
        self.new=Attendance(self.new_window)

    # to open photos folder
    def open_photos(self):
        os.startfile("PhotosSample")

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ")
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=face_recognition(window)
    window.mainloop()