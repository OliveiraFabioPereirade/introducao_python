# for x in range(100): # causa execução de 0 a 99
#     print(x)

# for x in range(90, 100): # causa execução de 90 a 99
#     print(x)



# a = int(input('Entre com um número: '))
# div = 0
# for x in range (1, a + 1): # vai executar de 1 até o valor de a
#     resto = a % x
#     print(a, resto)
#     if resto == 0:
# #        div = div + 1
#         div += 1 # faz o mesmo que a linha de cima
# if div == 2: # se a pode ser dividido apenas por 1 e por ele mesmo
#     print('O número {} é primo' .format(a))
# else:
#     print('O número {} não é primo' .format(a))



# for a in range(100): #testa números primos de 0 a 100
#     div = 0
#     for x in range (1, a + 1): # vai executar de 1 até o valor de a
#         resto = a % x
#         if resto == 0:
#     #        div = div + 1
#             div += 1 # faz o mesmo que a linha de cima
#     if div == 2: # se a pode ser dividido apenas por 1 e por ele mesmo
#         print('O número {} é primo' .format(a))


# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida!\n'
#                      'Entre com a nota correta: '))
# print(nota)


# Validação na entrada com while
a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou uma nota errada. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou uma nota errada. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou uma nota errada. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou uma nota errada. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}' .format(media))
