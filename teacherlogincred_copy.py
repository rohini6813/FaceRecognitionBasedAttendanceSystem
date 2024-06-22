from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
from time import strftime
import tkinter as tk


class Teachercred:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')

        self.teacher_entry = StringVar()
        self.teacher_password = StringVar()

        self.name = ""
        self.branch = ""
        self.semester = ""
        self.subject = ""
        self.teacher_data = []  # Initialize teacher_data attribute

        # Teacher ID Label
        label_teacher_id = tk.Label(root, text="Teacher ID", background='lightblue', foreground='black',
                                    font=('Quicksand', 12))
        label_teacher_id.place(relx=0.45, rely=0.3)

        # Teacher ID Entry
        entry_teacher_id = tk.Entry(root, textvariable=self.teacher_entry, font=('Quicksand', 12))
        entry_teacher_id.place(relx=0.45, rely=0.325)

        # Password Label
        label_password = tk.Label(root, background='lightblue', foreground='black', text="Password",
                                font=('Quicksand', 12))
        label_password.place(relx=0.45, rely=0.4)

        # Password Entry
        entry_password = tk.Entry(root, textvariable=self.teacher_password, show="*", font=('Quicksand', 12))
        entry_password.place(relx=0.45, rely=0.425)

        # Login Button
        btn_login = tk.Button(root, text="Login", command=self.login, font=('Quicksand', 12), bg="deep sky blue",
                            fg='white', width=19)
        btn_login.place(relx=0.45, rely=0.5)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()


    def login(self):
        try:
            self.conn = mysql.connector.connect(host='localhost', username='root', password='janhavikhadke',
                                        database='face_recognizer')
            self.cursor = self.conn.cursor()

            self.cursor.execute("SELECT name, branch, semester, subject FROM teacher WHERE teacher_id = %s AND password = %s",
                        (self.teacher_entry.get(), self.teacher_password.get()))
            self.teacher_data = self.cursor.fetchone()

            if self.teacher_data:
                self.name, self.branch, self.semester, self.subject = self.teacher_data  # Unpack the fetched data into variables
                
                messagebox.showinfo("Login Successful",
                                    f"Welcome, {self.name}!\nBranch: {self.branch}\nSemester: {self.semester}\nSubject: {self.subject}")
                
                if not os.path.exists("teacher_data.py"):
                    with open("teacher_data.py", "w") as file:
                        file.write(f"teacher_data = {self.teacher_data}")
                        # Do not write to the file again
                        self.teacher_data_written = True

                elif not getattr(self, 'teacher_data_written', False):
                    with open("teacher_data.py", "w") as file:
                        file.write(f"teacher_data = {self.teacher_data}")
                        self.teacher_data_written = True
                self.chooseoptions()
                return self.teacher_data 
            
            else:
                messagebox.showerror("Login Failed", "Invalid Teacher ID or Password")
                self.conn.close()

        
            
        
        


        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

 

    def chooseoptions(self):
        from teacheroptions import ChooseOperations 
        self.new_window = Toplevel(self.root)
        self.app = ChooseOperations(self.new_window)
       

if __name__ == "__main__":
    root = Tk()
    app = Teachercred(root)
    root.mainloop()
