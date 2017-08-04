#!/usr/bin/env python3
import json
import requests
from termcolor import colored, cprint
from subprocess import call

# limpa tela
call(['clear'])

while True:
	cidade = input('Digite a cidade ou S para sair: ')
	print('------------------------')

	# exit
	if cidade in ['s','S']:
		cprint('bye, bye...\n', 'green')
		break

	# API REQUEST
	requisicao = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+cidade+'&APPID=43a336c821d5e8e79037e56e24941f97')
	# conversao json
	tempo = json.loads(requisicao.text)

	if tempo['cod'] == 200:
		tempo_convertido = tempo['weather'][0]['main']
		tempo_float = float(tempo['main']['temp']) - 273.15

		# traducao
		dicionario = {"Clear":"Limpo", "Clouds":"Nublado", "Rain":"Chuva"}

		if tempo_convertido in dicionario:
			tempo_convertido = dicionario[tempo_convertido]

		cprint('Condicao do tempo: ' + tempo_convertido, 'green')
		cprint('Temperatura: '+ '%.1f' % tempo_float + ' C', 'green')
		print('------------------------\n')

	else:
		cprint('Cidade não localizada.\n', 'green')
