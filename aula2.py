# a = 10
# b = 6

a = int(input('Entre com o primeiro valor: ')) # como o input retorna uma string
b = int(input('Entre com o segundo valor: '))  # tem que converter retorno em int antes das operações

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# cria comentários

# para comentar/descomentat linhas: selecione as linhas e digite ctrl + /

# print(type(soma)) # exibe tipo da variável soma
# soma = str(soma)  # converte variável soma de int em string
# print(type(soma)) # exibe tipo da variável soma

print('soma: ' + str(soma))
print('subtracao: ' + str(subtracao))
print('multiplicacao: ' + str(multiplicacao))
print('divisao: ' + str(divisao))
print('resto: ' + str(resto))

# outras formas de exibir:
print('soma: {}.'
      '\nsubtração: {}' .format(soma, subtracao))
#       |
#       +---> quebra de linha

#              +-------------------------------+
#              |                               |
print('soma: {som}. subtração: {sub}' .format(som = soma, sub = subtracao))
#                                |                         |
#                                +-------------------------+  são alias, podem ter qualquer nome

resultado = ('soma: {som}. subtração: {sub}' .format(som = soma, sub = subtracao))
print(resultado)

# x = '2'
# soma2 = int(x) + 2 # converte x em inteiro antes de somar
# print(soma2)