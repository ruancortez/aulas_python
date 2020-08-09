class Error(Exception):
    pass

class ImputError(Error):
    def __init__ (self, message):
        self.message = message




while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise ImputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise ImputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except ImputError as ex:
        print(ex)


