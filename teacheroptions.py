from tkinter import *
from attendance import Attendance2
from attendance_files import Excel
import os
from teacher_data import teacher_data
from PIL import Image, ImageTk
import re 
import shutil


class ChooseOperations:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title('Login')
        self.root.configure(background='lightblue')
        
        

        name_lbl=Label(self.root,text="Choose Operation",font=('Quicksand',36),fg='black',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')


        take_atd_button = Image.open(r"images\attendance3.png")
        take_atd_button = take_atd_button.resize((220,220))
        self.phototake_atd_button = ImageTk.PhotoImage(take_atd_button)
        take_atd_button_1 = Button(self.root,image = self.phototake_atd_button,command=self.take_attendance,cursor="hand2",bg="white")
        take_atd_button_1.place(relx=0.25, rely=0.4, anchor='center',width=220,height=220)

        take_atd_button_2 = Button(self.root,text="Take Attendance",command=self.take_attendance,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        take_atd_button_2.place(relx=0.25, rely=0.52, anchor='center',width=220,height=40)

        '''take_attendance_btn = Button(self.root,text="Take Attendance",command=self.take_attendance,font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        take_attendance_btn.place(relx = 0.4,rely=0.4)'''

        gen_file_button = Image.open(r"images\generate.png")
        gen_file_button = gen_file_button.resize((220,220))
        self.photogen_file_button = ImageTk.PhotoImage(gen_file_button)
        gen_file_button_1 = Button(self.root,image = self.photogen_file_button,command=self.gen_files,cursor="hand2",bg="white")
        gen_file_button_1.place(relx=0.50, rely=0.4, anchor='center',width=220,height=220)

        gen_file_button_2 = Button(self.root,text="Generate Files",command=self.gen_files,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        gen_file_button_2.place(relx=0.50, rely=0.52, anchor='center',width=220,height=40)

        '''generate_files_btn = Button(self.root,text="Generate Attendance Files",command=self.gen_files,font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        generate_files_btn.place(relx = 0.4,rely=0.5)'''

        show_files_button = Image.open(r"images\files.png")
        show_files_button = show_files_button.resize((220,220))
        self.photoshow_files_button = ImageTk.PhotoImage(show_files_button)
        show_files_button_1 = Button(self.root,image = self.photoshow_files_button,command=self.read_file_path,cursor="hand2",bg="white")
        show_files_button_1.place(relx=0.750, rely=0.4, anchor='center',width=220,height=220)

        show_files_button_2 = Button(self.root,text="Show Files",command=self.read_file_path,cursor="hand2",font=('Quicksand',15),bg='Crimson',fg='white')
        show_files_button_2.place(relx=0.750, rely=0.52, anchor='center',width=220,height=40)

        '''show_files_button = Button(self.root,text="Show Attendance Files",command=self.show_files,font=('Quicksand',12),bg="deep sky blue",fg='white', width=40)
        show_files_button.place(relx = 0.4,rely=0.6)'''

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)

    def exit(self):
        self.root.destroy()


    def gen_files(self):
        self.new_window = Toplevel(self.root)
        self.app = Excel(self.new_window)

    def take_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance2(self.new_window)
        
    
    def read_file_path(self):
        name = teacher_data[0]
        attendance_dir = 'Attendance_Sheets'
        teacher_files_dir = 'Teacher Files'

        # Ensure 'Teacher Files' directory exists
        if not os.path.exists(teacher_files_dir):
            os.makedirs(teacher_files_dir)

        # Clear 'Teacher Files' directory
        for file in os.listdir(teacher_files_dir):
            file_path = os.path.join(teacher_files_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)

        # Search for files in 'Attendance_Sheets' and copy them
        for file in os.listdir(attendance_dir):
            match = re.search(name, file)
            if match:
                source_file = os.path.join(attendance_dir, file)
                destination_file = os.path.join(teacher_files_dir, file)
                shutil.copy(source_file, destination_file)

        os.startfile(r'Teacher Files')
        
    
    


if __name__ =="__main__":
    root=Tk()

    app = ChooseOperations(root)
    root.configure(bg='lightblue')
    root.mainloop()