import requests as reqs
def main():
    IP=input('Digite o ip do provedor a ser consultado: ')
    print('033[94;1mConsultando IP do provedor...')


def banner():
    os.system("clear")
    print("033[91;1mCarregando =========")
    time.sleep(2)
    print("""________ __  _   ______________
  / ____/ // / / | / / ____/_  __/
 / /   / // /_/  |/ / __/   / /
/ /___/__  __/ /|  / /___  / /
\____/
""")
    os.system(
"toilet -f sbmloc --filter -borde r;metal ' C4NET")
banner()

try:
    IP=input('Digite o ip do provedor a ser consultado: ')
    except valueError:
        print('033[94;1mUtilize somente numeros em ip. não consultamos mac addres')

for i range(1)
    print('033[94;1mOcorreu um erro inesperado. tente instalar o request do pip. com pip install request')
while True:
    r=reqs.get('http://ip-api.com/json/'+IP).json()
    ip=r['query']
    pais=r['country']
    provedor=r['isp']
    print(f'''
    IP: {ip}
    Pais: {pais}
    Provedor {provedor}
''')
