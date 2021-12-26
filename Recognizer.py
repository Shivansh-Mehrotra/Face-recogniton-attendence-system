from tkinter import *
import tkinter
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import cv2
from time import strftime
from datetime import datetime

class recognize:
    def __init__(self,window):

        # window
        self.window=window
        self.window.geometry("1530x790-0+0")
        self.window.state('zoomed')
        self.window.title("Recognizer")

        # Bg image
        bg=Image.open(r"C:\Users\mehro\Desktop\face recognition\face detect1.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        #heading
        heading=Label(self.window,text="Face Recognition",font=("times new roman",40,"bold"),bg="white",fg="darkgreen").place(x=0,y=5,relwidth=1)


        b1_1=Button(self.window,text="Recognize Face",command=self.face_recognitn,cursor="hand2",font=("times new roman",25,"bold"),bg='green',fg="white").place(x=0,y=390,width=1530,height=40)

    def attendance(self,data1,data2,data3,data4):
            with open("Attendance_Report.csv","r+",newline="\n") as f:
                mydata=f.readlines()
                list=[]
                for line in mydata:
                    data=line.split(',')
                    list.append(data[0])
                if data1 not in list and data2 not in list and data3 not in list and data4 not in list:
                    now=datetime.now()
                    dt=now.strftime("%d/%m/%Y")
                    tm=now.strftime("%I:%M:%S %p")
                    f.writelines(f"{data1},{data2},{data3},{data4},{tm},{dt},Present\n")

    def face_recognitn(self):
        def boundry(img,classifier,scalefactor,minneighbr,color,text,classifr):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,scalefactor,minneighbr)
            coordinate=[]
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=classifr.predict(gray_img[y:y+h,x:x+w])
                sure=int(100*(1-predict/300))

                try:
                    con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                    cur=con.cursor()

                    cur.execute("select First_Name,Last_Name from students where Id="+str(id))
                    data1=cur.fetchone()
                    data1=' '.join(data1)

                    cur.execute("select Course from students where Id="+str(id))
                    data2=cur.fetchone()
                    data2='+'.join(data2)

                    cur.execute("select Section from students where Id="+str(id))
                    data3=cur.fetchone()
                    data3='+'.join(data3)

                    cur.execute("select Id from students where Id="+str(id))
                    data4=cur.fetchone()
                    data4='+'.join(data4)


                except Exception as e:
                    messagebox.showerror("Error","Error due to "+str(e))

                if sure>77:
                    cv2.putText(img,f"Name : {data1}",(x,y-65),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
                    cv2.putText(img,f"Course : {data2}",(x,y-50),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
                    cv2.putText(img,f"Section : {data3}",(x,y-35),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
                    cv2.putText(img,f"Student Id : {data4}",(x,y-20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,0),2)
                    self.attendance(data1,data2,data3,data4)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),2)
                coordinate=[x,y,w,h]
            return coordinate
        
        def recognize(img,classifr,face):
            coords=boundry(img,face,1.1,10,(255,25,255),"Face",classifr)
            return img
        
        face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clasfr=cv2.face.LBPHFaceRecognizer_create()
        clasfr.read("classifier.xml")

        cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret,myimg=cam.read()
            myimg=recognize(myimg,clasfr,face)
            cv2.imshow("Welcome",myimg)
            if cv2.waitKey(1)==13:
                break
        cam.release()
        cv2.destroyAllWindows()

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=recognize(window)
    window.mainloop()