import smtplib
import subprocess

df = subprocess.check_output(['df','-h'])
df = str(df)
df = df.split('/run')[1]
df = df.split('/\\ntmpfs')[0]
df = df.split('\\n')[1]
df = df.strip()
df = df.replace('       ', '  ')
topo = 'P:               T:       U:        S:      U%:'
msg = f'\nGerenciamento Espaço:\n\n {topo} \n {df}\n\n............................\nP: Partition\nT: Total\nU: Usage\nS: Space\nU%: Usage %'


server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('diegosarzi@gmail.com', 'mInister23')

para = 'diegosarzi@gmail.com'
corpo = msg.encode('utf8')

server.sendmail('diegosarzi@gmail.com', para, corpo)

print('email enviado com sucesso.')

server.quit()
