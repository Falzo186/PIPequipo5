import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile= "P02.ui"
Ui_MainWindow,QtBaseClse = uic.loadUiType(qtCreatorFile)
class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
       QtWidgets.QMainWindow.__init__(self)
       Ui_MainWindow.__init__(self)
       self.setupUi(self)

       self.BTN_SALUDO.clicked.connect(self.saludar)


   def saludar(self):
       self.msj(self ,"hola")

   def msj(self    ,txt):
       m = QtWidgets.QMessageBox()
       m.setText(txt)
       m.exec_()

if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())