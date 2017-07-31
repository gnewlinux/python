import sys
from PyQt5 import QtWidgets, QtGui

def window():
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QWidget()
	w.setWindowTitle('Treinamento PyQt')
	
	v_box = QtWidgets.QVBoxLayout()
	h_box = QtWidgets.QHBoxLayout()

	l = QtWidgets.QLabel('Hello, World!')
	b = QtWidgets.QPushButton('Clique aqui')
	

	h_box.addStretch()
	h_box.addWidget(l)
	h_box.addStretch()

	v_box.addWidget(b)
	v_box.addLayout(h_box)

	w.setLayout(v_box)

	w.show()
	sys.exit(app.exec_())

window()