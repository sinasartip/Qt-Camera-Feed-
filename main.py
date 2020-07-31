import PySide2
from PySide2 import QtWidgets
from PySide2.QtCore import QThread, SIGNAL, Signal, Slot, QObject

import Ui_main
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import cv2
import numpy as np
import queue
from threading import Thread

class signals(QObject):
    image = Signal(object)


class PlotThread(QThread):
    def __init__(self,GUI):
        QThread.__init__(self)
        self.GUI = GUI
        self.signal = signals()

        #setup of graphing widget
        self.graphWidget = pg.ImageView()
        self.graphWidget.show()
        self.GUI.addWidget(self.graphWidget,0,0,1,3)

        #flags & queues
        self.stopped = False
        
        
        
        
        

    def __del__(self):
        self.wait()

   
    def run(self,image):

        #setup flag
        self.stopped = False

        #continoulsy grab images 
        self.graphWidget.setImage(image)

class camThread(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.stopped = False
        self.signal = signals()
        
        

    def __del__(self):
        self.wait()

    @Slot()
    def run(self):
        #setup flag
        self.stopped = False
        #capture webcam images
        cap = cv2.VideoCapture(0)
        while(not self.stopped):
            # Capture frame-by-frame
            _, frame = cap.read()
        
            self.signal.image.emit(frame)
            
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
      
        
        self.plot_thread = PlotThread(self.mainPageGrid)

        #setup signals and slotes 
        self.cam_thread = camThread() #camera feed thread
        self.StartPB.clicked.connect(self.cam_thread.start)#start push button sends camera feed signal
        self.cam_thread.signal.image.connect(self.plot_thread.run)
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
