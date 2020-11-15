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
    

def banner():
    os.system("clear")
    print("\033[1;91m\033[1;93mCarregando...")
    sleep(2)
    print("""
+-+-+-+-+-+
|C|4|N|E|T|
+-+-+-+-+-+
    """)
    
    sleep(2)
 
    print('\033[1;91m\033[1;93mDesenvolvido por: 0x0a')
    sleep(20)
    print('Carregando...')
    os.system("clear")
banner()

def dependencias():
    print('\033[1;91m\033[1;93m.:.:.Avisos legais: Eu desenvolvedor não me responsabilizo pelos atos dos usuarios dessa tool.:.:.')
    
    
    print('\033[1;91m\033[1;93m.:.:. Disclammer: I developer is not responsible for the actions of users.:.:.')
    
    
    sleep(2)
    os.system("clear")
    
    IP = input('\033[1;91m\033[1;93mDigite o ip do provedor a ser consultado:  ')
    
    
    print('\033[1;91m\033[1;93mPara sair pressione ctrl + C')
    
    
    print('\033[1;91m\033[1;93mConsultando IP do provedor...')

dependencias()

try:
    IP = input('Digite o ip do provedor a ser consultado: ')
except valueError:
    print('Utilize somente numeros em ip. não consultamos mac addres')


try:
    print('Para sair pressione ctrl + C')

except valueError:
    print('Você escolheu sair. obrigado pela preferencia')

class api: 
    def _init_(self, tk, search):
        self.tk = tk
        self.search = search
        
        class metodo:
            
            
            r = reqs.get('http://ip-api.com/json/'+IP).json()
            ip = r['query']
            pais = r['country']
            latitude = r['lat']
            longitude = r['lon']
            provedor = r['isp']
            horario_local = r['timezone']
            
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
            Latitude{
            latitude
}
            Longitude{
            longitude
}
            Horario local{
            horario_local
}

    ''')
            print(ip)
            print(provedor)
            print(latitude)
            print(longitude)
            print(horario_local)