# lambda é uma fução anônima que utiliza um código mais reduzido que os métodos

# reescrita do contador_letras no formato lambda
contador_letras = lambda lista: [len(x) for x in lista]
#                          |    |
#                          |    +-------> retorna uma lista de quantidade de letras de cada palavra na lista de palavras
#                          +------------> recebe ua lista de palavras

lista_animais = ['cobra', 'girafa', 'dromedário']
print(lista_animais)
print(contador_letras(lista_animais))

add = lambda a, b: a + b
sub = lambda a, b: a - b

print(add(10,5))
print(sub(10,5))

# dicionário lambda
calculadora = {
    'soma': lambda a, b: a + b,
    'subt': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'divi': lambda a, b: a / b
}
print(type(calculadora))
                      # usar colchetes []
adiciona = calculadora['soma'] # é o mesmo que escrever: adiciona = lambda a, b: a + b
multiplica = calculadora['mult']
print(adiciona(10,5))
print(multiplica(10,5))



