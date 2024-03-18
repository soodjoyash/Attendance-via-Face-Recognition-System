from tkinter import*   #import tkinter
from tkinter import ttk
from PIL import Image,ImageTk  #import pillow library for images
import os
from student import Student
from train import Train
from face_recognition import Face_recognition
from developer import Developer
from help import Help

class Face_Recognition_System:    #create class
    def __init__(self,root):   #define function
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #FIRST IMAGE-

        img=Image.open("D:/Codes/Face Recognition System/Project Images/BestFacialRecognition.jpg")
        img=img.resize((425,130),Image.ANTIALIAS) #converts highter resloution image into lower resolution image
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=425,height=130)

        #SECOND IMAGE-

        img1=Image.open("D:/Codes/Face Recognition System/Project Images/faces.png")
        img1=img1.resize((425,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=425,y=0,width=425,height=130)

        #THIRD IMAGE-

        img2=Image.open("D:/Codes/Face Recognition System/Project Images/bg.jpg")
        img2=img2.resize((425,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=850,y=0,width=425,height=130)

        #BACKGROUND IMAGE-

        img3=Image.open("D:/Codes/Face Recognition System/Project Images/di.jpg")
        img3=img3.resize((1275,575),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1275,height=575)

        #TITLE-

        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",32,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1275,height=52)

        #1 STUDENT BUTTON-

        img4=Image.open("D:/Codes/Face Recognition System/Project Images/gettyimages-1022573162.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=70,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=250,width=200,height=40)


        #2 DETECT FACE BUTTON-

        img5=Image.open("D:/Codes/Face Recognition System/Project Images/face_detector1.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b1.place(x=390,y=70,width=200,height=200)

        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=390,y=250,width=200,height=40)


        #3 ATTENDANCE BUTTON-

        img6=Image.open("D:/Codes/Face Recognition System/Project Images/report.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=680,y=70,width=200,height=200)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=250,width=200,height=40)


        #4 HELP DESK BUTTON-

        img7=Image.open("D:/Codes/Face Recognition System/Project Images/helpdesk.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,command=self.help_data,cursor="hand2")
        b1.place(x=975,y=70,width=200,height=200)

        b1_1=Button(bg_img,text="Help Desk",command=self.help_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=975,y=250,width=200,height=40)


        #5 TRAIN DATA BUTTON-

        img8=Image.open("D:/Codes/Face Recognition System/Project Images/Train.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2")
        b1.place(x=100,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Train Data",command=self.train_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=500,width=200,height=40)


        #6 PHOTOS BUTTON-

        img9=Image.open("D:/Codes/Face Recognition System/Project Images/opencv_face_reco_more_data.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=390,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=390,y=500,width=200,height=40)


        #7 DEVELOPER BUTTON-

        img10=Image.open("D:/Codes/Face Recognition System/Project Images/Team-Management-Software-Development.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
        b1.place(x=680,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Developer",command=self.developer_data,cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=680,y=500,width=200,height=40)


        #8 EXIT BUTTON-

        img11=Image.open("D:/Codes/Face Recognition System/Project Images/exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=975,y=310,width=200,height=200)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",20,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=975,y=500,width=200,height=40)

    

        #FUNCTION-

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)


      
if __name__=="__main__":        
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()