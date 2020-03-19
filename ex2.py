import subprocess

text = input("o que deseja procurar? ")
text = text.replace(" ", "+")
command = "firefox -new-window http://letmegooglethat.com/?q=" + text
command = command.split()


p = subprocess.Popen(command)

p.communicate()

