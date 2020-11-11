import requests as reqs
IP=input('Digite o IP a ser consultado: ')
print('Consultando IP:')
r=reqs.get('http://ip-api.com/json/'+IP).json()
ip=r['query']
pais=r['country']
provedor=r['isp']
print(f'''
IP: {ip}
Pais: {pais}
Provedor {provedor}
''')
