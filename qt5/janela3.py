import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.setWindowTitle('Treinamento PyQt')
	w.setGeometry(100,100,300,240)

	l1 = QtWidgets.QLabel(w)
	l2 = QtWidgets.QLabel(w)
	b = QtWidgets.QPushButton(w)

	l1.move(113,40)
	l2.move(90,50)
	b.move(112,185)

	l1.setText('Hello, World!')
	l2.setPixmap(QtGui.QPixmap('mozilla_firefox.png'))
	b.setText('Clique aqui')

	w.show()
	sys.exit(app.exec_())

window()