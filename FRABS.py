import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pygame
import pandas as pd
import time

sf = pd.read_csv('./datafile/Student03.csv')
studno = sf["Student No."].tolist()
firstname = sf["Name"].tolist()
"""lastname = ef["Last Name"].tolist()"""
photolocation = sf["Photo Location"].tolist()
audiolocation = sf["Audio Location"].tolist()
n = len(studno)
stud = []
stud_encod = []
audio = []



#path = 'Student'
#images = []
#classNames = []
for i in range(n):
    stud.append(face_recognition.load_image_file(photolocation[i]))
    stud_encod.append(face_recognition.face_encodings(stud[i])[0])
#print(stud_encod)    

def markAttendance(name):
    with open('./datafile/attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tString = time_now.strftime('%H:%M:%S')
            dString = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tString},{dString}')

encodeListKnown = stud_encod
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
       
        if matches[matchIndex]:
            name = firstname[matchIndex].upper()
            markAttendance(name)
            audioloc = audiolocation[matchIndex]
            pygame.mixer.init()
           
            if matchIndex ==-1:
                pygame.mixer.music.load(
                    "./datafile/StudentAudio/failure.mp3")
                pygame.mixer.music.play()
            else:
                time.sleep(2)
                pygame.mixer.music.load(audioloc)
                pygame.mixer.music.play()
               # pygame.mixer.music.queue(
                #    "./datafile/StudentAudio/attendance.mp3")
               # pygame.mixer.music.play()

            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 250, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
           
    cv2.imshow('webcam', img)
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindow()
