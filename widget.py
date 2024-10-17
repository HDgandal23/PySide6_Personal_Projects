from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton
from ui_widget import Ui_MainWindow




class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculatrice")
        self.setMaximumWidth(300)
        self.setMinimumWidth(300)
        self.setMaximumHeight(360)




        # call the buttons

        self.button_0.clicked.connect(self.on_button_clicked)
        self.button_1.clicked.connect(self.on_button_clicked)
        self.button_2.clicked.connect(self.on_button_clicked)
        self.button_3.clicked.connect(self.on_button_clicked)
        self.button_4.clicked.connect(self.on_button_clicked)
        self.button_5.clicked.connect(self.on_button_clicked)
        self.button_6.clicked.connect(self.on_button_clicked)
        self.button_7.clicked.connect(self.on_button_clicked)
        self.button_8.clicked.connect(self.on_button_clicked)
        self.button_9.clicked.connect(self.on_button_clicked)
        self.button_dote.clicked.connect(self.on_button_clicked)
        self.button_plus.clicked.connect(self.on_button_clicked)
        self.button_clear.clicked.connect(self.on_button_clicked)
        self.button_equal.clicked.connect(self.on_button_clicked)
        self.button_moins.clicked.connect(self.on_button_clicked)
        self.button_multi.clicked.connect(self.on_button_clicked)
        self.button_division.clicked.connect(self.on_button_clicked)


    # Logics Methode

    def on_button_clicked(self):
        button = self.sender()
        current_text = self.main_label.text()

        if current_text == "0":
            current_text = ""

        if button.text() == "=":

            try:
                result = str(eval(current_text))
                self.main_label.setText(result)
                self.main_label2.setText(current_text + button.text())

            except ZeroDivisionError:
                self.main_label.setText("Error : impossible de diviser par 0 !")

            except Exception as e:
                self.main_label.setText("Exception error")

        else:
            self.main_label.setText(current_text + button.text())
            self.main_label2.setText(current_text + button.text())

        if button.text() == "c":
            self.main_label.setText("0")
            self.main_label2.setText("")




