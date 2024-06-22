from tkinter import *
from PIL import Image, ImageTk
from admin_login import AdminLogin
from teacherlogin2 import Login2
from studentlogin import Studentlogin
import time

class Admin:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Teacher Page")
        self.root.configure(background='white')

        main_frame =  Frame(self.root,bd=2,background='lightblue')
        main_frame.place(relx=0.5,rely=0.7,anchor='center',width=2000,height=1000)
  
        #left
        '''left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=('Quicksand',12,'bold'),background='#d8dbe2')
        left_frame.place(relx=0.01,y=10,width=920,height=670)'''
        
        college_logo_button = Image.open("images\college_logo2.png")
        college_logo_button = college_logo_button.resize((283,195))
        self.photocollege_logo_button = ImageTk.PhotoImage(college_logo_button)

        college_logo_button_1 = Button(self.root, image=self.photocollege_logo_button, cursor="hand2")
        college_logo_button_1.place(relx=0.085, rely=0.1, anchor='center', width=283, height=195)


        name_lbl=Label(self.root,text="Usha Mittal Institute Of Technology",font=('Times New Roman',36),fg='dark blue',bg='white')
        name_lbl.place(relx=0.35, rely=0.05, anchor='center')

        name2_lbl=Label(self.root,text="Shreemati Nathibai Damodar Thackeresy Women's University",font=('Times New Roman',20),fg='dark blue',bg='white')
        name2_lbl.place(relx=0.35, rely=0.1, anchor='center')

        name_lbl3=Label(self.root,text="Juhu-Tara Road, Sir Vitthaldas Vidyavihar, Santacruz(W), Mumbai, Maharashtra 400049",font=('Times New Roman',15),fg='dark blue',bg='white')
        name_lbl3.place(relx=0.36, rely=0.145, anchor='center')

        name_lbl4=Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SOFTWARE",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl4.place(relx=0.5, rely=0.25, anchor='center')

        name_lbl5=Label(self.root,text="Select Your Role for Login",font=('Quicksand',25),fg='maroon',bg='lightblue')
        name_lbl5.place(relx=0.5, rely=0.4, anchor='center')


        admin_button = Image.open("images/admin2.png")
        admin_button = admin_button.resize((220, 220))
        self.photoadmin_button = ImageTk.PhotoImage(admin_button)

        admin_button_1 = Button(self.root,command=self.admin, image=self.photoadmin_button, cursor="hand2")
        admin_button_1.place(relx=0.25, rely=0.6, anchor='center', width=220, height=220)

        admin_button_2 = Button(self.root, command=self.admin,text="Admin", cursor="hand2", font=('Quicksand', 15), bg='Crimson', fg='white')
        admin_button_2.place(relx=0.25, rely=0.72, anchor='center', width=220, height=40)
## teacher
        taeacher_button = Image.open("images/teacher2.png")
        taeacher_button = taeacher_button.resize((220, 220))
        self.phototaeacher_button = ImageTk.PhotoImage(taeacher_button)

        taeacher_button_1 = Button(self.root,command=self.teacher, image=self.phototaeacher_button, cursor="hand2")
        taeacher_button_1.place(relx=0.5, rely=0.6, anchor='center', width=220, height=220)

        taeacher_button_2 = Button(self.root,command=self.teacher, text="Teacher", cursor="hand2", font=('Quicksand', 15), bg='Crimson', fg='white')
        taeacher_button_2.place(relx=0.5, rely=0.72, anchor='center', width=220, height=40)
## student

        student_button = Image.open("images/student2.png")
        student_button = student_button.resize((220, 220))
        self.photostudent_button = ImageTk.PhotoImage(student_button)

        student_button_1 = Button(self.root,command=self.student, image=self.photostudent_button, cursor="hand2")
        student_button_1.place(relx=0.75, rely=0.6, anchor='center', width=220, height=220)

        student_button_2 = Button(self.root ,command=self.student, text="Student", cursor="hand2", font=('Quicksand', 15), bg='Crimson', fg='white')
        student_button_2.place(relx=0.75, rely=0.72, anchor='center', width=220, height=40)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()

    def student(self):
        self.new_window = Toplevel(self.root)
        self.app = Studentlogin(self.new_window)
    
    def admin(self):
        self.new_window = Toplevel(self.root)
        self.app = AdminLogin(self.new_window)

    def teacher(self):
        self.new_window = Toplevel(self.root)
        self.app = Login2(self.new_window)



         

if __name__ == "__main__":
    root = Tk()
    app = Admin(root)
    root.configure(bg='white')
    root.mainloop()

