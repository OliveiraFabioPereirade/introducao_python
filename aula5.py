lista = [7, 3 ,1, 5] # listas são formadas por colchetes
lista_animal = ['cachorro', 'gato', 'elefante'] # por convenção, listas possuem o mesmo tipo de variáveis

# print(type(lista))
# print(lista)
#
# print(lista_animal)
# print(lista_animal[1]) #pega 2º elemento da lista porque começa a contar do 0
#
# for x in lista_animal: # imprime todos os elementos da lista
#     print(x)

# soma = 0
# for x in lista: # imprime todos os elementos da lista e soma
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista)) # exibe a soma dos elementos da lista
# print(max(lista)) # exibe o maior    elemento  da lista
# print(min(lista)) # exibe o menor    elemento  da lista
#
# print(max(lista_animal)) # exibe o maior    elemento  da lista alfabeticamente
# print(min(lista_animal)) # exibe o menor    elemento  da lista alfabeticamente

# nova_lista_animal = lista_animal * 3  # multiplica lista: no caso, repete elementos 3 vezes
# print(nova_lista_animal)

# if 'lobo' in lista_animal: #verifica se elemento existe na lista
#     print('Existe na lista')
# else:
#     print('Não existe na lista, mas será incluído')
#     lista_animal.append('lobo') # inclui elemento na última posição da lista
#     print(lista_animal)
#
# lista_animal.pop() # retira a última posição da lista
# print(lista_animal)
#
# lista_animal.pop(1) # retira a 2ª posição da lista
# print(lista_animal)
#
# lista_animal.remove('elefante') # retira o elefante da lista
# print(lista_animal)

# lista.sort() # ordena lista no modo crescente
# print(lista)
# lista.reverse() # apenas inverte ordem da lista, não ordena decrescente
# print(lista)
#
# lista_animal.sort()
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# a lista é mutável
lista_animal[0] = 'macaco'
print(lista_animal)

# a tupla é imutável
tupla = (1, 10, 12, 14) # tuplas são formadas por parenteses
print(tupla)
print(tupla[2]) #exibe 3º elemento da tupla
# tupla[0] = 12 # retorna erro porque não pode ser alterado

print(len(lista_animal)) # mostra nº de elementos
print(len(tupla))

tupla_animal = tuple(lista_animal) # converte lista em tupla que não pode ser alterada
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)   # converte tupla em lista que pode ser alterada
print(type(lista_numerica))
print(lista_numerica)
