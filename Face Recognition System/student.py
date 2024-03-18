from tkinter import*   #import tkinter
from tkinter import ttk
from PIL import Image,ImageTk  #import pillow library for images
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision library

class Student:    #create class
    def __init__(self,root):   #define function
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #VARIABLES-

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentID=StringVar()
        self.var_studentName=StringVar()
        self.var_classDiv=StringVar()
        self.var_rollNo=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phoneNo=StringVar()
        self.var_address=StringVar()
        self.var_teacherName=StringVar()

    
        #FIRST IMAGE-

        img=Image.open("D:/Codes/Face Recognition System/Project Images/face-recognition.png")
        img=img.resize((425,110),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=425,height=110)

        #SECOND IMAGE-

        img1=Image.open("D:/Codes/Face Recognition System/Project Images/pipt.jpg")
        img1=img1.resize((425,110),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=425,y=0,width=425,height=110)

        #THIRD IMAGE-

        img2=Image.open("D:/Codes/Face Recognition System/Project Images/KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2=img2.resize((425,110),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=850,y=0,width=425,height=110)

        #BACKGROUND IMAGE-

        img3=Image.open("D:/Codes/Face Recognition System/Project Images/wp2551980.jpg")
        img3=img3.resize((1275,575),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1275,height=575)

        #TITLE-

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",30,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1275,height=45)

        main_frame=Frame(bg_img,bd=1)
        main_frame.place(x=3,y=47,width=1262,height=523)

        #LEFT SIDE LABEL FRAME-

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=5,y=1,width=605,height=515)

        img_left=Image.open("D:/Codes/Face Recognition System/Project Images/adobebook.jpeg")
        img_left=img_left.resize((600,120),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=1,y=2,width=600,height=120)

        #CURRENT COURSE INFORMATION-

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=1,y=125,width=600,height=85)

        #DEPARTMENT-

        dep_label=Label(current_course_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=5)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly") #we can select options through combo box
        dep_combo["values"]=("Select Department","Computer","Electrical","Civil","Mechanical") #enter values with tuple
        dep_combo.current(0) #to see select department option first 
        dep_combo.grid(row=0,column=1,padx=10,pady=2)

        #COURSE-

        course_label=Label(current_course_frame,text="Course:",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly") #we can select options through combo box
        course_combo["values"]=("Select Course","FE","SE","TE","BE") #enter values with tuple
        course_combo.current(0) #to see select department option first 
        course_combo.grid(row=0,column=3,padx=10,pady=2,sticky=W)

        #YEAR-

        year_label=Label(current_course_frame,text="Year:",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly") #we can select options through combo box
        year_combo["values"]=("Select Year","2021-22","2022-23","2023-24","2024-25") #enter values with tuple
        year_combo.current(0) #to see select department option first 
        year_combo.grid(row=1,column=1,padx=10,pady=2,sticky=W)

        #SEMESTER-

        semester_label=Label(current_course_frame,text="Semester:",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=2,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly") #we can select options through combo box
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2") #enter values with tuple
        semester_combo.current(0) #to see select department option first 
        semester_combo.grid(row=1,column=3,padx=10,pady=2,sticky=W) #sticky=waste if cell is larger than widget it does not cause an error

        #STUDENT INFORMATION-

        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=1,y=210,width=600,height=280)

        #STUDENT ID-

        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=2,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentID,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=2,pady=3,sticky=W)

        #STUDENT NAME-

        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=3,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentName,width=18,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=2,sticky=W)

        #CLASS DIVISION-

        classDiv_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        classDiv_label.grid(row=1,column=0,padx=2,sticky=W)

        classDiv_entry=ttk.Entry(class_student_frame,textvariable=self.var_classDiv,width=20,font=("times new roman",12,"bold"))
        classDiv_entry.grid(row=1,column=1,padx=2,pady=3,sticky=W)

        #ROLL NUMBER-

        rollNo_label=Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=1,column=2,padx=5,sticky=W)

        rollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollNo,width=18,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=2,sticky=W)

        #GENDER-

        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select","Male","Female","Other")
        gender_combo.current(0) 
        gender_combo.grid(row=2,column=1,padx=0,sticky=W)

        #DOB-

        dob_label=Label(class_student_frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=18,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=2,sticky=W)

        #Email ID-

        email_label=Label(class_student_frame,text="Email ID:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=2,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=2,pady=3,sticky=W)

        #PHONE NUMBER-

        phoneNo_label=Label(class_student_frame,text="Phone Number:",font=("times new roman",12,"bold"),bg="white")
        phoneNo_label.grid(row=3,column=2,padx=2,sticky=W)

        phoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phoneNo,width=18,font=("times new roman",12,"bold"))
        phoneNo_entry.grid(row=3,column=3,padx=2,pady=3,sticky=W)


        #ADDRESS-

        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=2,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=2,pady=3,sticky=W)

        #TEACHER NAME-

        teacherName_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacherName_label.grid(row=4,column=2,padx=2,sticky=W)

        teacherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacherName,width=18,font=("times new roman",12,"bold"))
        teacherName_entry.grid(row=4,column=3,padx=2,pady=3,sticky=W)

        #RADIO BUTTONS -

        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0,padx=5,pady=10)

        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1,padx=0,pady=10)

        #BUTTON FRAME-

        btn_frame=Frame(class_student_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=190,width=595,height=80)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #BUTTON FRAME 2-

        btn_frame1=Frame(class_student_frame,bd=1,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=225,width=595,height=45)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #RIGHT SIDE LABEL FRAME-

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=1,width=635,height=515)

        #RIGHT SIDE IMAGE-

        img_right=Image.open("D:/Codes/Face Recognition System/Project Images/gettyimages-1022573162.jpg")
        img_right=img_right.resize((630,120),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=1,y=2,width=630,height=120)

        #SEARCH SYSTEM-

        search_system_frame=LabelFrame(Right_frame,bd=1,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_system_frame.place(x=1,y=125,width=630,height=65)

        search_label=Label(search_system_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5)

        search_combo=ttk.Combobox(search_system_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0) 
        search_combo.grid(row=0,column=1,padx=5,pady=2)

        search_entry=ttk.Entry(search_system_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=3,sticky=W)

        search_btn=Button(search_system_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_system_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4)

        #TABLE FRAME-

        table_frame=Frame(Right_frame,bd=1,bg="white",relief=RIDGE)
        table_frame.place(x=1,y=195,width=630,height=295)

        #SCROLL BAR-

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","semester","studentID","studentName","classDiv","rollNo","gender","dob","email","phoneNo","address","teacherName","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) #setting up scroll bars

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y) #Placed scroll bars 
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("studentID",text="StudentID")
        self.student_table.heading("studentName",text="StudentName")
        self.student_table.heading("classDiv",text="ClassDivision")
        self.student_table.heading("rollNo",text="RollNo")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DateOfBirth")
        self.student_table.heading("email",text="EmailID")
        self.student_table.heading("phoneNo",text="PhoneNumber")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacherName",text="TeacherName")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("studentID",width=100)
        self.student_table.column("studentName",width=100)
        self.student_table.column("classDiv",width=100)
        self.student_table.column("rollNo",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phoneNo",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacherName",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

        #FUNCTION DECLARATION-

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()=="":
            messagebox.showerror("Error","All Fields Are Required To Be Filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_studentID.get(),
                                                                                                    self.var_studentName.get(),
                                                                                                    self.var_classDiv.get(),
                                                                                                    self.var_rollNo.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phoneNo.get(),
                                                                                                    self.var_address.get(),
                                                                                                    self.var_teacherName.get(),
                                                                                                    self.var_radio1.get()
                                                                                               
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success!","Student deatils have been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                #FETCH DATA-

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

        #GET CURSOR-

    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_studentID.set(data[4]),
        self.var_studentName.set(data[5]),
        self.var_classDiv.set(data[6]),
        self.var_rollNo.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phoneNo.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacherName.set(data[13]),
        self.var_radio1.set(data[14])

        #UPDATE FUNCTION-

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()=="":
            messagebox.showerror("Error","All Fields Are Required To Be Filled",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you wan to update these student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_studentName.get(),
                                                                                                                                                                                        self.var_classDiv.get(),
                                                                                                                                                                                        self.var_rollNo.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phoneNo.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacherName.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_studentID.get()
                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)


    #DELETE FUNCTION-
    
    def delete_data(self):
        if self.var_studentID.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_studentID.get())
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)

    #RESET FUNCTION-

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentID.set("")
        self.var_studentName.set("")
        self.var_classDiv.set("")
        self.var_rollNo.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phoneNo.set("")
        self.var_address.set("")
        self.var_teacherName.set("")
        self.var_radio1.set("")

        #GENERATE DATA SET OR TAKE A PHOTO SAMPLE-

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_studentName.get()=="" or self.var_studentID.get()=="":
            messagebox.showerror("Error","All Fields Are Required To Be Filled",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where StudentID=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_studentName.get(),
                                                                                                                                                                                    self.var_classDiv.get(),
                                                                                                                                                                                    self.var_rollNo.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phoneNo.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacherName.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_studentID.get()==id+1
                                                                                                                                                                                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

        #LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV-

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultisclae(gray,1.3,5)  #scaling factor=1.3,min. neighbour =5
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="data/user."+str(id)+"."+str(img_id)+".jpg" #Storing the clicked images
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data set completed successfully!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)



                    
                        
if __name__=="__main__":          
    root=Tk()
    obj=Student(root)
    root.mainloop()        