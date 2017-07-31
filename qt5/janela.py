import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.setWindowTitle('PyQt4 Lesson 2')
	w.show()
	sys.exit(app.exec_())

window()