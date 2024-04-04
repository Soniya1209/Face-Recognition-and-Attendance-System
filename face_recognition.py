from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import csv
import cv2
import os
import numpy as np



class Face_Recognition:
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
        title_lbl=Label(bg_img,text="FACE RECOGNITION", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        #button
        b1_1=Button(bg_img,text="Face Recognition",command=self.face_recog ,cursor="hand2",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        b1_1.place(x=680,y=380,width=200,height=40)
        
    #**************************Attendance******************************************
   

    # def mark_attendance(self, i, r, n, d):
    #     # Create a set to store existing names
    #     existing_names = set()

    #     # Read the existing attendance data
    #     with open("attendance.csv", "r", newline="\n") as file:
    #         csv_reader = csv.reader(file)
    #         for line in csv_reader:
    #             existing_names.update(line[:4])

    #     # Check if any of the provided names already exist in the set
    #     if i not in existing_names and r not in existing_names and n not in existing_names and d not in existing_names:
    #         now = datetime.now()
    #         d1 = now.strftime("%d/%m/%Y")
    #         dtString = now.strftime("%H:%M:%S")

    #         # Append new attendance only if none of the names exist in the set
    #         with open("attendance.csv", "a", newline="\n") as file:
    #             csv_writer = csv.writer(file)
    #             csv_writer.writerow([i, r, n, d, dtString, d1, "Present"])
    


    

    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r", newline="\n") as file:
            csv_reader = csv.reader(file)
            myDataList = list(csv_reader)
            name_list = [entry[:4] for entry in myDataList]

        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")

        new_entry = [i, r, n, d, dtString, d1, "Present"]

        # Check if the combination of names exists in the attendance file
        if [i, r, n, d] not in name_list:
            # If the combination of names does not exist, append the new entry
            with open("attendance.csv", "a", newline="\n") as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(new_entry)




    # def mark_attendance(self,i,r,n,d):
        
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDataList=f.readlines()
    #         name_list=[]
    #         for line in myDataList:
    #             entry=line.split((","))
    #             name_list.append(entry[0])
    #         if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
    #             now=datetime.now()
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%H:%M:%S")
    #             f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

                
        
    #**************** face recognition****************
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234",
                    database="face_recognizer",
                )
                
                my_cursor=conn.cursor()
                
                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchall()
                
                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchall()
                n = "+".join(str(item) for item in n)

                my_cursor.execute("select Roll_no from student where Student_Id="+str(id))
                r=my_cursor.fetchall()
                r = "+".join(str(item) for item in r)
                
                my_cursor.execute("select Dep from student where Student_Id="+str(id))
                d=my_cursor.fetchall()
                d = "+".join(str(item) for item in d)
                
                
                i = "+".join(str(item) for item in i)
                
                if confidence>75:
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord=[x,y,w,h]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

        
if __name__  == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()