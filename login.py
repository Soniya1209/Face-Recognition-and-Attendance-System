from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os



def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()
    
    
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("Login")
        
        ##bg image
        img3=Image.open(r"Photos\bg.png")
        img3=img3.resize((1620,890),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1620,height=890)
        
        #main frame
        main_frame= Frame(bg_img,bg="white")
        main_frame.place(x=350,y=150,width=780,height=450)
        
        #left frame
        left_frame=Frame(main_frame,)
        left_frame.place(x=0,y=0,width=390,height=450)
        
        img4=Image.open(r"Photos\login.png")
        img4=img4.resize((390,450),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(left_frame,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=390,height=450)
        
        #right frame
        rigth_frame=Frame(main_frame,bg="white")
        rigth_frame.place(x=390,y=0,width=390,height=450)
        
        #login frame
        login_frame= Frame(rigth_frame,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=10,y=70,width=350,height=300)
        
        title=Label(rigth_frame,text=" LOG IN ", font=("Ubuntu",20,"bold"),bg="white",fg="#1c195e")
        title.place(x=130,y=55,width=100, height=35)
        
        #username
        username_lbl=Label(login_frame,text="Username",font=("Ubuntu",10,"bold"),bg="white",fg="#1c195e")
        username_lbl.place(x=7,y=30,width=120,height=15)
        
        self.txt_user=ttk.Entry(login_frame,font=("Ubuntu",13,"bold"))
        self.txt_user.place(x=35,y=55,width=250,height=30)
        
        #pwd
        pwd_lbl=Label(login_frame,text="Password",font=("Ubuntu",10,"bold"),bg="white",fg="#1c195e")
        pwd_lbl.place(x=7,y=100,width=120,height=15)
        
        self.txt_pwd=ttk.Entry(login_frame,font=("Ubuntu",13,"bold"))
        self.txt_pwd.place(x=35,y=135,width=250,height=30)
        
        #Buttons
        login_btn=Button(login_frame,text="Sign In",command=self.login,font=("Ubuntu",10,"bold"),width=70,bg="#e0af43",fg="#1c195e",activeforeground="#e0af43",activebackground="#1c195e")
        login_btn.place(x=140,y=180,width=70,height=30)
        
        #register button
        reg_btn=Button(login_frame,text="New User",command=self.register_window,borderwidth=0,font=("Ubuntu",10,"bold"),width=70,bg="white",fg="#e0af43",activeforeground="#e0af43",activebackground="white")
        reg_btn.place(x=13,y=225,width=120,height=15)
        
        #register button
        forgot_btn=Button(login_frame,text="Forgot Password",command=self.forgot_password_window,borderwidth=0,font=("Ubuntu",10,"bold"),width=70,bg="white",fg="#e0af43",activeforeground="#e0af43",activebackground="white")
        forgot_btn.place(x=35,y=245,width=120,height=15)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
    def login(self):
        if (self.txt_user.get()=="" or self.txt_pwd.get()==""):
            messagebox.showerror("Error","All fields required")
        else:
            if self.txt_user.get()=="soniya"  and self.txt_pwd.get()=="1234":
                messagebox.showinfo("Success","Successful")
            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and pwd=%s",(
                    self.txt_user.get(),
                    self.txt_pwd.get()
                ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid username or password")
                else:
                    open_main=messagebox.askyesno("YesNo","Access only admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.new_window)
                        self.app=face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()
                
    # ******************* reset password ************************
    def reset_password(self):
        if self.sec_ques.get()=="":
            messagebox.showerror("Error","Select security question")
        elif self.sec_ans=="":
            messagebox.showerror("Error","Enter security answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="SHB*#4017",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and ques=%s and ans=%s",(
                self.txt_user.get(),
                self.sec_ques.get(),
                self.sec_ans.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please entern correct answer")
            else:
                value=(self.txt_newpass.get(),self.txt_user.get())
                my_cursor.execute("update register set pwd=%s where email=%s",value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been updated")
        

    def forgot_password_window(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Enter Username to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txt_user.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Invalid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("550x550+610+170")

                l=Label(self.root2,text="Forgot Password",font=("Ubuntu",20,"bold"),bg="white",fg="#1c195e")
                l.place(x=0,y=10,relwidth=1)
                
                #security question  
                sec_ques_lbl=Label(self.root2,text="Security Question",font=("Ubuntu",13,"bold"),fg="#1c195e")
                sec_ques_lbl.place(x=200,y=80,width=250,height=20)
                
                self.sec_ques=ttk.Combobox(self.root2,font=("Ubuntu",15,"bold"),width=250,state="read only")
                self.sec_ques["values"]=("","Your birth place","Your pet name","Your first school")
                self.sec_ques.current(0)
                self.sec_ques.place(x=200,y=120,width=250,height=30)
                
                #security answer  
                sec_ans_lbl=Label(self.root2,text="Security Answer",font=("Ubuntu",13,"bold"),fg="#1c195e")
                sec_ans_lbl.place(x=200,y=160,width=250,height=20)

                self.sec_ans=ttk.Entry(self.root2,width=250,font=("Ubuntu",13,"bold"))
                self.sec_ans.place(x=200,y=200,width=250,height=30)
                
                #New Password
                new_pass_lbl=Label(self.root2,text="New Password",font=("Ubuntu",13,"bold"),fg="#1c195e")
                new_pass_lbl.place(x=200,y=240,width=250,height=20)

                self.txt_newpass=ttk.Entry(self.root2,width=250,font=("Ubuntu",13,"bold"))
                self.txt_newpass.place(x=200,y=280,width=250,height=30)
                
                btn=Button(self.root2,text="Reset",command= self.reset_password,font=("Ubuntu",13,"bold"),bg="#1c195e",fg="white")
                btn.place(x=200,y=350)
                

                
                
                
        
                
                
                
                
                
class Register:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("Register")
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_ques=StringVar()
        self.var_ans=StringVar()
        self.var_pwd=StringVar()
        self.var_confPwd=StringVar()
        
        ##bg image
        img3=Image.open(r"Photos\bg.png")
        img3=img3.resize((1620,890),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1620,height=890)
        
        #main frame
        main_frame= Frame(bg_img,bg="white")
        main_frame.place(x=200,y=25,width=1080,height=700)
        
        #left frame
        left_frame=Frame(main_frame,)
        left_frame.place(x=0,y=125,width=390,height=450)
        
        
        img4=Image.open(r"Photos\login.png")
        img4=img4.resize((390,450),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(left_frame,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=390,height=450)
        
        #right frame
        rigth_frame=Frame(main_frame,bg="white")
        rigth_frame.place(x=390,y=0,width=790,height=700)
 
        #login frame
        reg_frame= Frame(rigth_frame,bd=4,relief=RIDGE,bg="white")
        reg_frame.place(x=0,y=40,width=680,height=650)
        
        title=Label(rigth_frame,text=" Registration Form ", font=("Ubuntu",20,"bold"),bg="white",fg="#1c195e")
        title.place(x=200,y=25,width=300, height=35)
        
        #First name  
        fname_lbl=Label(reg_frame,text="First Name",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        fname_lbl.place(x=20,y=50,width=100,height=20)

        self.fname=ttk.Entry(reg_frame,textvariable=self.var_fname,width=250,font=("Ubuntu",13,"bold"))
        self.fname.place(x=20,y=90,width=250,height=30)
        
        #laast name  
        lname_lbl=Label(reg_frame,text="Last Name",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        lname_lbl.place(x=330,y=50,width=100,height=20)

        self.lname=ttk.Entry(reg_frame,textvariable=self.var_lname,width=250,font=("Ubuntu",13,"bold"))
        self.lname.place(x=330,y=90,width=250,height=30)
        
        #contact  
        contact_lbl=Label(reg_frame,text="Contact",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        contact_lbl.place(x=10,y=130,width=100,height=20)

        self.contact=ttk.Entry(reg_frame,textvariable=self.var_contact,width=250,font=("Ubuntu",13,"bold"))
        self.contact.place(x=20,y=160,width=250,height=30)
        
        #email  
        email_lbl=Label(reg_frame,text="Email",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        email_lbl.place(x=310,y=130,width=100,height=20)

        self.email=ttk.Entry(reg_frame,textvariable=self.var_email,width=250,font=("Ubuntu",13,"bold"))
        self.email.place(x=330,y=160,width=250,height=30)
               
        #security question  
        sec_ques_lbl=Label(reg_frame,text="Security Question",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        sec_ques_lbl.place(x=15,y=200,width=170,height=20)
        
        self.sec_ques=ttk.Combobox(reg_frame,textvariable=self.var_ques,font=("Ubuntu",13,"bold"),width=250,state="read only")
        self.sec_ques["values"]=("","Your birth place","Your pet name","Your first school")
        self.sec_ques.current(0)
        self.sec_ques.place(x=23,y=240,width=250,height=30)
        
        #security answer  
        sec_ans_lbl=Label(reg_frame,text="Security Answer",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        sec_ans_lbl.place(x=315,y=200,width=170,height=20)

        self.sec_ans=ttk.Entry(reg_frame,textvariable=self.var_ans,width=250,font=("Ubuntu",13,"bold"))
        self.sec_ans.place(x=330,y=240,width=250,height=30)
        
        #password  
        pwd_lbl=Label(reg_frame,text="Password",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        pwd_lbl.place(x=20,y=280,width=100,height=20)

        self.pwd=ttk.Entry(reg_frame,textvariable=self.var_pwd,width=250,font=("Ubuntu",13,"bold"))
        self.pwd.place(x=20,y=320,width=250,height=30)
        
        #confirm password  
        conf_pwd_lbl=Label(reg_frame,text="Confirm Password",font=("Ubuntu",13,"bold"),bg="white",fg="#1c195e")
        conf_pwd_lbl.place(x=330,y=280,width=150,height=20)

        self.conf_pwd=ttk.Entry(reg_frame,textvariable=self.var_confPwd,width=250,font=("Ubuntu",13,"bold"))
        self.conf_pwd.place(x=330,y=320,width=250,height=30)
        
        #Buttons
        reg_btn=Button(reg_frame,text="Register",command=self.register_data,font=("Ubuntu",10,"bold"),width=70,bg="#e0af43",fg="#1c195e",activeforeground="#e0af43",activebackground="#1c195e")
        reg_btn.place(x=270,y=380,width=90,height=35)

        login_btn=Button(reg_frame,text="Go back to Login ",command=self.Login,borderwidth=0,font=("Ubuntu",10,"bold"),width=70,bg="white",fg="#e0af43",activeforeground="#e0af43",activebackground="white")
        login_btn.place(x=13,y=450,width=120,height=18)
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_ques=="" or self.var_ans.get()=="":
            messagebox.showerror("Error","All fiels are required")
        elif self.var_pwd.get()!= self.var_confPwd.get():
            messagebox.showerror("Error","Password and confirm password are not same")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
            my_cursor=conn.cursor()
            query= ("Select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email already exists")
            else:
                my_cursor.execute("Insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_ques.get(),
                        self.var_ans.get(),
                        self.var_pwd.get(),
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registration successful")

               
    def Login(self):
        self.new_window=Toplevel(self.root)
        self.app=login_window(self.new_window)
 

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
    main()