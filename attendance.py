from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import csv
from tkinter import filedialog
import cv2
import os

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1620x920")
        self.root.title("face Recognition System")
        
        #********************** variables**************************
        self.var_attd_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attd_status=StringVar()
        
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
        title_lbl=Label(bg_img,text="ATTENDANCE SYSTEM", font=("Ubuntu",25,"bold"),bg="#1c195e",fg="#e0af43")
        title_lbl.place(x=0,y=0,width=1620,height=35)
        
        #main frame
        main_frame= Frame(bg_img,bd=2)
        main_frame.place(x=50,y=50,width=1420,height=580)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("Ubuntu",15,"bold"),bg="#1c195e",fg="#e0af43")
        left_frame.place(x=10,y=10,width=690,height=560)
        
        left_inside_frame= Frame(left_frame,bd=2,relief=RIDGE,bg="#1c195e")
        left_inside_frame.place(x=5,y=5,width=680,height=300)
        
        #Labels Entry
        #Attendance ID 
        attdId_lbl=Label(left_inside_frame,text="Student Id",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        attdId_lbl.grid(row=0,column=0,padx=10,sticky=W)

        attdId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attd_id,width=20,font=("Ubuntu",13,"bold"))
        attdId_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #Name 
        name_lbl=Label(left_inside_frame,text="Name",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        name_lbl.grid(row=0,column=2,padx=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("Ubuntu",13,"bold"))
        name_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #Roll  
        roll_lbl=Label(left_inside_frame,text="Roll No",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        roll_lbl.grid(row=1,column=0,padx=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=20,font=("Ubuntu",13,"bold"))
        roll_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        #Department  
        dep_lbl=Label(left_inside_frame,text="Department",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        dep_lbl.grid(row=1,column=2,padx=10,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_dep,width=20,font=("Ubuntu",13,"bold"))
        dep_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #Date  
        date_lbl=Label(left_inside_frame,text="Date",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        date_lbl.grid(row=2,column=0,padx=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_date,width=20,font=("Ubuntu",13,"bold"))
        date_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        
        #Time  
        time_lbl=Label(left_inside_frame,text="Time",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        time_lbl.grid(row=2,column=2,padx=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("Ubuntu",13,"bold"))
        time_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
        
        #Attendance Status  
        attd_status_lbl=Label(left_inside_frame,text="Year",font=("Ubuntu",13,"bold"),bg="#1c195e",fg="#e0af43")
        attd_status_lbl.grid(row=3,column=0,padx=10,sticky=W)
        
        attd_status_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attd_status,font=("Ubuntu",13,"bold"),width=17,state="read only")
        attd_status_combo["values"]=("Absent","Present")
        attd_status_combo.current(0)
        attd_status_combo.grid(row=3,column=1,padx=2,pady=10,sticky=W)
        
        #buttons frame
        btn_frame=Frame(left_inside_frame,bg="#1c195e")
        btn_frame.place(x=0,y=200,width=680,height=50)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=15,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        import_btn.grid(row=0,column=0,padx=(90,10),pady=10)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=15,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        export_btn.grid(row=0,column=1,padx=10,pady=10)
        
        update_btn=Button(btn_frame,text="Update",width=15,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        update_btn.grid(row=0,column=2,padx=10,pady=10)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("Ubuntu",8,"bold"),bg="#e0af43",fg="#1c195e")
        reset_btn.grid(row=0,column=3,padx=(10,90),pady=10)
        
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Ubuntu",15,"bold"),bg="#e0af43",fg="#1c195e")
        right_frame.place(x=705,y=10,width=685,height=560)
        
        #**************table frame*************
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="#e0af43")
        table_frame.place(x=5,y=5,width=675,height=530)
        
        
        #*************scroll bar***********
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.attdReport_table=ttk.Treeview(table_frame,column=("id","roll","name","dept","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attdReport_table.xview)
        scroll_y.config(command=self.attdReport_table.yview)

        self.attdReport_table.heading("id",text="Attendance Id")
        self.attdReport_table.heading("roll",text="Roll No")
        self.attdReport_table.heading("name",text="Name")
        self.attdReport_table.heading("dept",text="Department")
        self.attdReport_table.heading("time",text="Time")
        self.attdReport_table.heading("date",text="Date ")
        self.attdReport_table.heading("attendance",text="Attendance Status")
        self.attdReport_table["show"]='headings'
        
        self.attdReport_table.column("id",width=100)
        self.attdReport_table.column("roll",width=100)
        self.attdReport_table.column("name",width=100)
        self.attdReport_table.column("dept",width=100)
        self.attdReport_table.column("time",width=100)
        self.attdReport_table.column("date",width=100)
        self.attdReport_table.column("attendance",width=100)
        
        self.attdReport_table.pack(fill=BOTH,expand=1)
        
        self.attdReport_table.bind("<ButtonRelease>",self.get_cursor)
        
    #*********************fetch data*************************

    def fetchData(self,rows):
        self.attdReport_table.delete(*self.attdReport_table.get_children())
        for i in rows:
            self.attdReport_table.insert("",END,values=i)
    
    #*********************import csv*************************
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)
            
    #********************export csv**********************
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
            messagebox.showinfo("Data Export","Your data exported"+os.path.basename(fln)+"successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
            
            
    #***********************************************
    def get_cursor(self,event=""):
        cursor_row=self.attdReport_table.focus()
        content=self.attdReport_table.item(cursor_row)
        rows=content['values']
        self.var_attd_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_attd_status.set(rows[6])

    def reset_data(self):
        self.var_attd_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attd_status.set("")
        
     
        


if __name__  == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()