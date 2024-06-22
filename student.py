from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Student Details")
        self.root.configure(bg='lightblue')


        #variables
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       



        name_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        main_frame =  Frame(self.root,bd=2,background='#58a4b0')
        main_frame.place(relx=0.5,rely=0.5,anchor='center',width=1900,height=700)
  
        #left
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details", font=('Quicksand',12,'bold'),background='#d8dbe2')
        left_frame.place(relx=0.01,y=10,width=920,height=670)

        
        #current course
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information", font=('Quicksand',12,'italic',"underline"),background='#d8dbe2')
        current_course_frame.place(relx=0.02,rely=0.1,width=880,height=180)


        #Department
        dep_label=Label(current_course_frame,text="Department",font=('Quicksand',12,'bold'),background='#d8dbe2',foreground='black')
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_department,font=('Quicksand',12,'italic'),width=17,state='readonly')
        dep_combo['values']=('Select Department', "Computer","IT",'Civil','Mechanical')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=('Quicksand',12,'bold'),background='#d8dbe2',foreground='black')
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=('Quicksand',12,'italic'),width=17,state='readonly')
        course_combo['values']=('Select Course', "FE","SE",'TE','BE')
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=('Quicksand',12,'bold'),background='#d8dbe2',foreground='black')
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=('Quicksand',12,'italic'),width=17,state='readonly')
        year_combo['values']=('Select Year', "2020-21","2021-22",'2022-23','2023-24')
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #SEMESTER
        sem_label=Label(current_course_frame,text="Semester",font=('Quicksand',12,'bold'),background='#d8dbe2',foreground='black')
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=('Quicksand',12,'italic'),width=17,state='readonly')
        sem_combo['values']=('Select Semester', "Semester-1","Semester-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #Student Information

        class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Information", font=('Quicksand',12,'italic',"underline"),background='#d8dbe2')
        class_student_frame.place(relx=0.02,rely=0.4,width=880,height=260)


         #Student Information
        studentid_label=Label(class_student_frame,text="Student ID",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        studentid_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        studentid_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=('Quicksand',12,'italic'))
        studentid_entry.grid(row=0,column=1,padx=10,sticky=W)

        #2
        studentname_label=Label(class_student_frame,text="Student Name",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        studentname_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        studentname_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=('Quicksand',12,'italic'))
        studentname_entry.grid(row=0,column=3,padx=10,sticky=W)

        #3
        div_label=Label(class_student_frame,text="Class Division",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        div_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        #div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=('Quicksand',12,'italic'))
        #div_entry.grid(row=1,column=1,padx=10,sticky=W)

        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=('Quicksand',12,'italic'),width=17,state='readonly')
        div_combo['values']=('Select Division', "A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #4
        roll_label=Label(class_student_frame,text="Roll No",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        roll_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        roll_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=('Quicksand',12,'italic'))
        roll_entry.grid(row=1,column=3,padx=10,sticky=W)

        #5
        gender_label=Label(class_student_frame,text="Gender",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        gender_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        #gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=('Quicksand',12,'italic'))
        #gender_entry.grid(row=2,column=1,padx=10,sticky=W)
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=('Quicksand',12,'italic'),width=17,state='readonly')
        gender_combo['values']=('Male', "Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=10,sticky=W)


        #6
        dob_label=Label(class_student_frame,text="Date Of Birth",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        dob_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=('Quicksand',12,'italic'))
        dob_entry.grid(row=2,column=3,padx=10,sticky=W)

        #7
        email_label=Label(class_student_frame,text="Email",font=('Quicksand',12,),background='#d8dbe2',foreground='black')
        email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=('Quicksand',12,'italic'))
        email_entry.grid(row=3,column=1,padx=10,sticky=W)

        #8
        phone_label=Label(class_student_frame,text="Phone Number",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        phone_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=('Quicksand',12,'italic'))
        phone_entry.grid(row=3,column=3,padx=10,sticky=W)

        #9
        address_label=Label(class_student_frame,text="Address",font=('Quicksand',12,),background='#d8dbe2',foreground='black')
        address_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=('Quicksand',12,'italic'))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)

        #10
        #teahername_label=Label(class_student_frame,text="Teacher Name",font=('Quicksand',12),background='#d8dbe2',foreground='black')
        #teahername_label.grid(row=4,column=2,padx=10,pady=10,sticky=W)

        #teahername_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=('Quicksand',12,'italic'))
        #teahername_entry.grid(row=4,column=3,padx=10,stick=W)


        #radiobutton
        self.var_radio1=StringVar()
        rb1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",value="Yes")
        rb1.grid(row=5,column=0)

        self.var_radio2=StringVar()
        rb2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio2, text="No Photo Sample",value="No")
        rb2.grid(row=5,column=2)

        '''back_button_2 = Button(self.root,command=self.exit,text="Back",cursor="hand2",font=('Quicksand',15),bg='Black',fg='white')
        back_button_2.place(relx=0.1, rely=0.9, anchor='center',width=220,height=40)'''

       






        #another

        button1_frame = LabelFrame(left_frame,bd=2)
        button1_frame.place(relx=0.1,rely=0.85,width=728,height=35)

        save_btn = Button(button1_frame,text="Save",command=self.add_data,font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        save_btn.grid(row=0,column=0)

        update_btn = Button(button1_frame,text="Update",command = self.update,font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(button1_frame,text="Delete",command=self.delete,font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(button1_frame,text="Reset",command=self.reset,font=('Quicksand',12),bg="deep sky blue",fg='white', width=19)
        reset_btn.grid(row=0,column=3)

        #takephoto_btn = Button(button_frame,text="Reset",font=('Quicksand',12),bg="deep sky blue",fg='white', width=38)
        #takephoto_btn.grid(row=1,column=0)

        button2_frame = LabelFrame(left_frame,bd=2)
        button2_frame.place(relx=0.1,rely=0.9,width=727,height=35)

        takephoto_btn = Button(button2_frame,text="Take Photo Sample",command=self.generate_dataset,font=('Quicksand',12),bg="deep sky blue",fg='white', width=80)
        takephoto_btn.grid(row=1,column=0)

        #upload_photo_btn = Button(button2_frame,text="Upload Photo Sample",font=('Quicksand',12),bg="deep sky blue",fg='white', width=39)
        #upload_photo_btn.grid(row=1,column=1)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white')
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


        



#Right frame
        #rright
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students", font=('Quicksand',12,'bold'),background='#d8dbe2')
        right_frame.place(relx=0.5,y=10,width=920,height=670)



    #table frame
        
        table_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,background='#d8dbe2')
        table_frame.place(relx=0.02,rely=0.1,width=880,height=460)


        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,columns=('department', 'course', 'year','sem', 'id', 'name', 'div', 'roll', 'gender', 'dob', 'email', 'phone','address'
                                                               ,'teacher','photo' ), xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('department',text="Department")
        self.student_table.heading('course',text="Course")
        self.student_table.heading('year',text="Year")
        self.student_table.heading('sem',text="Semester")
        self.student_table.heading('id',text="Student ID")
        self.student_table.heading('name',text="Name")
        self.student_table.heading('div',text="Divison")
        self.student_table.heading('roll',text="Roll NO")
        self.student_table.heading('gender',text="Gender")
        self.student_table.heading('dob',text="DOB")
        self.student_table.heading('email',text="Email")
        self.student_table.heading('phone',text="Phone")
        self.student_table.heading('address',text="Address")
        self.student_table.heading('teacher',text="Teacher")
        self.student_table.heading('photo',text="Photo Sample Status")
        self.student_table['show']='headings'

        self.student_table.column('department',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('year',width=100)
        self.student_table.column('sem',width=100)
        self.student_table.column('id',width=100)
        self.student_table.column('name',width=100)
        self.student_table.column('roll',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('div',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('email',width=100)
        self.student_table.column('phone',width=100)
        self.student_table.column('address',width=100)
        self.student_table.column('teacher',width=100)
        self.student_table.column('photo',width=150)
        



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



        
    #Function Declaration
    def add_data(self):
        if self.var_department.get()=='Select Department' or self.var_std_name.get=="" or self.var_std_id =="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_department.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),

                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Student Details has been added Successfully', parent = self.root)

            except Exception as e:
                messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )


    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
        my_cursor = conn.cursor()
        my_cursor.execute('select * from student')
        data = my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']

        self.var_department.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    def update(self):
        if self.var_department.get()=='Select Department' or self.var_std_name.get=="" or self.var_std_id =="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update","Do you want to Update Student Details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
                    my_cursor = conn.cursor()
                    my_cursor.execute('update student set department=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s', (

                                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()
                                                                                                                                                                                        ))
                else :
                    if not update:
                        return 
                
                messagebox.showinfo("Success","Student Details has been Updated Successfully",parent = self.root)
                    
                conn.commit()
                self.fetch_data()
                conn.close()


            except Exception as e:
                messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )


    def delete(self):
        if self.var_std_id.get()=='':
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete","Do you want to DELETE Student Details",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student Details has been Deleted Successfully",parent = self.root)

            
            except Exception as e:
                messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )

    def reset(self):
        self.var_department.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")




    def generate_dataset(self):
        if self.var_department.get()=='Select Department' or self.var_std_name.get=="" or self.var_std_id =="" :
            messagebox.showerror("Error","All Fields are Required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost',username='root',password='janhavikhadke', database='face_recognizer')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute('update student set department=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s', (

                                                                                                                                                                                            self.var_department.get(),
                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                            self.var_std_name.get(),
                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                            self.var_std_id.get()==id+1
                                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                if cv2.cuda.getCudaEnabledDeviceCount() > 0:
                    print("Using CUDA-accelerated GPU for face detection.")
                    face_clf = cv2.cuda.CascadeClassifier_gpu('haarcascade_frontalface_default.xml')
                else:
                    print("Using CPU for face detection (GPU not available).")
                    face_clf = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_clf.detectMultiScale(gray,1.3,5)

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame),(500,500))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = 'data/user.'+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Cropped Face',face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                
                 

                
                messagebox.showinfo("Done","Generating Datasets Completed...!",parent = self.root)

            except Exception as e :
                messagebox.showerror("Error",f'Due To : {str(e)}',parent=self.root  )

   

    

    def exit(self):
        self.root.destroy()
         

                        

                    





















if __name__ =="__main__":
    root=Tk()

    app = Student(root)
    root.configure(bg='lightblue')
    root.mainloop()