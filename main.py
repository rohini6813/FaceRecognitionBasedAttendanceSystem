from tkinter import *
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from attendance_files import Excel
from attendance import Attendance2
from teacherlogin import Login
from studentlogin import Studentlogin
from teacherlogin import Login


class Attendance:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Attendance")
        self.root.configure(background='lightblue')
        

        name_lbl=Label(self.root,text="Admin",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        #Add
        add_button = Image.open(r"images\plus.png")
        add_button = add_button.resize((220,220))
        self.photoadd_button = ImageTk.PhotoImage(add_button)

        add_button_1= Button(self.root,image = self.photoadd_button,command=self.student_details,cursor="hand2")
        add_button_1.place(relx=0.20, rely=0.3, anchor='center',width=220,height=220)

        add_button_2 = Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        add_button_2.place(relx=0.20, rely=0.42, anchor='center',width=220,height=40)

        #extra
    

        #face detect button
        face_detect_button = Image.open(r"images\facedetect.png")
        face_detect_button = face_detect_button.resize((220,220))
        self.photoface_detect_button = ImageTk.PhotoImage(face_detect_button)

        face_detect_button_1 = Button(self.root,command=self.face_recog,image = self.photoface_detect_button,cursor="hand2",bg="white")
        face_detect_button_1.place(relx=0.40, rely=0.3, anchor='center',width=220,height=220)

        face_detect_button_2 = Button(self.root,command=self.face_recog,text="Take Attendance",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        face_detect_button_2.place(relx=0.40, rely=0.42, anchor='center',width=220,height=40)

        #attendance button
        attendance_button = Image.open(r"images\attendance3.png")
        attendance_button = attendance_button.resize((220,220))
        self.photoattendance_button = ImageTk.PhotoImage(attendance_button)

        attendance_button_1 = Button(self.root,command=self.attendance,image = self.photoattendance_button,cursor="hand2",bg="white")
        attendance_button_1.place(relx=0.60, rely=0.3, anchor='center',width=220,height=220)

        attendance_button_2 = Button(self.root,command=self.attendance,text="Generate Files",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        attendance_button_2.place(relx=0.60, rely=0.42, anchor='center',width=220,height=40)

        #attendance button
        student_button = Image.open(r"images\student.png")
        student_button = student_button.resize((220,220))
        self.photostudent_button = ImageTk.PhotoImage(student_button)

        student_button_1 = Button(self.root,image = self.photostudent_button,command=self.studentlog,cursor="hand2",bg="white")
        student_button_1.place(relx=0.80, rely=0.3, anchor='center',width=220,height=220)

        student_button_2 = Button(self.root,text="Student",cursor="hand2",command=self.studentlog,font=('Quicksand',15),bg='Crimson',fg='white')
        student_button_2.place(relx=0.80, rely=0.42, anchor='center',width=220,height=40)



        #Train
        train_button = Image.open(r"images\train.png")
        train_button = train_button.resize((220,220))
        self.phototrain_button = ImageTk.PhotoImage(train_button)

        train_button_1 = Button(self.root,command=self.train_data,image = self.phototrain_button,cursor="hand2",bg="white")
        train_button_1.place(relx=0.20, rely=0.7, anchor='center',width=220,height=220)

        train_button_2 = Button(self.root,command=self.train_data,text="Train",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        train_button_2.place(relx=0.20, rely=0.82, anchor='center',width=220,height=40)

        #photos
        photo_button = Image.open(r"images\photos.png")
        photo_button = photo_button.resize((220,220))
        self.photophoto_button = ImageTk.PhotoImage(photo_button)
        photo_button_1 = Button(self.root,image = self.photophoto_button,command=self.open_image,cursor="hand2",bg="white")
        photo_button_1.place(relx=0.40, rely=0.7, anchor='center',width=220,height=220)

        photo_button_2 = Button(self.root,text="Photos",command=self.open_image,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        photo_button_2.place(relx=0.40, rely=0.82, anchor='center',width=220,height=40)

        #Attendance Files
        file_button = Image.open(r"images\files.png")
        file_button = file_button.resize((220,220))
        self.photofile_button = ImageTk.PhotoImage(file_button)
        file_button_1 = Button(self.root,command=self.open_files,image = self.photofile_button,cursor="hand2",bg="white")
        file_button_1.place(relx=0.60, rely=0.7, anchor='center',width=220,height=220)

        file_button_2 = Button(self.root,command=self.open_files,text="Attendance Files",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        file_button_2.place(relx=0.60, rely=0.82, anchor='center',width=220,height=40)

        #Attendance Files
        teacher_button = Image.open(r"images\teacher.png")
        teacher_button = teacher_button.resize((220,220))
        self.phototeacher_button = ImageTk.PhotoImage(teacher_button)
        teacher_button_1 = Button(self.root,command=self.teacher,image = self.phototeacher_button,cursor="hand2",bg="white")
        teacher_button_1.place(relx=0.80, rely=0.7, anchor='center',width=220,height=220)

        teacher_button_2 = Button(self.root,command=self.teacher,text="Teacher",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        teacher_button_2.place(relx=0.80, rely=0.82, anchor='center',width=220,height=40)
        
        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()
        


     
    

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def open_image(self):
        os.startfile('data')

    def open_files(self):
        os.startfile('Attendance_Sheets')

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recog(self):
        self.new_window  = Toplevel(self.root)
        self.app = Attendance2(self.new_window)

    def attendance(self):
        self.new_window  = Toplevel(self.root)
        self.app = Excel(self.new_window)

    def teacher(self):
        self.new_window  = Toplevel(self.root)
        self.app = Login(self.new_window)

    def studentlog(self):
        self.new_window  = Toplevel(self.root)
        self.app = Studentlogin(self.new_window)

    def teacherlog(self):
        self.new_window = Toplevel(self.root)
        self.app = Login(self.new_window)

   



if __name__ =="__main__":
    root=Tk()

    app = Attendance(root)
    root.configure(bg='lightblue')
    root.mainloop()