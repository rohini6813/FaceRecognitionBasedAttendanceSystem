from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql
import mysql.connector

class Teacherregistry:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Teacher Registration")
        self.root.configure(background='lightblue')

        #variables
        self.var_name = StringVar()
        self.var_teacher_id = StringVar()
        self.var_branch = StringVar()
        self.var_semester = StringVar()
        self.var_subject = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()

        name_lbl=Label(self.root,text="TEACHER REGISTRATION",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        main_frame =  Frame(self.root,bd=2,background='#58a4b0')
        main_frame.place(relx=0.5,rely=0.5,anchor='center',width=1900,height=700)
  
        #left
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Teacher Details", font=('Quicksand',12,'bold'),background='#d8dbe2')
        left_frame.place(relx=0.01,y=10,width=920,height=670)

        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Teacher", font=('Quicksand',12,'bold'),background='#d8dbe2')
        right_frame.place(relx=0.5,y=10,width=920,height=670)

        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,background='#d8dbe2')
        table_frame.place(relx=0.02,rely=0.1,width=880,height=460)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=('teacher_id','name','branch','semester','subject'), xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('teacher_id',text="Teacher ID")
        self.student_table.heading('name',text="Name")
        self.student_table.heading('branch',text="Branch")
        self.student_table.heading('semester',text="Semester")
        self.student_table.heading('subject',text="Subject")
        
        self.student_table['show']='headings'

        self.student_table.column('teacher_id',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('branch',width=100)
        self.student_table.column('semester',width=100)
        self.student_table.column('subject',width=100)
        
        



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    

#teache_id,name,branch,semester,subject,password
        teacher_id_label=Label(left_frame,text="Teacher ID",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        teacher_id_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        teacher_id_entry = ttk.Entry(left_frame,textvariable=self.var_teacher_id,width=60,font=('Quicksand',12,'italic'))
        teacher_id_entry.grid(row=0,column=1,padx=10,sticky=W)

        name_label=Label(left_frame,text="Name",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        name_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=60,font=('Quicksand',12,'italic'))
        name_entry.grid(row=2,column=1,padx=10,sticky=W)

        branch_label=Label(left_frame,text="Branch",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        branch_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        branch_combo = ttk.Combobox(left_frame,textvariable=self.var_branch,font=('Quicksand',12,'italic'),width=17,state='readonly')
        branch_combo['values']=('Select Branch', "Computer","IT",'Civil','Mechanical')
        branch_combo.current(0)
        branch_combo.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        '''branch_entry = ttk.Entry(left_frame,textvariable=self.var_branch,width=60,font=('Quicksand',12,'italic'))
        branch_entry.grid(row=4,column=1,padx=10,sticky=W)'''

        semester_label=Label(left_frame,text="Semester",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        semester_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)

        semester_combo = ttk.Combobox(left_frame,textvariable=self.var_semester,font=('Quicksand',12,'italic'),width=17,state='readonly')
        semester_combo['values']=('Select Semester', "1","2",'3','4',"5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=6,column=1,padx=2,pady=10,sticky=W)

        '''semester_entry = ttk.Entry(left_frame,textvariable=self.var_semester,width=60,font=('Quicksand',12,'italic'))
        semester_entry.grid(row=6,column=1,padx=10,sticky=W)'''

        subject_label=Label(left_frame,text="Subject",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        subject_label.grid(row=8,column=0,padx=10,pady=10,sticky=W)

        subject_entry = ttk.Entry(left_frame,textvariable=self.var_subject,width=60,font=('Quicksand',12,'italic'))
        subject_entry.grid(row=8,column=1,padx=10,sticky=W)

        password_label=Label(left_frame,text="Password",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        password_label.grid(row=10,column=0,padx=10,pady=10,sticky=W)

        password_entry = ttk.Entry(left_frame,textvariable=self.var_password,show='*',width=60,font=('Quicksand',12,'italic'))
        password_entry.grid(row=10,column=1,padx=10,sticky=W)

        confirm_password_label=Label(left_frame,text="Confirm Password",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        confirm_password_label.grid(row=12,column=0,padx=10,pady=10,sticky=W)

        confirm_password_entry = ttk.Entry(left_frame,textvariable=self.var_confirm_password,width=60,font=('Quicksand',12,'italic'))
        confirm_password_entry.grid(row=12,column=1,padx=10,sticky=W)


        button1_frame = LabelFrame(left_frame,bd=2)
        button1_frame.place(relx=0.1,rely=0.6,width=728,height=35)

        save_btn = Button(button1_frame,command=self.save,text="Save",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        save_btn.grid(row=0,column=0)

        update_btn = Button(button1_frame,text="Update",command=self.update,font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button1_frame,command=self.delete,text="Delete",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button1_frame,command=self.reset,text="Reset",font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        reset_btn.grid(row=0,column=3)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()

    def save(self):
        if self.var_branch.get() != '' or self.var_confirm_password.get() != '' or self.var_name.get() != '' or self.var_password.get() != '' or self.var_semester.get() != '' or self.var_teacher_id.get() != '' or self.var_subject.get() != '':
            if self.var_password.get() != self.var_confirm_password.get():
                messagebox.showerror("Wrong Password","Password does not match",parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer',)
                    my_cursor = conn.cursor()
                    my_cursor.execute('insert into teacher values(%s,%s,%s,%s,%s,%s)',(
                                                                                                                    self.var_teacher_id.get(),
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_branch.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_subject.get(),
                                                                                                                    self.var_password.get()


                                                                                                                    

                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Success','Teacher Details has been added Successfully', parent = self.root)

                except Exception as e:
                    messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )
        else:
            messagebox.showerror("Error","All Fields are Required",parent=self.root)


    def update(self):
        if self.var_branch.get() != '' or self.var_confirm_password.get() != '' or self.var_name.get() != '' or self.var_password.get() != '' or self.var_semester.get() != '' or self.var_teacher_id.get() != '' or self.var_subject.get() != '':
            if self.var_password.get() != self.var_confirm_password.get():
                messagebox.showerror("Wrong Password","Password does not match",parent=self.root)
            else:
                try:
                    update = messagebox.askyesno("Update","Do you want to Update Teacher Details",parent=self.root)
                    if update>0:
                        conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer',)
                        my_cursor = conn.cursor()
                        my_cursor.execute('update teacher set name=%s,branch=%s,semester=%s,subject=%s,password=%s where teacher_id=%s',(
                                                                                                                        
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_branch.get(),
                                                                                                                        self.var_semester.get(),
                                                                                                                        self.var_subject.get(),
                                                                                                                        self.var_password.get(),
                                                                                                                        self.var_teacher_id.get()


                                                                                                                        

                                                                                                                    ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo('Success','Teacher Details has been added Successfully', parent = self.root)
                    else:
                        if not update:
                            return
                        
                except Exception as e:
                    messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )
        else:
            messagebox.showerror("Error","All Fields are Required",parent=self.root)


    def delete(self):
        if self.var_teacher_id.get() == '':
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to DELETE Teacher Details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
                    my_cursor = conn.cursor()
                    sql = "delete from teacher where teacher_id=%s"
                    val = (self.var_teacher_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Teacher Details has been Deleted Successfully",parent = self.root)

            
            except Exception as e:
                messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )


    def reset(self):
        self.var_name.set(''),
        self.var_branch.set(''),
        self.var_semester.set(''),
        self.var_subject.set(''),
        self.var_password.set(''),
        self.var_teacher_id.set('')
        self.var_confirm_password.set('')
    

    def get_cursor(self,event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_teacher_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_branch.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_subject.set(data[4])
        

    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from teacher')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()



        

if __name__ =="__main__":
    root=Tk()

    app = Teacherregistry(root)
    root.configure(bg='lightblue')
    root.mainloop()