import subprocess
import csv

nome_arquivo = input('Qual nome do arquivo de gastos? ')

arquivo = open(nome_arquivo+'.csv', mode='w', encoding='utf8')
escritor = csv.writer(arquivo, lineterminator='\n')
escritor.writerow(['GASTOS','VALORES'])

lista = {}
sair = False

subprocess.call('clear')

while sair == False:
   print('### Gastos ###')
   print('a - adiicionar    l - listar    q - sair')
   menu = input('Digite sua opção: ')

   if menu == 'a':
      nome_gasto = input('Digite o nome do gasto: ')
      valor_gasto = input('Digite o valor do gasto: R$')
  
      lista[nome_gasto] = valor_gasto
      escritor.writerow([nome_gasto, valor_gasto])
      print(lista)
      input()
   elif menu == 'l':
      print(lista)
      input()
   elif menu == 'q':
      sair = True
   else:
      print('Opção Invalida')
   
   subprocess.call('clear')

arquivo.close()
