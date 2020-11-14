#------------------------------------#
#    CREATED  BY:   0x0a λ           #
#   time: 10/11/2020                 #
#   python version: 3.8              #
#------------------------------------#



import requests as reqs
from time import sleep
import os
import fileinput

class Collors:
    Preto1 = '\033[1;30m'
    Preto2 = '\033[1;40m'
    Vermelho1 = '\033[1;31m'
    Vermelho2 = '\033[1;41m'
    Verde1 = '\033[1;32m'
    Verde2 = '\033[1;42m'
    Amarelo1 = '\033[1;33m'
    Amarelo2 = '\033[1;43m'
    Azul1 = '\033[1;34m'
    Azul2 = '\033[1;34m'
    Magneta1 = '\033[1;35m'
    Magneta2 = '\033[1;45m'
    Cyan1 = '\033[1;36m'
    Cyan2 = '\033[1;46m'
    CinzaC1 = '\033[1;37m'
    CinzaC2 = '\033[1;47m'
    CinzaE1 = '\033[1;90m'
    CinzaE2 = '\033[1;100m'
    VermelhoC1 = '\033[1;91m'
    Vermelhoc2 = '\033[1;101m'
    VerdeC1 = '\033[1;92m'
    VerdeC2 = '\033[1;101m'
    AmareloC1 = '\033[1;93m'
    AmareloC2 = '\033[1;103m'
    AzulC1 = '\033[1;94m'
    AzulC2 = '\033[1;104m'
    

def runntxt(s):
    for noobs in s + '\n':
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10 / 2100)
runntxt()

def main():
    print('\x1b[32;1m Avisos legais: Eu desenvolvedor não me responsabilizo pelos atos dos usuarios dessa tool.')
    print('\x1b[32;1m disclammer: I developer is not responsible for the actions of users')
    sleep(2)
    os.system("clear")
    IP = input('\x1b[32;1m Digite o ip do provedor a ser consultado:  \x1b[90;1m')
    print('\x1b[32;1m Consultando IP do provedor...')


def banner():
    os.system("clear")
    print("\x1b[32;1m Carregando...")
    sleep(2)
    print("""________ __  _   ______________
  / ____/ // / / | / / ____/_  __/
 / /   / // /_/  |/ / __/   / /
/ /___/__  __/ /|  / /___  / /
\____/
    """)
    sleep(2)
    os.system(
    "toilet -f sbmloc --filter -borde r;metal ' C4NET")
    print('\x1b[32;1m Desenvolvido por: 0x0a')
banner()

try:
    IP = input('Digite o ip do provedor a ser consultado: ')
except valueError:
    print('Utilize somente numeros em ip. não consultamos mac addres')

try:
    r = reqs.get('http://ip-api.com/json/'+IP).json()
    ip = r['query']
    pais = r['country']
except valueError:
    print('Para utilizar esse script você precisa instalar os requests do pip utize, pip install requests')
try:
    IP = input('Digite o ip do provedor a ser consultado: ')
KeyboardInterrupt

except valueError:
    print('Você escolheu sair. obrigado pela preferencia')

class api: 
    def _init_(self, tk, search()):
        self.tk = tk
        self.search = search
        
        class metodo:
            
        r = reqs.get('http://ip-api.com/json/'+IP).json()
        ip = r['query']
        pais = r['country']
        provedor = r['isp']
            print(f'''
                IP: {
                ip
}
                Pais: {
                pais
}
               Provedor {
               provedor
}
    ''')
