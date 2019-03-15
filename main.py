import socket
import sys
from time import sleep

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

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
        self.pushButton_selectFile.clicked.connect(self.selectFile)
        self.pushButton_sendFile.clicked.connect(self.sendFile)
     #发送消息
    def sendMessage(self):
        '''
        新建一个UDP协议的socket，将消息发送到目标地址
        :return:
        '''
        #获取ip
        ip = self.lineEdit_IP.text()
        #获取消息内容
        message=self.textEdit_message.toPlainText()
        #print(ip,'\n',message)
        #构建地址
        ip,port=ip.split(':')
        address=(ip,int(port))
        #print(address)
        #发送消息
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(bytes(message,encoding="utf-8"),address)
            s.close()
        except Exception as e:
            print(e)
    def selectFile(self):
        '''
        选择要发送的文件
        :return:文件名
        '''
        #打开文件选择对话框
        fileName,state= QFileDialog.getOpenFileName(self,self.tr("选择发送的文件"),"",self.tr("All File (*.*)"))
        #print(fileName,state)
        self.label_fileName.setText(fileName)
        return fileName
    def createUDPSocket(self):
        # 获取ip
        ip = self.lineEdit_IP.text()
        # 获取消息内容
        message = self.textEdit_message.toPlainText()
        # print(ip,'\n',message)
        # 构建地址
        ip, port = ip.split(':')
        address = (ip, int(port))
        # print(address)
        # 发送消息
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except Exception as e:
            s=None
            print(e)
        return s,address
    def yiledFile(self,fileName, length):
        try:
            with open(fileName,"rb") as f:
                content=f.read(length)
                while(content):
                    yield content
                    content=f.read(length)
        except Exception as e:
            print(e)


    def sendFile(self):
        #首先判断是否有文件发送
        if self.label_fileName.text()=="文件名":
            fileName=self.selectFile()
        else:
            fileName=self.label_fileName.text()
        #print(fileName)
        #创建socket
        udpScoket,address=self.createUDPSocket()
        count=0;
        for fileSegment in  self.yiledFile(fileName,1024):
            count+=1
            udpScoket.sendto(fileSegment,address)
            sleep(0.005)
            #print("发送到{0}\n{1}".format(address,fileSegment))
            print(count*1024)

        print(count*1024)
        udpScoket.close()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec_())