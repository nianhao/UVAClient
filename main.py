import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QWidget

qtCreatorFile="send.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QWidget,Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())