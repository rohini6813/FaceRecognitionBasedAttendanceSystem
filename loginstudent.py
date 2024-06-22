from tkinter import *
from tkinter import messagebox
from tkinter import *
import tkinter as tk
import mysql.connector
from student_data import student_data


class StudentLogin:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Student Login")
        self.root.configure(background='lightblue')

        self.var_studentid = StringVar()
        self.var_studentpass = StringVar()

        name_lbl=Label(self.root,text="Student Login",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        text_lbl=Label(self.root,text="Your Date of Birth is your Password(in DD/MM/YYYY format)",font=('Quicksand',18),fg='black',bg='lightblue')
        text_lbl.place(relx=0.5, rely=0.10, anchor='center')

        # Teacher ID Label
        label_student_id = tk.Label(root, text="Student ID", background='lightblue', foreground='black',
                                    font=('Quicksand', 12))
        label_student_id.place(relx=0.45, rely=0.3)

        # Teacher ID Entry
        entry_student_id = tk.Entry(root, textvariable=self.var_studentid, font=('Quicksand', 12))
        entry_student_id.place(relx=0.45, rely=0.325)

        label_password = tk.Label(root,background='lightblue', foreground='black', text="Password",
                                font=('Quicksand', 12))
        label_password.place(relx=0.45, rely=0.4)

        # Password Entry
        entry_password = tk.Entry(root, textvariable=self.var_studentpass, show="*", font=('Quicksand', 12))
        entry_password.place(relx=0.45, rely=0.425)

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

            self.cursor.execute("SELECT department,course,Year,Semester,student_id,Name,Division,Roll,Gender,email,phone,address FROM student WHERE student_id = %s AND Dob = %s",
                        (self.var_studentid.get(),self.var_studentpass.get()))
            self.student_data = self.cursor.fetchone()

            if self.student_data:
                self.department, self.course, self.year, self.semester,self.student_id, self.name, self.division, self.roll, self.gender, self.email, self.phone, self.address = self.student_data  # Unpack the fetched data into variables
                
            messagebox.showinfo("Login Successful",
                                f"Welcome, {self.name}!\nBranch: {self.department}\nSemester: {self.semester}\nSubject: {self.roll}")
    
            
            with open("student_data.txt",'w') as f:
                f.write(str(self.student_data))

            with open("student_data.txt",'r') as d:
                
                import studentviz 
                studentviz.Studentinfo(self.root,self.student_data)

        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root)

        
if __name__ =="__main__":
    root=Tk()

    app = StudentLogin(root)
    root.configure(bg='lightblue')
    root.mainloop()