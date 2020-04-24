
#Main Window of the GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from Widget import*
import sys 
import numpy as np
import os
import cv2
import imutils
import pickle
import face_recognition

class Ui_MainWindow(object):

    def clicked_new_employee(self):
        self.window = QtWidgets.QWidget()
        self.ui= Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def recognition(self):
        encoding = "Insert the path of the encodings folder here with the addition \\encoding1.pickle " # example : "C:\\Users\XYZ\\SIDDHI\\Desktop\\encodings\\encoding1.pickle"
        data = pickle.loads(open(encoding, "rb").read())
        print(data)
        cap = cv2.VideoCapture(0)
  
        if cap.isOpened :
            ret, frame = cap.read()
        else:
            ret = False
        while(ret):
            ret, frame = cap.read()
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=400)
            r = frame.shape[1] / float(rgb.shape[1])

            boxes = face_recognition.face_locations(rgb, model= "hog")
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []
        
            for encoding in encodings:
                        matches = face_recognition.compare_faces(np.array(encoding),np.array(data["encodings"]))
                        name = "Unknown"
                    
                        if True in matches:
                            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                            counts = {}
                        
                            
                            for i in matchedIdxs:
                                name = data["names"][i]
                                counts[name] = counts.get(name, 0) + 1
                                name = max(counts, key=counts.get)
                        names.append(name)
                        
            for ((top, right, bottom, left), name) in zip(boxes, names):
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r) 
                left = int(left * r)
                cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) == 27:
                break                                                

        cv2.destroyAllWindows()

        cap.release()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 572)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcome_label = QtWidgets.QLabel(self.centralwidget)
        self.welcome_label.setGeometry(QtCore.QRect(280, 110, 231, 71))
        self.welcome_label.setStyleSheet("background-color:black;\n"
"color:white;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.NewEmpbtn = QtWidgets.QPushButton(self.centralwidget)
        self.NewEmpbtn.setGeometry(QtCore.QRect(140, 300, 191, 41))
        self.NewEmpbtn.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.NewEmpbtn.setObjectName("NewEmpbtn")
        self.NewEmpbtn.clicked.connect(self.clicked_new_employee)
        self.accessbtn = QtWidgets.QPushButton(self.centralwidget)
        self.accessbtn.setGeometry(QtCore.QRect(500, 300, 191, 41))
        self.accessbtn.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style:outset;\n"
"border-width:2px; \n"
"border-radius: 10px;\n"
"border-color:black;\n"
"font:bold 14px;\n"
"padding:6px;\n"
"min-width:10px;")
        self.accessbtn.setObjectName("accessbtn")
        self.accessbtn.clicked.connect(self.recognition)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_label.setText(_translate("MainWindow", "WELCOME"))
        self.NewEmpbtn.setText(_translate("MainWindow", "New Employee"))
        self.accessbtn.setText(_translate("MainWindow", "Access"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


