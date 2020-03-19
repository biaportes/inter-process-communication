#Verifica como está a carga média (load average) do sistema	
#shell command: uptime ->  médias de carga de 1 minuto, 5 minutos e 15 minutos
#shell command: nproc -> nº de núcleos de processamento (cpu com hyper-threading, contabiliza o dobro)
import subprocess
import threading

class InterProcessPIPE(threading.Thread):
        def __init__(self, command):
                self.cm = command
                self.result = []
                
                threading.Thread.__init__(self)
        #metodo sobrescrito da classe pai
        def run(self):

                p = subprocess.Popen(self.cm,
                        stdin = subprocess.PIPE,
                        stdout = subprocess.PIPE)

                out,err = p.communicate()
                out = out.decode()
                out = out.split()
                self.result = out

                if self.cm == "uptime":
                        self.normalizeLAUptime()
                else:
                        self.result = int(self.result[0])

                return self.result

        def normalizeLAUptime(self):
                la = [self.result[9], self.result[10], self.result[11]]

                la[2] = la[2] + ","

                for i in range(3):
                        la[i] = la[i][0:-1]
                        la[i] = la[i].replace(",", ".")
                        la[i] = float(la[i])

                self.result = la
                        
                



if __name__ == "__main__":
        threads = []
        threads.append(InterProcessPIPE("nproc"))
        threads.append(InterProcessPIPE("uptime"))

        for i in range(2):
                threads[i].start()
                
        for i in range(2):
                threads[i].join()

        
        nproc = threads[0].result
        uptime = [[1,5,15],threads[1].result]

        print("O computador tem {0} núcleos de processamento.".format( nproc))
        
        print("A carga média nos últimos 1, 5 e 15 minutos são: ", uptime[1])

        for i in range(3):
                if uptime[1][i] > nproc :
                        print("Há gargalo no sistema")
                else:
                        print("Sem gargalo no sistema nos últimos {0} minutos".format(uptime[0][i]))
        
