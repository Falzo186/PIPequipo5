import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile="unidad1/P00_intro.ui"
Ui_MainWindow,QtBaseClse = uic.loadUiType(qtCreatorFile)
class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
   def __init__(self):
       QtWidgets.QMainWindow.__init__(self)
       Ui_MainWindow.__init__(self)
       self.setupUi(self)


if __name__ =="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())
