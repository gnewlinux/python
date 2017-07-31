#!/usr/bin/env python3

from veiculo import Veiculo

fusca = Veiculo('branco', 'WW', 4)
caminhao = Veiculo('azul', 'Ford', 12)
moto = Veiculo('vermelha', 'Honda', 2)

fusca.metodo()

print('fusca', fusca, '\ncaminhao', caminhao, '\nmoto', moto)