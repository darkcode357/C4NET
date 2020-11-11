import requests as reqs
def main():
    IP=input('Digite o IP a ser consultado: ')
    print('Consultando IP:')
while true:
    r=reqs.get('http://ip-api.com/json/'+IP).json()
    ip=r['query']
    pais=r['country']
    provedor=r['isp']
    print(f'''
    IP: {ip}
    Pais: {pais}
    Provedor {provedor}
''')
