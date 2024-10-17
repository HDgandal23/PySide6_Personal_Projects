# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 361)
        MainWindow.setMaximumSize(QSize(300, 450))
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.main_label = QLabel(self.widget)
        self.main_label.setObjectName(u"main_label")
        self.main_label.setGeometry(QRect(10, 80, 281, 51))
        font = QFont()
        font.setFamilies([u"Palatino Linotype"])
        font.setPointSize(30)
        font.setBold(True)
        self.main_label.setFont(font)
        self.main_label.setAutoFillBackground(False)
        self.main_label.setStyleSheet(u"color: white;")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.main_label2 = QLabel(self.widget)
        self.main_label2.setObjectName(u"main_label2")
        self.main_label2.setEnabled(False)
        self.main_label2.setGeometry(QRect(8, 10, 281, 51))
        font1 = QFont()
        font1.setFamilies([u"Palatino Linotype"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.main_label2.setFont(font1)
        self.main_label2.setStyleSheet(u"color:white;")
        self.main_label2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 145, 281, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName(u"button_6")
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(17)
        self.button_6.setFont(font2)
        self.button_6.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_6, 1, 2, 1, 1)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName(u"button_7")
        self.button_7.setFont(font2)
        self.button_7.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_7, 0, 0, 1, 1)

        self.button_moins = QPushButton(self.gridLayoutWidget)
        self.button_moins.setObjectName(u"button_moins")
        self.button_moins.setFont(font2)
        self.button_moins.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_moins, 1, 3, 1, 1)

        self.button_division = QPushButton(self.gridLayoutWidget)
        self.button_division.setObjectName(u"button_division")
        self.button_division.setFont(font2)
        self.button_division.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_division, 3, 3, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName(u"button_9")
        self.button_9.setFont(font2)
        self.button_9.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_9, 0, 2, 1, 1)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")
        self.button_2.setFont(font2)
        self.button_2.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_2, 2, 1, 1, 1)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName(u"button_3")
        self.button_3.setFont(font2)
        self.button_3.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_3, 2, 2, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName(u"button_plus")
        self.button_plus.setFont(font2)
        self.button_plus.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_plus, 0, 3, 1, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName(u"button_0")
        self.button_0.setFont(font2)
        self.button_0.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_0, 3, 0, 1, 2)

        self.button_dote = QPushButton(self.gridLayoutWidget)
        self.button_dote.setObjectName(u"button_dote")
        self.button_dote.setFont(font2)
        self.button_dote.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_dote, 3, 2, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(u"button_1")
        self.button_1.setFont(font2)
        self.button_1.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_1, 2, 0, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName(u"button_5")
        self.button_5.setFont(font2)
        self.button_5.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_5, 1, 1, 1, 1)

        self.button_multi = QPushButton(self.gridLayoutWidget)
        self.button_multi.setObjectName(u"button_multi")
        self.button_multi.setFont(font2)
        self.button_multi.setStyleSheet(u"background-color: #EEA10C;\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_multi, 2, 3, 1, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName(u"button_4")
        self.button_4.setFont(font2)
        self.button_4.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_4, 1, 0, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName(u"button_8")
        self.button_8.setFont(font2)
        self.button_8.setStyleSheet(u"background-color: rgb(42, 50, 46);\n"
"color: white;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_8, 0, 1, 1, 1)

        self.button_clear = QPushButton(self.gridLayoutWidget)
        self.button_clear.setObjectName(u"button_clear")
        self.button_clear.setFont(font2)
        self.button_clear.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_clear, 4, 0, 1, 2)

        self.button_equal = QPushButton(self.gridLayoutWidget)
        self.button_equal.setObjectName(u"button_equal")
        self.button_equal.setFont(font2)
        self.button_equal.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 50px;")

        self.gridLayout.addWidget(self.button_equal, 4, 2, 1, 2)

        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.main_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.main_label2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_moins.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.button_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_dote.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.button_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.button_multi.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.button_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

