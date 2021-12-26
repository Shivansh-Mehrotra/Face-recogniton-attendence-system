import tkinter
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import cv2

class student:
    def __init__(self,window):

        # window
        self.window=window
        self.window.geometry("1530x790-0+0")
        self.window.state('zoomed')
        self.window.title("Student Details")

        # Bg image
        bg=Image.open(r"C:\Users\mehro\Desktop\face recognition\background.jpg")
        bg=bg.resize((1530,790),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        # top frame
        self.f1=Frame(self.window,bg="white")
        self.f1.place(x=0,y=10,relwidth=1,height=170)

        # top frame -> Heading
        heading=Label(self.f1,text="Add Students Details",font=("times new roman",40,"bold"),bg="white",fg="darkgreen").place(x=0,y=40,width=1530,height=40)


        # main frame
        self.f2=Frame(self.window,bg="white")
        self.f2.place(x=20,y=155,width=1485,height=650)
        
        # main frame -> left label frame
        self.left=LabelFrame(self.f2,relief=RIDGE,text="Course Details",font=("times new roman",12,"bold"),bg="white")
        self.left.place(x=10,y=180,width=600,height=580)

        # course label
        course=Label(self.left,text="Course",font=("times new roman",12,"bold"),bg="white")
        course.place(x=30,y=10)
        # course combo box
        self.course_cmb_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.course_cmb_bx['values']=("Select Course","B.Tech","Bsc","B.Com","BA")
        self.course_cmb_bx.place(x=100,y=10,width=150)
        self.course_cmb_bx.current(0)

        # department label
        dep=Label(self.left,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep.place(x=280,y=10)
        # department combo box
        self.dep_cmb_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.dep_cmb_bx['values']=("Select Department","CSE","ME","IT","CIVIL")
        self.dep_cmb_bx.place(x=390,y=10,width=150)
        self.dep_cmb_bx.current(0)

        # year label
        year=Label(self.left,text="Year",font=("times new roman",12,"bold"),bg="white")
        year.place(x=30,y=50)
        # year combo box
        self.year_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.year_bx['values']=("Select Year","First","Second","Third","Fourth")
        self.year_bx.place(x=100,y=50,width=150)
        self.year_bx.current(0)

        # semester label
        sem=Label(self.left,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem.place(x=280,y=50)
        # semester combo box
        self.sem_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.sem_bx['values']=("Select Semester","Odd","Even")
        self.sem_bx.place(x=390,y=50,width=150)
        self.sem_bx.current(0)

        # Fname
        first_name=Label(self.left,text="First Name",font=("times new roman",12,"bold"),bg="white")
        first_name.place(x=20,y=90)
        self.fname=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.fname.place(x=120,y=92,width=150)

        # lname
        last_name=Label(self.left,text="Last Name",font=("times new roman",12,"bold"),bg="white")
        last_name.place(x=280,y=90)
        self.lname=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.lname.place(x=390,y=92,width=150)

        # Studentid
        stud_id=Label(self.left,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        stud_id.place(x=20,y=130)
        self.studid=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.studid.place(x=120,y=132,width=150)

        # Section
        sectn=Label(self.left,text="Section",font=("times new roman",12,"bold"),bg="white")
        sectn.place(x=280,y=130)
        self.section=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.section.place(x=390,y=132,width=150)

        # gender label
        gendr=Label(self.left,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gendr.place(x=20,y=170)
        # gender combo box
        self.gender_cmb_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.gender_cmb_bx['values']=("Select Gender","Male","Female","Other")
        self.gender_cmb_bx.place(x=120,y=172,width=150)
        self.gender_cmb_bx.current(0)

        # univ roll no
        univrll=Label(self.left,text="Univ Roll No",font=("times new roman",12,"bold"),bg="white")
        univrll.place(x=280,y=170)
        self.univ_roll=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.univ_roll.place(x=390,y=172,width=150)

        # email
        email=Label(self.left,text="Email",font=("times new roman",12,"bold"),bg="white")
        email.place(x=20,y=210)
        self.email_id=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.email_id.place(x=120,y=212,width=150)

        # phone
        phn=Label(self.left,text="Phone",font=("times new roman",12,"bold"),bg="white")
        phn.place(x=280,y=210)
        self.phone=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.phone.place(x=390,y=212,width=150)

        # address
        addrss=Label(self.left,text="Address",font=("times new roman",12,"bold"),bg="white")
        addrss.place(x=20,y=250)
        self.address=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.address.place(x=120,y=252,width=420)

        # radio btn
        self.var=StringVar()
        self.rad=IntVar()
        self.radbtn1=ttk.Radiobutton(self.left,variable=self.rad,text="Take Photo",value=1)
        self.radbtn1.place(x=180,y=290)
        self.radbtn2=ttk.Radiobutton(self.left,variable=self.rad,text="Don't Take Photo",value=2)
        self.radbtn2.place(x=280,y=290)

        # bottom btn
        save=Button(self.left,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="green",fg="white",relief=RIDGE)
        save.place(x=100,y=330,width=70,height=30)

        update=Button(self.left,text="Update",command=self.update,font=("times new roman",12,"bold"),bg="yellow",fg="black",relief=RIDGE)
        update.place(x=200,y=330,width=70,height=30)

        Delete=Button(self.left,text="Delete",command=self.delete,font=("times new roman",12,"bold"),bg="red",fg="black",relief=RIDGE)
        Delete.place(x=300,y=330,width=70,height=30)

        Reset=Button(self.left,text="Reset",command=self.clear,font=("times new roman",12,"bold"),bg="skyblue",fg="black",relief=RIDGE)
        Reset.place(x=400,y=330,width=70,height=30)

        Takephtsample=Button(self.left,command=self.generate_data,text="Take Photo Sample",font=("times new roman",12,"bold"),bg="darkgreen",fg="white",relief=RIDGE)
        Takephtsample.place(x=110,y=370,width=340,height=30)

        # updatephtsample=Button(self.left,text="Update Photo Sample",font=("times new roman",12,"bold"),bg="darkgreen",fg="white",relief=RIDGE)
        # updatephtsample.place(x=290,y=370,width=160,height=30)

        # main frame -> right label frame
        self.right=LabelFrame(self.f2,relief=RIDGE,text="Search Records",font=("times new roman",12,"bold"),bg="white")
        self.right.place(x=635,y=180,width=610,height=430)

        # search label
        self.search=Label(self.right,text="Search By",font=("times new roman",12,"bold"),bg="lightblue",fg="black")
        self.search.place(x=10,y=10)
        self.search_cmb_bx=ttk.Combobox(self.right,font=("times new roman",12),state='readonly',justify=CENTER)
        self.search_cmb_bx['values']=("Select","Roll_No","Phone","First_Name","Id")
        self.search_cmb_bx.place(x=100,y=10,width=100)
        self.search_cmb_bx.current(0)
        self.srch_entry=Entry(self.right,font=("times new roman",15),bg="lightgrey")
        self.srch_entry.place(x=220,y=12,width=150)

        # searchbtn
        srch=Button(self.right,command=self.search_by,text="Search",font=("times new roman",12,"bold"),bg="green",fg="white",relief=RIDGE)
        srch.place(x=380,y=10,width=100,height=30)
        # showall
        shwal=Button(self.right,command=self.fetch_data,text="Show All",font=("times new roman",12,"bold"),bg="green",fg="white",relief=RIDGE)
        shwal.place(x=490,y=10,width=100,height=30)

        # detail frame   
        self.details=LabelFrame(self.right,relief=RIDGE,text="Records",font=("times new roman",12,"bold"),bg="white")
        self.details.place(x=13,y=40,width=580,height=355)

        # scrll bars
        scroll_x=ttk.Scrollbar(self.details,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.details,orient=VERTICAL)
        
        # table tree view
        self.table=ttk.Treeview(self.details,columns=("First Name","Last Name","Department","Course","Year","Semester","Id","Roll No","Section","Gender","Email","Phone","Address","Photo"),xscrollcommand=scroll_x,yscrollcommand=scroll_y) # these names are dummy
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.table.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.table.yview)

        self.table.heading("First Name",text="First Name") # first name is dummy
        self.table.heading("Last Name",text="Last Name")
        self.table.heading("Department",text="Department")
        self.table.heading("Course",text="Course")
        self.table.heading("Year",text="Year")
        self.table.heading("Semester",text="Semester")
        self.table.heading("Id",text="Id")
        self.table.heading("Roll No",text="Roll No")
        self.table.heading("Section",text="Section")
        self.table.heading("Gender",text="Gender")
        self.table.heading("Email",text="Email")
        self.table.heading("Phone",text="Phone")
        self.table.heading("Address",text="Address")
        self.table.heading("Photo",text="Photo")
        self.table["show"]="headings"

        self.table.column("First Name",width=100) #name is dummy
        self.table.column("Last Name",width=100)
        self.table.column("Department",width=100)
        self.table.column("Course",width=100)
        self.table.column("Year",width=100)
        self.table.column("Semester",width=100)
        self.table.column("Id",width=100)
        self.table.column("Roll No",width=100)
        self.table.column("Section",width=100)
        self.table.column("Gender",width=100)
        self.table.column("Email",width=100)
        self.table.column("Phone",width=100)
        self.table.column("Address",width=100)
        self.table.column("Photo",width=100)

        self.table.pack(fill=BOTH,expand=1)

        self.table.bind("<ButtonRelease>",self.click_record_see)

        self.fetch_data()
    
    #clear fields
    def clear(self):
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.section.delete(0,END)
        self.address.delete(0,END)
        self.phone.delete(0,END)
        self.email_id.delete(0,END)
        self.studid.delete(0,END)
        self.dep_cmb_bx.current(0)
        self.gender_cmb_bx.current(0)
        self.sem_bx.current(0)
        self.year_bx.current(0)
        self.course_cmb_bx.current(0)
        self.univ_roll.delete(0,END)
        self.rad.set(0)

    # search by
    def search_by(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            cur=con.cursor()
            cur.execute(f"select * from students where {self.search_cmb_bx.get()} = '{self.srch_entry.get()}'")
            row=cur.fetchall()
            if(len(row))!=0:
                self.table.delete(*self.table.get_children())
                for i in row:
                    self.table.insert("",END,values=i)
            else:
                messagebox.showinfo("Warning","No records Found")
            con.close()
        except Exception as e:
            print("Error due to : "+str(e))

    # add data to database
    def add_data(self):
        # validation 
        if self.course_cmb_bx.get()=="" or self.dep_cmb_bx.get()=="" or self.fname.get()=="" or self.lname.get()=="" or self.email_id.get()=="" or self.univ_roll.get()=="" or self.studid.get()=="" or self.gender_cmb_bx.get()=="" or self.year_bx=="" or self.section=="" or self.sem_bx=="" or self.phone=="" or self.address=="":
            messagebox.showerror("Error","All Fields Are Compulsary",parent=self.left)
        elif self.rad.get()==0:
            messagebox.showerror("Error","Please Select any Radio Button",parent=self.left)
        else:
            if self.rad.get()==1:
                self.var="Yes"
            elif self.rad.get()==2:
                self.var="No"
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                cur=con.cursor()
                cur.execute("select * from students where id=%s",self.studid.get())
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Student with same Id already exist.",parent=self.left)
                else:
                    cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.fname.get(),self.lname.get(),self.dep_cmb_bx.get(),self.course_cmb_bx.get(),self.year_bx.get(),self.sem_bx.get(),self.studid.get(),self.univ_roll.get(),self.section.get(),self.gender_cmb_bx.get(),self.email_id.get(),self.phone.get(),self.address.get(),self.var))
                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo("Success","Details Added Successfully",parent=self.left)
                    self.clear()
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.left)

    # fetch data
    def fetch_data(self):
        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
            cur=con.cursor()
            cur.execute("select * from students")
            row=cur.fetchall()

            if(len(row))!=0:
                self.table.delete(*self.table.get_children())
                for i in row:
                    self.table.insert("",END,values=i)
            con.close()
        except Exception as e:
            print("Error due to : "+str(e))

    # click pn table recors and see in entry fields to update
    def click_record_see(self,event=""):
        self.clear()
        cur=self.table.focus()
        content=self.table.item(cur)
        data=content["values"]
        self.fname.insert(0,data[0]),
        self.lname.insert(0,data[1]),
        self.dep_cmb_bx.set(data[2]),
        self.course_cmb_bx.set(data[3]),
        self.year_bx.set(data[4]),
        self.sem_bx.set(data[5]),
        self.studid.insert(0,data[6]),
        self.univ_roll.insert(0,data[7]),
        self.section.insert(0,data[8]),
        self.gender_cmb_bx.set(data[9]),
        self.email_id.insert(0,data[10]),
        self.phone.insert(0,data[11]),
        self.address.insert(0,data[12]),
        if data[13] == "Yes":
            self.rad.set(1)
        elif data[13] == "No":
            self.rad.set(2)

    # update function
    def update(self):
        # validation 
        if self.course_cmb_bx.get()=="" or self.dep_cmb_bx.get()=="" or self.fname.get()=="" or self.lname.get()=="" or self.email_id.get()=="" or self.univ_roll.get()=="" or self.studid.get()=="" or self.gender_cmb_bx.get()=="" or self.year_bx=="" or self.section=="" or self.sem_bx=="" or self.phone=="" or self.address=="":
            messagebox.showerror("Error","All Fields Are Compulsary",parent=self.left)
        elif self.rad.get()==0:
            messagebox.showerror("Error","Please Select any Radio Button",parent=self.left)
        else:
            if self.rad.get()==1:
                self.var="Yes"
            elif self.rad.get()==2:
                self.var="No"
            try:
                user=messagebox.askyesno("Update","Are you sure you want to update",parent=self.left)
                if user>0:
                    con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                    cur=con.cursor()
                    cur.execute("update students set First_Name=%s,Last_Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Section=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Id=%s",(self.fname.get(),self.lname.get(),self.dep_cmb_bx.get(),self.course_cmb_bx.get(),self.year_bx.get(),self.sem_bx.get(),self.univ_roll.get(),self.section.get(),self.gender_cmb_bx.get(),self.email_id.get(),self.phone.get(),self.address.get(),self.var,self.studid.get()))
                    con.commit()
                    self.fetch_data()
                    con.close()
                    messagebox.showinfo("Success","Details Updated Successfully",parent=self.left)
                    self.clear()
                else:
                    if not user:
                        return
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.left)

    # delete functn
    def delete(self):
        if self.studid=="":
            messagebox.showerror("Error","Student Id Required.",parent=self.left)
        else:
            try:
                user=messagebox.askyesno("Delete","Are you sure you want to delete.",parent=self.left)
                if user>0:
                    con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                    cur=con.cursor()
                    cur.execute("delete from students where id=%s",self.studid.get())
                    con.commit()
                    self.fetch_data()
                    con.close()
                    self.clear()
                    messagebox.showinfo("Success","Student's Details deleted successfully",parent=self.left)
                else:
                    if not user:
                        return
            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.left)

    # generate data set/take photo sample
    def generate_data(self):
        # validation 
        if self.course_cmb_bx.get()=="" or self.dep_cmb_bx.get()=="" or self.fname.get()=="" or self.lname.get()=="" or self.email_id.get()=="" or self.univ_roll.get()=="" or self.studid.get()=="" or self.gender_cmb_bx.get()=="" or self.year_bx=="" or self.section=="" or self.sem_bx=="" or self.phone=="" or self.address=="":
            messagebox.showerror("Error","All Fields Are Compulsary",parent=self.left)
        elif self.rad.get()==0:
            messagebox.showerror("Error","Please Select any Radio Button",parent=self.left)
        else:
            self.var="Yes"
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="face recognition")
                cur=con.cursor()
                cur.execute("select * from students")
                data=cur.fetchall()
                id=0
                for x in data:
                    id+=1
                cur.execute("update students set First_Name=%s,Last_Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Roll_No=%s,Section=%s,Gender=%s,Email=%s,Phone=%s,Address=%s,Photo=%s where Id=%s",(self.fname.get(),self.lname.get(),self.dep_cmb_bx.get(),self.course_cmb_bx.get(),self.year_bx.get(),self.sem_bx.get(),self.univ_roll.get(),self.section.get(),self.gender_cmb_bx.get(),self.email_id.get(),self.phone.get(),self.address.get(),self.var,self.studid.get()))
                con.commit()
                self.fetch_data()
                con.close()

                # loading predefined files from open cv2
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def crop_img(img):  # function to crop images.
                    # first we need to convert image to grayscale.
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5) # 1.3- scaling factor by default value || 5-minimum neighbour
                    for (x,y,w,h) in faces:
                        crop_img=img[y:y+h,x:x+w]
                        return crop_img
                # cap=cv2.VideoCapture(0) # for web camera use zero and for others use 1
                cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                imgid=0
                while True:
                    ret,myimg=cap.read()
                    if crop_img(myimg) is not None:
                        imgid+=1
                        pic=cv2.resize(crop_img(myimg),(450,450))
                        pic=cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
                        file='PhotosSample/user.'+str(self.studid.get())+'.'+str(imgid)+'.jpg'
                        cv2.imwrite(file,pic)
                        cv2.putText(pic,str(imgid),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),3)
                        cv2.imshow('Croped Face',pic)
                    if cv2.waitKey(1)==13 or int(imgid)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.clear()
                messagebox.showinfo("Result","Generating Dataset",parent=self.left)

            except Exception as e:
                messagebox.showerror("Error",f"Error due to {str(e)}",parent=self.left)

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=student(window)
    window.mainloop()