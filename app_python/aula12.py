import requests

def retorna_dados_cep(cep):
    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.json())

    dados_cep = response.json()

    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon
def retorna_responsa(url):
    response = requests.get(url)
    return response.text

if __name__== '__main__':
    response = retorna_responsa('https://www.globo.com/')
    print(response)
    # retorna_dados_cep('01001000')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])