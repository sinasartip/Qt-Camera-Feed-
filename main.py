import PySide2
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, SIGNAL
import Ui_main
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import cv2
import numpy as np
import queue
from threading import Thread

class PlotThread(QThread):
    def __init__(self,GUI,imgQueue):
        QThread.__init__(self)
        self.GUI = GUI

        #setup of graphing widget
        self.graphWidget = pg.ImageView()
        self.graphWidget.show()
        self.GUI.addWidget(self.graphWidget,0,0,1,3)

        #flags & queues
        self.stopped = False
        self.imgQueue = imgQueue
        
        
        
        

    def __del__(self):
        self.wait()

    def run(self):
        

        #setup flag
        self.stopped = False

        #continoulsy grab images 
        while not self.stopped:
            #print("plotting")
            self.graphWidget.setImage(self.imgQueue.get())
            self.sleep(0.1)
       

        print("Exited thread graph!")

class camThread(QThread):
    def __init__(self, imgQueue):
        QThread.__init__(self)
        self.stopped = False
        self.imgQueue = imgQueue

    def __del__(self):
        self.wait()

    def run(self):
        #setup flag
        self.stopped = False
        #capture webcam images
        cap = cv2.VideoCapture(0)
        while(not self.stopped):
            # Capture frame-by-frame
            _, frame = cap.read()
           
            self.imgQueue.put(frame)
            #print("capturing")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                pass

        # When everything done, release the capture
        cap.release()
        print("Exited thread capture!")
        


class GraphingApp(Ui_main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(GraphingApp,self).__init__()
        self.setupUi(self)

        #flags
        self.stopped = False
        
        ###page 1###
        
        #init graphing widget
        self.imgQueue = queue.Queue(5)
        
        self.plot_thread = PlotThread(self.mainPageGrid,self.imgQueue)

        #setup signals and slotes 
        self.cam_thread = camThread(self.imgQueue) #camera feed thread
        self.connect(self.cam_thread,SIGNAL("started()"), self.plot_thread.start()) #camera feed signals plotting thread
        self.StartPB.clicked.connect(self.cam_thread.start) #start push button sends camera feed signal
        self.StopPB.clicked.connect(self.stop) 
    
    def stop(self): 
        self.stopped = True
        self.cam_thread.stopped = True
        self.plot_thread.stopped = True

    
                

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    

    qt_app = GraphingApp()
    qt_app.show()
    app.exec_()
