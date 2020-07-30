# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setDocumentMode(False)
        self.mainPage = QWidget(MainWindow)
        self.mainPage.setObjectName(u"mainPage")
        self.mainPageGrid = QGridLayout(self.mainPage)
        self.mainPageGrid.setObjectName(u"mainPageGrid")
        self.StartPB = QPushButton(self.mainPage)
        self.StartPB.setObjectName(u"StartPB")
        self.StartPB.setLayoutDirection(Qt.LeftToRight)
        self.StartPB.setAutoDefault(False)
        self.StartPB.setFlat(True)

        self.mainPageGrid.addWidget(self.StartPB, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.mainPageGrid.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.StopPB = QPushButton(self.mainPage)
        self.StopPB.setObjectName(u"StopPB")
        self.StopPB.setLayoutDirection(Qt.LeftToRight)
        self.StopPB.setFlat(True)

        self.mainPageGrid.addWidget(self.StopPB, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.mainPage)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StartPB.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.StopPB.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

