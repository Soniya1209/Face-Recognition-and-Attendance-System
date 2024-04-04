from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
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
        img3=Image.open(r"Photos\bg.png")
        img3=img3.resize((1620,890),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1620,height=890)
        
        #title
        title_lbl=Label(bg_img,text="TRAIN DATA SET", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        # Train face Button
        btn5=Image.open(r"Photos\train.png")
        btn5=btn5.resize((200,180),Image.LANCZOS)
        self.photobtn5=ImageTk.PhotoImage(btn5)

        b1=Button(bg_img,image=self.photobtn5,command=self.train_classfier,cursor="hand2")
        b1.place(x=680,y=200,width=200,height=180)
        
        b1_1=Button(bg_img,text="Train Data",command=self.train_classfier,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=680,y=380,width=200,height=40)
        
        
    def train_classfier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image
            #img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
        
        #*********************** Train the classifier and save****************************
        clf = cv2.face.LBPHFaceRecognizer_create()


        # clf=cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")




if __name__  == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()