import subprocess

def communication_PIPE(command):
        
        command = command.split()
        p = subprocess.Popen(command,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE)

        out,err = p.communicate()
        out = out.decode()

        return out
        


pckt = input("Entre com o pacote Python que deseja verificar instalação: ")
command = "pip3 show " + pckt

saida = communication_PIPE(command)

if(saida == ""):
        print("Não está instalado")
        r = input("Deseja instalar? S ou N.")
        r = r.upper()
        if(r == "S" or r == "SIM"):
                command = "pip3 install " + pckt
                print("Aguardando resposta...\n\n")
                p = communication_PIPE(command)
                print(p)
                
else:
        print("\n*************************************\n")
        print("Pacote {0} está instalado.".format(pckt))
        print("\n*************************************\n")
        print(" \n\n", saida)
