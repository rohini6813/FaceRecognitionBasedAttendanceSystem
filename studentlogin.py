from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from loginstudent import StudentLogin


class Studentlogin:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        name_lbl=Label(self.root,text="Student Login",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        student_button = Image.open(r"images\student.png")
        student_button = student_button.resize((220,220))
        self.photostudent_button = ImageTk.PhotoImage(student_button)
        student_button_1 = Button(self.root,command=self.login,image = self.photostudent_button,cursor="hand2",bg="white")
        student_button_1.place(relx=0.50, rely=0.45, anchor='center',width=220,height=220)

        student_button_2 = Button(self.root,command=self.login,text="Student",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        student_button_2.place(relx=0.50, rely=0.57, anchor='center',width=220,height=40)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()


    def login(self):
        self.new_window = Toplevel(self.root)
        self.app = StudentLogin(self.new_window)

if __name__ =="__main__":
    root=Tk()

    app = Studentlogin(root)
    root.configure(bg='lightblue')
    root.mainloop()