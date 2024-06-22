from tkinter import *
from PIL import Image, ImageTk
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from teacher_reg import Teacherregistry
from teacherlogincred_copy import Teachercred


class Login:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        name_lbl=Label(self.root,text="Teacher Sign Up / Login",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        #registration
        teacher_reg_button = Image.open(r"images\registration.png")
        teacher_reg_button = teacher_reg_button.resize((220,220))
        self.phototeacher_reg_button = ImageTk.PhotoImage(teacher_reg_button)
        teacher_reg_button_1 = Button(self.root,command=self.register,image = self.phototeacher_reg_button,cursor="hand2",bg="white")
        teacher_reg_button_1.place(relx=0.35, rely=0.45, anchor='center',width=220,height=220)

        teacher_reg_button_2 = Button(self.root,command=self.register,text="Registration",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        teacher_reg_button_2.place(relx=0.35, rely=0.57, anchor='center',width=220,height=40)
        
        #login
        teacher_log_button = Image.open(r"images\login.png")
        teacher_log_button = teacher_log_button.resize((220,220))
        self.phototeacher_button = ImageTk.PhotoImage(teacher_log_button)
        teacher_log_button_1 = Button(self.root,command=self.teacherlog,image = self.phototeacher_button,cursor="hand2",bg="white")
        teacher_log_button_1.place(relx=0.65, rely=0.45, anchor='center',width=220,height=220)

        teacher_log_button_2 = Button(self.root,command=self.teacherlog,text="Login",cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        teacher_log_button_2.place(relx=0.65, rely=0.57, anchor='center',width=220,height=40)
        
        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()


    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Teacherregistry(self.new_window)

    def teacherlog(self):
        self.new_window = Toplevel(self.root)
        self.app = Teachercred(self.new_window)

       

if __name__ =="__main__":
    root=Tk()

    app = Login(root)
    root.configure(bg='lightblue')
    root.mainloop()