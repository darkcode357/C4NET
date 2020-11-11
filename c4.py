#------------------------------------#
#    CREATED  BY:   0x0a λ           #
#   time: 10/11/2020                 #
#   python version: 3.8              #
#------------------------------------#


import requests as reqs
from time import sleep
import os
import fileinput

N = '\x1b[0m'
D = '\x1b[90m'
W = '\x1b[1;37m'
B = '\x1b[1;34m'
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
C = '\x1b[1;36m'
WD = '\x1b[90;1m'
GL = '\x1b[96;1m'
BB = '\x1b[34;1m'
GG = '\x1b[32;1m'
RR = '\x1b[31;1m'
B = '\x1b[34m'
G = '\x1b[32m'
R = '\x1b[31m'
ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '\xe2\x88\x9a' + G + '] '
eror = R + '[' + W + '!' + R + ']'

def runntxt(s):
    for noobs in s + '\n':
        sys.stdout.write(noobs)
        sys.stdout.flush()
        time.sleep(10 / 2100)


def main():
    IP = input(GL'Digite o ip do provedor a ser consultado: ')
    print(GL'Consultando IP do provedor...')


def banner():
    os.system("clear")
    print(WD"Carregando...")
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
    print('Desenvolvido por: 0x0a')
banner()

try:
    IP = input('Digite o ip do provedor a ser consultado: ')
except valueError:
    print(BB'Utilize somente numeros em ip. não consultamos mac addres')

try:
    r = reqs.get('http://ip-api.com/json/'+IP).json()
    ip = r['query']
    pais = r['country']
except valueError:
    print(RR'Para utilizar esse script você precisa instalar os requests do pip utize, pip install requests')
try:
    File "/data/data/com.termux/files/home/C4NET/c4.py", line 26, in <module>
    IP = input('Digite o ip do provedor a ser consultado: ')
KeyboardInterrupt

except valueError:
    print(WD'Você escolheu sair. obrigado pela preferencia')

while True:
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
