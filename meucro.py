import time, subprocess

print("Iniciando...")

for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            
            print("Horas: ", h, "Minutos: ", m, "Segundos: ", s)
            time.sleep(1)
            subprocess.run(["clear"])
