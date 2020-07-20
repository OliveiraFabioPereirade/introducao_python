# conjunto = {1, 2, 3, 4, 4, 2} # conjuntos são formados por chaves
# print(type(conjunto))         # tipo set
# print((conjunto))             # conjuntos não permitem duplicidade, por isto conjunto será {1, 2, 3, 4}
#
# conjunto.add(5) # acrescenta elemento ao conjunto na última posição
# conjunto.discard(2) # remove elemento do conjunto
# print((conjunto))

# conjunto = {1, 2, 3, 4, 5}
# print('Conjunto: {}' .format(conjunto))
# conjunto2 = {5, 6, 7, 8}
# print('Conjunto2: {}' .format(conjunto2))
# conjunto_uniao = conjunto.union(conjunto2) # cria conjunto com unição de conjunto e conjunto2
# print('União: {}' .format(conjunto_uniao))
# conjunto_interseccao = conjunto.intersection(conjunto2) # cria conjunto com intersecção de conjunto e conjunto2
# print('Intersecção: {}' .format(conjunto_interseccao))
# conjunto_diferenca1 = conjunto.difference(conjunto2) # cria conjunto com diferença de conjunto em relação a conjunto2
# print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))
# conjunto_diferenca2 = conjunto2.difference(conjunto) # cria conjunto com diferença de conjunto2 em relação a conjunto
# print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))
# conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2) # cria conjunto com diferença simétrica (inverso de intersecção)
# print('Diferença simétrica: {}' .format(conjunto_dif_simetrica))

# conjunto_a = {1, 2, 3}
# conjunto_b = {1, 2, 3, 4, 5, 6}
# conjunto_subset = conjunto_a.issubset(conjunto_b) # avalia se conjunto a é um subconjunto do conjunto b
# print(conjunto_subset)
# conjunto_superset = conjunto_b.issuperset(conjunto_a) # avalia se conjunto b é um superconjunto do conjunto a
# print(conjunto_superset)

lista_animais = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('Uma lista com elementos repetidos: {}' .format(lista_animais))
conjunto_animais = set(lista_animais) # converte lista em conjunto
print('É convertida em um conjunto com elementos únicos: {}' .format(conjunto_animais))
lista_animais = list(conjunto_animais) # converte conjunto em lista
print('E depois, é reconvertida em uma lista com elementos únicos: {}' .format(lista_animais))


