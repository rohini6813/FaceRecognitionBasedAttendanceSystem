from tkinter import *
from time import strftime
from student import Student
from teacher_reg import Teacherregistry


class Login:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Sign Up')
        self.root.configure(background='lightblue')

        name_lbl=Label(self.root,text="Sign Up",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        question_lbl=Label(self.root,text="Select Your Role",font=('Quicksand',36),fg='black',bg='lightblue')
        question_lbl.place(relx=0.5, rely=0.3, anchor='center')

        teacher_btn = Button(self.root,command=self.teacher,cursor="hand2",text="Teacher",font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        teacher_btn.place(relx = 0.4,rely=0.4)

        student_btn = Button(self.root,text="Student",command=self.student_details,cursor="hand2",font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        student_btn.place(relx = 0.4,rely=0.5)

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app=Student(self.new_window)

    def teacher(self):
        self.new_window = Toplevel(self.root)
        self.app=Teacherregistry(self.new_window)


if __name__ =="__main__":
    root=Tk()

    app = Login(root)
    root.configure(bg='lightblue')
    root.mainloop()