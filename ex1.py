#
import subprocess

comando = "uptime"

p = subprocess.Popen(comando,
	stdin = subprocess.PIPE,
	stdout = subprocess.PIPE)

saida,err = p.communicate()
saida = saida.decode()
saida = saida.split()

m = [saida[7], saida[8], saida[9]]

print(m)

m[2] = m[2] + ","

for i in range(3):
	m[i] = m[i][0:-1]
	m[i] = m[i].replace(",", ".")
	m[i] = float(m[i])
	#Verifica se a carga média (load average) do sistema está ruim ou abaixo	
	if m[i] > 1 :
		print("eh maior")
	else:
		print("não eh maior")

