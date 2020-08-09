lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]


except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except IndexError:
    print('Erro ao acessar um indice invalido da lista')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))

else:
    print('Execute quando não ocorre excessão')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()