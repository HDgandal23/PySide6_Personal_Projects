from PySide6.QtWidgets import QApplication
from widget import MyWidget
import  sys


app = QApplication(sys.argv)


window = MyWidget()
window.show()
app.exec()
