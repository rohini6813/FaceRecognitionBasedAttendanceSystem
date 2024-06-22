from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root) -> None:
        self.root = root
        self.root.geometry("1920x1020+0+0")
        self.root.title("Trainingthe Dataset")
        self.root.configure(background='lightblue')
        self.root.configure(bg='lightblue')

        name_lbl=Label(self.root,text="TRAIN DATA",font=('Times New Roman',36,'bold'),fg='#154c79',bg='lightblue')
        name_lbl.place(relx=0.5, rely=0.05, anchor='center')


        train_button = Image.open(r"images\train.jpg")
        train_button = train_button.resize((440,440))
        self.phototrain_button = ImageTk.PhotoImage(train_button)

        train_button_1= Button(self.root,image = self.phototrain_button,cursor="hand2")
        train_button_1.place(relx=0.5, rely=0.4, anchor='center',width=440,height=440)

        train_button_2 = Button(self.root,text="TRAIN THE DATA ",command=self.train_classifier,cursor="hand2",font=('Quicksand',15),bg='Black',fg='white')
        train_button_2.place(relx=0.5, rely=0.65, anchor='center',width=720,height=40)

        close_button_2 = Button(self.root,command=self.exit,text="Close",cursor="hand2",font=('Quicksand',15),bg='black',fg='white',borderwidth=5)
        close_button_2.place(relx=0.5, rely=0.9, anchor='center',width=220,height=40)


    def exit(self):
        self.root.destroy()


    def train_classifier(self):
        data = ('data')
        path = [os.path.join(data,file) for file in os.listdir(data)]
        faces = []
        ids = []


        for image in path:
            img = Image.open(image).convert('L')
            imagenp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow('Training',imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #training classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Successful",parent=self.root)


if __name__ =="__main__":
    root=Tk()

    app = Train(root)
    
    root.mainloop()