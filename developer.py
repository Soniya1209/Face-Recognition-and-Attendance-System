from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
# import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("face Recognition System")
        
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
        bg_img.place(x=0,y=130,width=1620,height=700)
        
        #title
        title_lbl=Label(bg_img,text="DEVELOPER", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        #main frame
        main_frame= Frame(bg_img,bd=2, bg='#1c195e')
        main_frame.place(x=50,y=50,width=500,height=650)



if __name__  == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()