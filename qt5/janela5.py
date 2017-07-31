import sys
from PyQt5 import QtWidgets, QtGui

class Windows(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):
		self.b = QtWidgets.QPushButton('Clique aqui')
		self.l = QtWidgets.QLabel('Voce ainda não clicou')

		h_box = QtWidgets.QHBoxLayout()
		h_box.addStretch()
		h_box.addWidget(self.l)
		h_box.addStretch()

		v_box = QtWidgets.QVBoxLayout()
		v_box.addWidget(self.b)
		v_box.addLayout(h_box)

		self.setLayout(v_box)
		self.setWindowTitle('Clique!')

		self.b.clicked.connect(self.btn_click)

		self.show()

	def btn_click(self):
		self.l.setText('Fui clicado! :)')

app = QtWidgets.QApplication(sys.argv)
a_window = Windows()
sys.exit(app.exec_())