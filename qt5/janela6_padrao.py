import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):

	def __init__(self):
		super().__init__()

		self.init_ui()

	def init_ui(self):


		self.setWindowTitle('Titulo Janela')
		self.show()

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())