from tkinter import*   #import tkinter
from tkinter import ttk
from PIL import Image,ImageTk  #import pillow library for images
from tkinter import messagebox
import mysql.connector
import cv2 #open source computer vision library

class Help:    #create class
    def __init__(self,root):   #define function
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1285,height=45)

        #FIRST IMAGE-

        img_top=Image.open("D:/Codes/Face Recognition System/Project Images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top=img_top.resize((1285,650),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1285,height=650)

        developer_label=Label(f_lbl,text="Email: joyash466.be22@chitkara.edu.in",font=("times new roman",20,"bold"),bg="yellow",fg="blue")
        developer_label.place(x=420,y=120)

        developer_label=Label(f_lbl,text="Email: kashish495.be22@chitkara.edu.in",font=("times new roman",20,"bold"),bg="yellow",fg="blue")
        developer_label.place(x=420,y=200)

        developer_label=Label(f_lbl,text="Email: joel465.be22@chitkara.edu.in",font=("times new roman",20,"bold"),bg="yellow",fg="blue")
        developer_label.place(x=450,y=280)


if __name__=="__main__":          
    root=Tk()
    obj=Help(root)
    root.mainloop()        