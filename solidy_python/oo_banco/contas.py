from cliente import Clientes

class Contas():

	def __init__(self, cliente, saldo, limite):
		Clientes.__init__(nome, cpf, idade)
		self.cliente = cliente
		self.saldo = saldo
		self.limite = limite

	def sacar(self, saque):
		self.saldo -= saque
		pass

	def depositar(self, deposito):
		self.saldo += deposito
		pass

	def saldo(self):
		print(self.saldo)
		pass