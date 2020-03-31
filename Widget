#Wiget for GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWin import*
import sys 
import numpy as np
import os
import cv2
import imutils.paths as paths
import face_recognition
import pickle

class Ui_Form(object):
    def dataset(self):
        face_cascade = cv2.CascadeClassifier('C:\\Users\\SIDDHI\\Desktop\\python\\PP project\\cascades\\data\\haarcascade_frontalface_default.xml')

        cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
        path = "C:\\Users\\SIDDHI\\Desktop\\python\\PP project\\siddhi\\dataset\\"# path were u want store the data set
        id =self.id_enter.text()
        try:
            # Create target Directory
            os.mkdir(path+str(id))
            print("Directory " , path+str(id),  " Created ") 
        except FileExistsError:
            print("Directory " , path+str(id) ,  " already exists")
        sampleN=0;
        
        while 1:

            ret, img = cap.read()
            frame = img.copy()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x,y,w,h) in faces:

                sampleN=sampleN+1;

                cv2.imwrite(path+str(id)+ "\\" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])

                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

                cv2.waitKey(100)

            cv2.imshow('img',img)

            cv2.waitKey(1)

            if sampleN > 40:
                break
            
        cap.release()
        
        cv2.destroyAllWindows() 


    def train(self):
        dataset = "C:\\Users\\SIDDHI\\Desktop\\python\\PP project\\siddhi\\dataset\\"# path of the data set 
        module = r"C:\Users\SIDDHI\Desktop\python\PP project\siddhi\encodings\encoding1.pickle" # were u want to store the pickle file 

        imagepaths = list(paths.list_images(dataset))
        knownEncodings = []
        knownNames = []
        for (i, imagePath) in enumerate(imagepaths):
            print("[INFO] processing image {}/{}".format(i + 1,len(imagepaths)))
            name = imagePath.split(os.path.sep)[-2]
            image = cv2.imread(imagePath)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)	
            boxes = face_recognition.face_locations(rgb, model= "hog")
            encodings = face_recognition.face_encodings(rgb, boxes)
            for encoding in encodings:
                knownEncodings.append(encoding)
                knownNames.append(name)
                print("[INFO] serializing encodings...")
                data = {"encodings": knownEncodings, "names": knownNames}
                output = open(module, "wb") 
                pickle.dump(data, output)
                output.close()   

    def GoToMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(704, 509)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        Form.setFont(font)
        self.datasetbtn = QtWidgets.QPushButton(Form)
        self.datasetbtn.setGeometry(QtCore.QRect(240, 220, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.datasetbtn.setFont(font)
        self.datasetbtn.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.datasetbtn.setObjectName("datasetbtn")
        self.datasetbtn.clicked.connect(self.dataset)
        self.label_employee_id = QtWidgets.QLabel(Form)
        self.label_employee_id.setGeometry(QtCore.QRect(150, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_employee_id.setFont(font)
        self.label_employee_id.setObjectName("label_employee_id")
        self.id_enter = QtWidgets.QLineEdit(Form)
        self.id_enter.setGeometry(QtCore.QRect(280, 100, 171, 31))
        self.id_enter.setObjectName("id_enter")
        self.trainbtn = QtWidgets.QPushButton(Form)
        self.trainbtn.setGeometry(QtCore.QRect(240, 290, 221, 41))
        self.trainbtn.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.trainbtn.setObjectName("trainbtn")
        self.trainbtn.clicked.connect(self.train)
        self.MainMenubtn = QtWidgets.QPushButton(Form)
        self.MainMenubtn.setGeometry(QtCore.QRect(240, 370, 221, 41))
        self.MainMenubtn.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.MainMenubtn.setObjectName("MainMenubtn")
        self.MainMenubtn.clicked.connect(self.GoToMenu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.datasetbtn.setText(_translate("Form", "Data Set"))
        self.label_employee_id.setText(_translate("Form", "Employee ID:"))
        self.trainbtn.setText(_translate("Form", "Train"))
        self.MainMenubtn.setText(_translate("Form", "Go to Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
