from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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

        login_btn=Button(reg_frame,text="Go back to Login ",borderwidth=0,font=("Ubuntu",10,"bold"),width=70,bg="white",fg="#e0af43",activeforeground="#e0af43",activebackground="white")
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
            
        
         
        
if __name__  == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()