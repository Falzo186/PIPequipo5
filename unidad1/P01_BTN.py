import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile= "P01.ui"
Ui_MainWindow,QtBaseClse = uic.loadUiType(qtCreatorFile)
class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
       QtWidgets.QMainWindow.__init__(self)
       Ui_MainWindow.__init__(self)
       self.setupUi(self)

       self.BTN_SALUDO.clicked.connect(self.saludar)
   def saludar(self):
       print("hola")

if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())
