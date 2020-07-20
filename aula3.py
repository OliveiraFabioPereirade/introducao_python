# a = int(input('Entre com o primeiro valor: ')) # como o input retorna uma string
# b = int(input('Entre com o segundo valor: '))  # tem que converter retorno em int antes das operações
# c = int(input('Entre com o terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é: {}' .format(a)) #python reconhece escopo pela identação
# elif b > a and b > c: # elif é o elseif
#     print('O maior número é: {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))
#
# print('\nFinal do programa') # esta linha sempre é executada porque está fora do escopo do if (identação)



# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# # if resto_a == 0:
# #     print('O valor é par')
# # else:
# #     print('O valor é impar')
#
# #if resto_a == 0 or resto_b == 0:
# if resto_a == 0 or not resto_b > 0: # linha equivalente a de cima por causa do not e do >
#     print('Foi digitado um número par')
# else:
#     print('Não foram digitados numeros pares')


# Validação no final
# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}' .format(media))
# else:
#     print('Foi digitada alguma nota errada')

# Validação na entrada
a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou uma nota errada. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou uma nota errada. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou uma nota errada. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou uma nota errada. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}' .format(media))
