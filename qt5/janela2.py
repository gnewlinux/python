import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.setWindowTitle('PyQt4 Lesson 2')
	w.setGeometry(100,100,300,230)

	l1 = QtWidgets.QLabel(w)
	l2 = QtWidgets.QLabel(w)

	l1.move(113,40)
	l2.move(90,50)

	l1.setText('Hello, World!')
	l2.setPixmap(QtGui.QPixmap('mozilla_firefox.png'))

	w.show()
	sys.exit(app.exec_())

window()