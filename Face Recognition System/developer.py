from tkinter import*   #import tkinter
from tkinter import ttk
from PIL import Image,ImageTk  #import pillow library for images
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision library

class Developer:    #create class
    def __init__(self,root):   #define function
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1285,height=45)

        #FIRST IMAGE-

        img_top=Image.open("D:/Codes/Face Recognition System/Project Images/dev.jpg")
        img_top=img_top.resize((1285,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1285,height=650)

        #Frame-
        main_frame=Frame(f_lbl,bd=1,bg="white")
        main_frame.place(x=750,y=0,width=500,height=550)

        img_bottom=Image.open("D:/Codes/Face Recognition System/Project Images/developer.jpg")
        img_bottom=img_bottom.resize((200,150),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=1035,y=60,width=200,height=150)

        #developer info
        developer_label=Label(main_frame,text="This is a Team project made by: ",font=("times new roman",15,"bold"),bg="white",fg="green")
        developer_label.place(x=0,y=5)

        developer_label=Label(main_frame,text="Joyash Sood ",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=70)

        developer_label=Label(main_frame,text="Kashish Barthwal ",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=120)

        developer_label=Label(main_frame,text="Joel Matthew ",font=("times new roman",15,"bold"),bg="white")
        developer_label.place(x=0,y=170)

        img_1=Image.open("D:/Codes/Face Recognition System/Project Images/Bill_Gates.jpg")
        img_1=img_1.resize((400,300),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        f_lbl=Label(self.root,image=self.photoimg_1)
        f_lbl.place(x=800,y=275,width=400,height=300)


       
if __name__=="__main__":          
    root=Tk()
    obj=Developer(root)
    root.mainloop()        