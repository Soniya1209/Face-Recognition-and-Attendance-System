from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("face Recognition System")
        
        #********************** variables**************************
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        

        
        
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        #main frame
        main_frame= Frame(bg_img,bd=2)
        main_frame.place(x=50,y=50,width=1420,height=580)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Ubuntu",17,"bold"),bg="#1c195e",fg="#e0af43")
        left_frame.place(x=10,y=10,width=690,height=560)
        
        #current course
        cur_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        cur_course_frame.place(x=5,y=20,width=680,height=130)
        
        #department combo box
        dep_lbl=Label(cur_course_frame,text="Department",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_dep,font=("Ubuntu",13,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Course combo box
        course_lbl=Label(cur_course_frame,text="Course",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_course,font=("Ubuntu",13,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","BCA","B.Tech","MCA","M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Year combo box
        year_lbl=Label(cur_course_frame,text="Year",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_year,font=("Ubuntu",13,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020","2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Semester combo box
        sem_lbl=Label(cur_course_frame,text="Semester",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        sem_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_sem,font=("Ubuntu",13,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","I","II","III","IV")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
        
        #Class Student Information
        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        class_student_frame.place(x=5,y=150,width=680,height=350)
        
        #Student ID 
        stdId_lbl=Label(class_student_frame,text="Student Id",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        stdId_lbl.grid(row=0,column=0,padx=10,sticky=W)

        stdId_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("Ubuntu",13,"bold"))
        stdId_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Student name 
        stdName_lbl=Label(class_student_frame,text="Name",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        stdName_lbl.grid(row=0,column=2,padx=10,sticky=W)

        stdName_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("Ubuntu",13,"bold"))
        stdName_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Class Division 
        classDiv_lbl=Label(class_student_frame,text="Class Division",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        classDiv_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        classDiv_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("Ubuntu",13,"bold"),width=17,state="read only")
        classDiv_combo["values"]=("A","B","C")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Roll NO 
        rollNo_lbl=Label(class_student_frame,text="Roll NO",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        rollNo_lbl.grid(row=1,column=2,padx=10,sticky=W)

        rollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("Ubuntu",13,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Gender  
        gender_lbl=Label(class_student_frame,text="Gender",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        gender_lbl.grid(row=2,column=0,padx=10,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Ubuntu",13,"bold"),width=17,state="read only")
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        #DoB  
        DoB_lbl=Label(class_student_frame,text="DoB",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        DoB_lbl.grid(row=2,column=2,padx=10,sticky=W)

        DoB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("Ubuntu",13,"bold"))
        DoB_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        
        #email  
        email_lbl=Label(class_student_frame,text="Email",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        email_lbl.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("Ubuntu",13,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        #Phone  
        phnNo_lbl=Label(class_student_frame,text="Phone No",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        phnNo_lbl.grid(row=3,column=2,padx=10,sticky=W)

        phnNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("Ubuntu",13,"bold"))
        phnNo_entry.grid(row=3,column=3,padx=2,pady=10,sticky=W)
        
        #Address  
        address_lbl=Label(class_student_frame,text="Address",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        address_lbl.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("Ubuntu",13,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=10,sticky=W)
        
        #Teacher's Name  
        teacher_lbl=Label(class_student_frame,text="Teacher Name",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        teacher_lbl.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("Ubuntu",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=2,pady=10,sticky=W)
        
        #radio button style
        s = ttk.Style()                     
        s.configure('Wild.TRadiobutton',background="#1c195e", foreground='#e0af43',font=("Ubuntu",13,"bold"))
        
        #Radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take photo Sample",variable=self.var_radio1,value="Yes",style = 'Wild.TRadiobutton')
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)
        
        radiobtn2=ttk.Radiobutton(class_student_frame,text="No photo Sample",variable=self.var_radio1,value="No",style = 'Wild.TRadiobutton')
        radiobtn2.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #buttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#1c195e")
        btn_frame.place(x=0,y=260,width=680,height=120)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        save_btn.grid(row=0,column=0,padx=(90,10),pady=4)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        update_btn.grid(row=0,column=1,padx=10,pady=4)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        delete_btn.grid(row=0,column=2,padx=10,pady=4)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        reset_btn.grid(row=0,column=3,padx=(10,90),pady=4)
        
        
        takePhoto_btn=Button(btn_frame,command=self.generate_dataset,text="Take photo Sample",width=17,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        takePhoto_btn.grid(row=1,column=1,padx=10,pady=4)
        
        updatePhoto_btn=Button(btn_frame,text="Update Photo",width=17,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        updatePhoto_btn.grid(row=1,column=2,padx=10,pady=4)
        
        
        
        

        
        
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("Ubuntu",15,"bold"),bg="#e0af43",fg="#1c195e")
        right_frame.place(x=705,y=10,width=685,height=560)
        
        #****************Search System*****************************
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("Ubuntu",15,"bold"),bg="#e0af43",fg="#1c195e")
        search_frame.place(x=5,y=20,width=685,height=70)
        
        search_lbl=Label(search_frame,text="Search By",font=("Ubuntu",13,"bold"),bg="#e0af43",fg="#1c195e")
        search_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("Ubuntu",13,"bold"),width=17,state="read only")
        search_combo["values"]=("Select By","Roll_no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=18,font=("Ubuntu",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=12,font=("Ubuntu",10,"bold"),bg="#1c195e",fg="#e0af43")
        search_btn.grid(row=0,column=4,padx=2,pady=10,sticky=W)
        
        showAll_btn=Button(search_frame,text="Show All",width=12,font=("Ubuntu",10,"bold"),bg="#1c195e",fg="#e0af43")
        showAll_btn.grid(row=0,column=5,padx=2,pady=10,sticky=W)
        
        #**************table frame*************
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="#1c195e")
        table_frame.place(x=5,y=100,width=685,height=430)
        

        #*************scroll bar***********
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dept","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Sem")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DoB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]='headings'
        
        self.student_table.column("dept",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=50)
        self.student_table.column("sem",width=50)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=200)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #**************function declaration***************************************
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_id.get(),
                                                                                        self.var_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_address.get(),
                                                                                        self.var_teacher.get(),
                                                                                        self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added succesfully",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
        
        
    #******************************fetch data************************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #**********************************get cursor********************************************
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #*****************************update function*******************************
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update Student details", parent=self.root
                )
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="1234",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    sql = "update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll_no=%s, Gender=%s, DoB=%s, Email=%s, Phone_no=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_Id=%s"
                    values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get(),
                    )
                    my_cursor.execute(sql, values)
                    messagebox.showinfo(
                        "Success", "Student details successfully updated", parent=self.root
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                else:
                    if not Update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    # delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                    
    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
            
            
    #********************** Generate data set or Take photo Samples ****************************
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_name.get() == ""
            or self.var_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="1234",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                sql = "update student set Dep=%s, Course=%s, Year=%s, Semester=%s,Name=%s, Division=%s, Roll_no=%s, Gender=%s, DoB=%s, Email=%s, Phone_no=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_Id=%s"
                values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1,
                    )
                my_cursor.execute(sql, values)
                conn.commit()
                self.fetch_data()
                conn.close()

                # ========================== Load predefined date on face frontals from opencv ===========================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces= face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.3 , Minimum Neighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                # cap=cv2.VideoCapture(0)
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path='data/user.'+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==10:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","generating data set completed!!!",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        
    
if __name__  == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()