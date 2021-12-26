from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox,filedialog
import pymysql
import os
import csv
import tkinter

mydata=[]

class Attendance:
    def __init__(self,window):

        # window
        self.window=window
        self.window.geometry("1280x720-0+0")
        self.window.state('zoomed')
        self.window.title("Student Details")

        # Bg image
        bg=Image.open(r"C:\Users\mehro\Desktop\face recognition\att3.jpg")
        bg=bg.resize((1280,720),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)
        bglbl=Label(self.window,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)

        # top frame
        self.f1=Frame(self.window,bg="green")
        self.f1.place(x=0,y=10,relwidth=1,height=170)
        
        
        # top frame -> Heading
        heading=Label(self.f1,text="Attendance Report",font=("times new roman",40,"bold"),bg="white",fg="darkgreen").place(x=550,y=40)


        # main frame
        self.f2=Frame(self.window,bg="white")
        self.f2.place(x=20,y=200,width=1485,height=670)
        
        # main frame -> left label frame
        self.left=LabelFrame(self.f2,relief=RIDGE,text="Student Report",font=("times new roman",12,"bold"),bg="white")
        self.left.place(x=10,y=10,width=600,height=580)

        # Name
        name=Label(self.left,text="Name",font=("times new roman",12,"bold"),bg="white")
        name.place(x=20,y=50)
        self.fname=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.fname.place(x=120,y=52,width=150)

        # Student Id
        stud_id=Label(self.left,text="Student Id",font=("times new roman",12,"bold"),bg="white")
        stud_id.place(x=280,y=50)
        self.studid=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.studid.place(x=390,y=52,width=150)

        # Course
        course=Label(self.left,text="Course",font=("times new roman",12,"bold"),bg="white")
        course.place(x=20,y=90)
        self.corse=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.corse.place(x=120,y=92,width=150)

        # Section
        sectn=Label(self.left,text="Section",font=("times new roman",12,"bold"),bg="white")
        sectn.place(x=280,y=90)
        self.section=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.section.place(x=390,y=92,width=150)

        # Time
        time=Label(self.left,text="Time",font=("times new roman",12,"bold"),bg="white")
        time.place(x=20,y=130)
        self.times=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.times.place(x=120,y=132,width=150)

        # Date
        date=Label(self.left,text="Date",font=("times new roman",12,"bold"),bg="white")
        date.place(x=280,y=130)
        self.dates=Entry(self.left,font=("times new roman",12),bg="lightgrey")
        self.dates.place(x=390,y=132,width=150)


        # attendance label
        status=Label(self.left,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        status.place(x=140,y=180)
        # attendance box
        self.status_cmb_bx=ttk.Combobox(self.left,font=("times new roman",12),state='readonly',justify=CENTER)
        self.status_cmb_bx['values']=("Status","Present","Absent")
        self.status_cmb_bx.place(x=280,y=182,width=150)
        self.status_cmb_bx.current(0)

        # bottom btn
        importcsv=Button(self.left,command=self.imprt_csv,text="Import CSV",font=("times new roman",12,"bold"),bg="green",fg="white",relief=RIDGE)
        importcsv.place(x=80,y=240,width=110,height=30)

        exportcsv=Button(self.left,command=self.exprt_csv,text="Export CSV",font=("times new roman",12,"bold"),bg="yellow",fg="black",relief=RIDGE)
        exportcsv.place(x=220,y=240,width=110,height=30)

        Reset=Button(self.left,command=self.clear,text="Reset",font=("times new roman",12,"bold"),bg="skyblue",fg="black",relief=RIDGE)
        Reset.place(x=360,y=240,width=110,height=30)

        # record frame   
        self.details=LabelFrame(self.f2,relief=RIDGE,text="All Records",font=("times new roman",12,"bold"),bg="white")
        self.details.place(x=625,y=5,width=625,height=430)

        # scrll bars
        scroll_x=ttk.Scrollbar(self.details,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(self.details,orient=VERTICAL)
        
        # table tree view
        self.table=ttk.Treeview(self.details,columns=("Name","Course","Section","Id","Time","Date","Status"),xscrollcommand=scroll_x,yscrollcommand=scroll_y) # these names are dummy
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.table.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.table.yview)

        self.table.heading("Name",text="Name") # first name is dummy
        self.table.heading("Course",text="Course")
        self.table.heading("Id",text="Id")
        self.table.heading("Section",text="Section")
        self.table.heading("Status",text="Status")
        self.table.heading("Date",text="Date")
        self.table.heading("Time",text="Time")
        self.table["show"]="headings"

        self.table.column("Name",width=100) #name is dummy
        self.table.column("Course",width=100)
        self.table.column("Id",width=100)
        self.table.column("Section",width=100)
        self.table.column("Status",width=100)
        self.table.column("Date",width=100)
        self.table.column("Time",width=100)

        self.table.pack(fill=BOTH,expand=1)

        self.table.bind("<ButtonRelease>",self.click_record_see)

    # fetch data
    def fetch_data(self,rows):
        self.table.delete(*self.table.get_children())
        for i in rows:
            self.table.insert("",END,values=i)

    # import csv
    def imprt_csv(self):
        global mydata
        mydata.clear()
        flnm=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.window)
        with open(flnm) as mf:
            csvrd=csv.reader(mf,delimiter=",")
            for i in csvrd:
                mydata.append(i)
            self.fetch_data(mydata)

    # export csv
    def exprt_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No data Found",parent=self.window)
                return False
            flnm=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.window)
            with open(flnm,"w",newline="\n") as f:
                exprtwrite=csv.writer(f,delimiter=",")
                for i in mydata:
                    exprtwrite.writerow(i)
                messagebox.showinfo("Success","Data Exported Successfully")
        
        except Exception as e:
            messagebox.showerror("Error","Error due to "+str(e))

    #clear fields
    def clear(self):
        self.fname.delete(0,END)
        self.section.delete(0,END)
        self.studid.delete(0,END)
        self.corse.delete(0,END)
        self.times.delete(0,END)
        self.dates.delete(0,END)
        self.status_cmb_bx.current(0)

    # click pn table recors and see in entry fields to update
    def click_record_see(self,event=""):
        self.clear()
        cur=self.table.focus()
        content=self.table.item(cur)
        data=content["values"]
        self.fname.insert(0,data[0]),
        self.corse.insert(0,data[1]),
        self.studid.insert(0,data[3]),
        self.section.insert(0,data[2]),
        self.status_cmb_bx.set(data[6]),
        self.times.insert(0,data[4]),
        self.dates.insert(0,data[5])

    # to exit
    def windexit(self):
        self.windexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit ? ",parent=self.window)
        if self.windexit>0:
            self.window.destroy()
        else:
            return

if __name__=="__main__":
    window=Tk()
    ob=Attendance(window)
    window.mainloop()