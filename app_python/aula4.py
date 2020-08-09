nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entre com a nota correta de 0 a 10: '))
print(nota)


# a = 0
# while a <= 100:
#     print(a)
#     a += 10

# a = int(input('Entre com um valor: '))
# for num in range(a+1):
#
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         #print(x,resto)
#         if resto == 0:
#             div += 1
#
#     if div ==2:
#         print(num)


# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     print(a,resto)
#     if resto == 0:
#         div += 1
#
# if div ==2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))
