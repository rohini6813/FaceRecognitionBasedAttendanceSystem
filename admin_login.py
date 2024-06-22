from tkinter import *
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import mysql.connector
from student_data import student_data

from main import Attendance


class AdminLogin:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Student Login")
        self.root.configure(background='lightblue')

        self.var_adminid = StringVar()
        self.var_adminpass = StringVar()

        name_lbl=Label(self.root,text="Admin Login",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.1, anchor='center')

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


 
       

        # Teacher ID Label
        label_student_id = tk.Label(root, text="ID", background='lightblue', foreground='black',
                                    font=('Quicksand', 12))
        label_student_id.place(relx=0.45, rely=0.3)

        # Teacher ID Entry
        entry_admin_id = tk.Entry(root, textvariable=self.var_adminid, font=('Quicksand', 12))
        entry_admin_id.place(relx=0.45, rely=0.325)

        label_password = tk.Label(root,background='lightblue', foreground='black', text="Password",
                                font=('Quicksand', 12))
        label_password.place(relx=0.45, rely=0.4)

        # Password Entry
        entry_password = tk.Entry(root, textvariable=self.var_adminpass, show="*", font=('Quicksand', 12))
        entry_password.place(relx=0.45, rely=0.425)

        btn_login = tk.Button(root, text="Login", command=self.login, font=('Quicksand', 12), bg="deep sky blue",
                            fg='white', width=19)
        btn_login.place(relx=0.45, rely=0.5)
    def login(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', username='root', password='janhavikhadke',
                                        database='face_recognizer')
            self.cursor = self.conn.cursor()

            self.cursor.execute("SELECT name, admin_id, password FROM admin WHERE name = %s AND password = %s",
                        (self.var_adminid.get(), self.var_adminpass.get()))
            self.admin_data = self.cursor.fetchone()
            self.name, self.id,self.password = self.admin_data

            

            messagebox.showinfo("Login Successful",
                                f"Welcome, {self.name}")
            
            self.mainpage()

                
                
                # print(self.teacher_data,"<------- 1")
                # Now you have the name, branch, semester, and subject stored in variables
                # You can use these variables as needed in your application
                

                
        
        
        
            
        
        


        except Exception as e:
            
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

        

    def exit(self):
        self.root.destroy()


    def mainpage(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

if __name__ =="__main__":
    root=Tk()

    app = AdminLogin(root)
    root.configure(bg='lightblue')
    root.mainloop()