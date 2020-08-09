import requests

response = requests.get('http://viacep.com.br/ws/{}/json/'.format('18764012'))
print(response.status_code)