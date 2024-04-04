from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("Face Recognition System")
        
        #1st image
        img=Image.open(r"Photos\logo.png")
        img=img.resize((300,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=300,height=130)
        
         #2nd image
        img1=Image.open(r"Photos\top.jpeg")
        img1=img1.resize((1300,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=300,y=0,width=1300,height=130)
          
        #bg image
        img3=Image.open(r"Photos\dev_bg.jpg")
        img3=img3.resize((1620,890),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1620,height=890)
        
        #title
        title_lbl=Label(bg_img,text="FACE RECOGNITION AND ATTENDANCE SYSTEM SOFTWARE", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        def time():
            string= strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl=Label(title_lbl,font=("Ubuntu",20),bg="#1c195e",fg="#e0af43")
        lbl.place(x=10,y=0,width=150,height=30)
        time()
            
        
        # Student Button
        btn1=Image.open(r"Photos\student.jpeg")
        btn1=btn1.resize((200,180),Image.LANCZOS)
        self.photobtn1=ImageTk.PhotoImage(btn1)

        b1=Button(bg_img,image=self.photobtn1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=180)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=200,y=280,width=200,height=40)
        
         # Detect face Button
        btn2=Image.open(r"Photos\face.jpeg")
        btn2=btn2.resize((200,180),Image.LANCZOS)
        self.photobtn2=ImageTk.PhotoImage(btn2)

        b1=Button(bg_img,image=self.photobtn2,command=self.face_data,cursor="hand2")
        b1.place(x=480,y=100,width=200,height=180)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=480,y=280,width=200,height=40)
        
        # Attendance  Button
        btn3=Image.open(r"Photos\attendance.png")
        btn3=btn3.resize((200,180),Image.LANCZOS)
        self.photobtn3=ImageTk.PhotoImage(btn3)

        b1=Button(bg_img,image=self.photobtn3,command=self.attd_data,cursor="hand2")
        b1.place(x=760,y=100,width=200,height=180)
        
        b1_1=Button(bg_img,text="Attendance",command=self.attd_data,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=760,y=280,width=200,height=40)
        
        # # Help Desk Button
        # btn4=Image.open(r"Photos\help.jpeg")
        # btn4=btn4.resize((200,180),Image.LANCZOS)
        # self.photobtn4=ImageTk.PhotoImage(btn4)

        # b1=Button(bg_img,image=self.photobtn4,cursor="hand2")
        # b1.place(x=1040,y=100,width=200,height=180)
        
        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        # b1_1.place(x=1040,y=280,width=200,height=40)
        
        # Train face Button
        btn5=Image.open(r"Photos\train.png")
        btn5=btn5.resize((200,180),Image.LANCZOS)
        self.photobtn5=ImageTk.PhotoImage(btn5)

        b1=Button(bg_img,image=self.photobtn5,command=self.train_data,cursor="hand2")
        b1.place(x=200,y=380,width=200,height=180)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=200,y=560,width=200,height=40)
        
        # Photos  Button
        btn6=Image.open(r"Photos\photos.jpeg")
        btn6=btn6.resize((200,180),Image.LANCZOS)
        self.photobtn6=ImageTk.PhotoImage(btn6)

        b1=Button(bg_img,image=self.photobtn6,cursor="hand2",command=self.open_img)
        b1.place(x=480,y=380,width=200,height=180)
        
        b1_1=Button(bg_img,text="Photos ",cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43",command=self.open_img)
        b1_1.place(x=480,y=560,width=200,height=40)
        
        # # Developer Button
        # btn7=Image.open(r"Photos\dev.jpeg")
        # btn7=btn7.resize((200,180),Image.LANCZOS)
        # self.photobtn7=ImageTk.PhotoImage(btn7)

        # b1=Button(bg_img,image=self.photobtn7,cursor="hand2")
        # b1.place(x=760,y=380,width=200,height=180)
        
        # b1_1=Button(bg_img,text="Developer ",cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        # b1_1.place(x=760,y=560,width=200,height=40)
        
        # Exit Button
        btn8=Image.open(r"Photos\exit.jpeg")
        btn8=btn8.resize((200,180),Image.LANCZOS)
        self.photobtn8=ImageTk.PhotoImage(btn8)

        b1=Button(bg_img,image=self.photobtn8,command=self.iExit,cursor="hand2")
        b1.place(x=760,y=380,width=200,height=180)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=760,y=560,width=200,height=40)
        
    def open_img(self):
        os.startfile("data")
        
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("!!!","Do you want to exit ?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return


    #********************function buttons************
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
        
    def attd_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)













if __name__  == "__main__":
    root=Tk()
    obj=face_Recognition_System(root)
    root.mainloop()
    
    