from tkinter import *
from tkinter import ttk, filedialog
import mysql.connector
import cv2
import os
from time import strftime
from datetime import datetime
from mtcnn import MTCNN
import csv
import pandas as pd
from teacher_data import teacher_data

class Attendance2:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Face Recognition")
        self.root.configure(background='lightblue')

        self.var_div = StringVar()
        self.var_semester = StringVar()
        self.var_teacher = StringVar()
        self.var_subject = StringVar()
        self.var_branch = StringVar()

        name_lbl = Label(self.root, text="Take Attendance ", font=('Quicksand', 36), fg='black', bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')

        teacher_label = Label(self.root, text="Teacher Name", font=('Quicksand', 12), background='lightblue', foreground='black')
        teacher_label.place(relx=0.35, rely=0.1)

        teacher_entry = ttk.Entry(self.root, textvariable=self.var_teacher, width=60, font=('Quicksand', 12, 'italic'))
        teacher_entry.place(relx=0.35, rely=0.125)

        dpt_label = Label(self.root, text="Department", font=('Quicksand', 12), background='lightblue', foreground='black')
        dpt_label.place(relx=0.35, rely=0.2)

        dep_combo = ttk.Combobox(self.root, textvariable=self.var_branch, font=('Quicksand', 12, 'italic'), width=58, state='readonly')
        dep_combo['values'] = ('Select Department', "Computer", "IT", 'Civil', 'Mechanical')
        dep_combo.current(0)
        dep_combo.place(relx=0.35, rely=0.225)

        div_label = Label(self.root, text="Division", font=('Quicksand', 12), background='lightblue', foreground='black')
        div_label.place(relx=0.35, rely=0.3)

        div_combo = ttk.Combobox(self.root, textvariable=self.var_div, font=('Quicksand', 12, 'italic'), width=58, state='readonly')
        div_combo['values'] = ('Select Division', "A", "B", "C", "D")
        div_combo.current(0)
        div_combo.place(relx=0.35, rely=0.325)

        semester_label = Label(self.root, text="Semester", font=('Quicksand', 12), background='lightblue', foreground='black')
        semester_label.place(relx=0.35, rely=0.4)

        dep_combo = ttk.Combobox(self.root, textvariable=self.var_semester, font=('Quicksand', 12, 'italic'), width=58, state='readonly')
        dep_combo['values'] = ('Select Department', "1", "2", '3', '4')
        dep_combo.current(0)
        dep_combo.place(relx=0.35, rely=0.425)

        subject_label = Label(self.root, text="Subject", font=('Quicksand', 12), background='lightblue', foreground='black')
        subject_label.place(relx=0.35, rely=0.5)

        subject_entry = ttk.Entry(self.root, textvariable=self.var_subject, width=60, font=('Quicksand', 12, 'italic'))
        subject_entry.place(relx=0.35, rely=0.525)

        take_photo_btn = Button(self.root, command=self.photo_atd, text="Upload A Photo", font=('Quicksand', 12), bg="deep sky blue", fg='white', width=30)
        take_photo_btn.place(relx=0.35, rely=0.6)

        take_photo_btn = Button(self.root, command=self.video_atd, text="Upload A Video", font=('Quicksand', 12), bg="deep sky blue", fg='white', width=30)
        take_photo_btn.place(relx=0.49, rely=0.6)

        open_cam = Button(self.root, command=self.face_recog, text="Video Camera", font=('Quicksand', 12), bg="deep sky blue", fg='white', width=60)
        open_cam.place(relx=0.35, rely=0.63)

        take_attendance_btn = Button(self.root, command=self.face_recog, text="Take Attendance", font=('Quicksand', 12), bg="green", fg='white', width=60)
        take_attendance_btn.place(relx=0.35, rely=0.7)

        self.var_teacher.set(teacher_data[0])
        self.var_branch.set(teacher_data[1])
        self.var_semester.set(teacher_data[2])
        self.var_subject.set(teacher_data[3])

        close_button_2 = Button(self.root, command=self.exit, text="Close", cursor="hand2", font=('Quicksand', 15), bg='black', fg='white', borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center', width=220, height=40)

    def exit(self):
        self.root.destroy()

    def mark_attendance(self, i, r, n, d):
        name = teacher_data[0]
        branch = teacher_data[1]
        semester = teacher_data[2]
        subject = teacher_data[3]

        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dString = now.strftime("%H:%M:%S")

        if not os.path.exists("atd.csv"):
            with open("atd.csv", "a", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerow(["Student ID", "Roll", "Name", "Department", "Semester", "Division", "Teacher", "Subject", "Time", "Date", "Attendance"])

        with open("atd.csv", "a", newline="\n") as f:
            writer = csv.writer(f)
            writer.writerow([i, r, n, branch, semester, self.var_div.get(), name, subject, dString, d1, "Present"])

    def generate_excel(self):
        df = pd.read_csv("atd.csv")
        df.to_excel("attendance.xlsx", index=False)

    def fetch_student_details(self, id, cursor):
        cursor.execute("SELECT Name, Roll, department FROM student WHERE Student_id = %s", (id,))
        result = cursor.fetchone()

        if result:
            return {
                'Name': str(result[0]),
                'Roll': str(result[1]),
                'department': str(result[2])
            }
        else:
            return {
                'Name': '',
                'Roll': '',
                'department': ''
            }

    def draw_boundary(self, img, classifier, scalefactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        coord = []

        if isinstance(classifier, MTCNN):
            features = classifier.detect_faces(img)
            for feature in features:
                if len(feature['box']) != 4:
                    continue
                x, y, w, h = feature['box']
                x -= 10
                y -= 10
                w += 20
                h += 20

                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - pred / 300))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="janhavikhadke", database="face_recognizer")
                my_cursor = conn.cursor()

                details = self.fetch_student_details(id, my_cursor)
                conn.close()

                if confidence > 80:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    cv2.putText(img, f"Student ID: {id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                    for i, (key, val) in enumerate(details.items()):
                        cv2.putText(img, val, (x, y-30+25*i), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                    self.mark_attendance(id, details['Roll'], details['Name'], details['Department'])
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                coord = [x, y, w, h]
        else:
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)
            for (x, y, w, h) in features:
                id, pred = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100 * (1 - pred / 300))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="janhavikhadke", database="face_recognizer")
                my_cursor = conn.cursor()

                details = self.fetch_student_details(id, my_cursor)
                conn.close()

                if confidence > 80:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    cv2.putText(img, f"Student ID: {id}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                    for i, (key, val) in enumerate(details.items()):
                        cv2.putText(img, val, (x, y-30+25*i), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 1)
                    self.mark_attendance(id, details['Roll'], details['Name'], details['department'])
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)
                coord = [x, y, w, h]

        return coord
    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_capture.read()
            if not ret:
                break
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        self.generate_excel()

    def photo_atd(self):
        photo_path = filedialog.askopenfilename()
        if not photo_path:
            return
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        img = cv2.imread(photo_path)
        if img is None:
            return
        
        img = self.recognize(img, clf, faceCascade)
        cv2.imshow("Photo Attendance", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.generate_excel()

    def video_atd(self):
        video_path = filedialog.askopenfilename()
        if not video_path:
            return
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(video_path)
        if not video_capture.isOpened():
            return

        while True:
            ret, img = video_capture.read()
            if not ret:
                break
            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Video Attendance", img)
            
            if cv2.waitKey(1) == 13:
                break

        video_capture.release()
        cv2.destroyAllWindows()
        self.generate_excel()
if __name__ =='__main__':
    root = Tk()
    app = Attendance2(root)
    root.configure(bg='lightblue')
    root.mainloop()