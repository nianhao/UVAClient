import socket
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

qtCreatorFile="send.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(qtCreatorFile)
class MyApp(QWidget,Ui_MainWindow):
    def __init__(self):
        QWidget.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #绑定事件
        self.eventBind()

    #事件绑定
    def eventBind(self):
        self.pushButton_send.clicked.connect(self.sendMessage)
    def sendMessage(self):
        ip = self.lineEdit_IP.text()
        message=self.textEdit_message.toPlainText()
        print(ip,'\n',message)
        ip,port=ip.split(':')
        address=(ip,int(port))
        print(address)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(message,encoding="utf-8"),address)
        except Exception as e:
            print(e)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())