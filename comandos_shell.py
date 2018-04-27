import subprocess

def checar():
	baterry = subprocess.check_output(['acpi','-b'])
	sensors = subprocess.check_output(['acpi','-t'])
	return baterry, sensors

bateria = str(checar()[0])
nova = bateria.split(":")[1]
nova = nova.split(",")[1]
nova = nova.split("%")[0]
nova = nova.strip()
novainter = int(nova)

sens = str(checar()[1])
sensor = sens.split(",")[1]
sensor = sensor.strip()
sensor = sensor.split(" ")[0]
sensorinter = float(sensor)

if 10 <= novainter <= 15:
	msg = f'CUIDADO! Bateria acabando!: {nova}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif 1 <= novainter <= 5:
	msg = f'FERRO! Corre pra pluga essa birosca! Bateria: {nova}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif novainter == 50:
	msg = f'Metade! Bateria: {nova}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif novainter == 75:
	msg = f'Ta tranquilo, bateria: {nova}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif novainter == 100:
	msg = f'FullBaterry!!! {nova}%'
	subprocess.call(['notify-send',msg])
	print(msg)

if 50 <= sensorinter <= 60:
	msg = f'CUIDADO! 50 GRAUS + !: {sensor}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif 60 <= sensorinter <= 70:
	msg = f'DESLIGA AI QUE VAI QUEIMA!: {sensor}%'
	subprocess.call(['notify-send',msg])
	print(msg)
elif sensorinter >= 70:
	msg = f'PERDENDO CPU EM 3..2..1.. MTU QUENTE!: {sensor}%'
	subprocess.call(['notify-send',msg])
	print(msg)
