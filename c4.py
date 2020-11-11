import requests as reqs
from time import sleep
import os

def main():
    IP = input('Digite o ip do provedor a ser consultado: ')
    print('033[94;1mConsultando IP do provedor...')


def banner():
    os.system("clear")
    print("Carregando...")
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
    print('033[94;1mUtilize somente numeros em ip. não consultamos mac addres')

try:
    r = reqs.get('http://ip-api.com/json/'+IP).json()
    ip = r['query']
    pais = r['country']
except valueError:
    print('Para utilizar esse script você precisa instalar os requests do pip utize, pip install requests')
try:
    File "/data/data/com.termux/files/home/C4NET/c4.py", line 26, in <module>
    IP = input('Digite o ip do provedor a ser consultado: ')
KeyboardInterrupt

except valueError:
    print('Você escolheu sair. obrigado pela preferencia')

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
