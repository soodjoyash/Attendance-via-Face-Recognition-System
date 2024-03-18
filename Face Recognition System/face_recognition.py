from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        #TITLE-

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1285,height=45)

        #IMAGE1-

        img_left=Image.open("D:/Codes/Face Recognition System/Project Images/face_detector1.jpg")
        img_left=img_left.resize((550,600),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=50,width=550,height=600)

        img_right=Image.open("D:/Codes/Face Recognition System/Project Images/facesss.jpg")
        img_right=img_right.resize((725,600),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=550,y=50,width=725,height=600)

        #BUTTON-

        b1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="black",fg="white")
        b1.place(x=260,y=530,width=200,height=35)

    #FACE RECOGNITION -

    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="CuPcAkE#2004",database="facerecognition")
                my_cursor=conn.cursor()

                my_cursor.execute("Select studentName from student where studentID="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("Select rollNo from student where studentID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("Select Dep from student where studentID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                

                if confidence>77:
                    cv2.putText(img,f"rollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"studentName:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,225),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,y]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()



if __name__=="__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()        