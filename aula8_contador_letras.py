def contador_letras(lista_palavras): # cria método que recebe uma lista de palavres e conta as letras das palavras
    contador = []                    # cria lista de quantidades de letras
    for x in lista_palavras:         # para cada elemento da lista de palavras
        quantidade = len(x)          # guarda a quantidade de letras
        contador.append(quantidade)  # insere a quantidade de letras na lista de quantidades de letras
    return contador                  # retorna a lista de quantidades de letras

def teste():                         # cria método
    return 'teste'                   # que retorna a string 'teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']      # cria a lista de palavras
    print(lista)                  # exibe a lista de palavras
    print(contador_letras(lista)) # exibe a lista de quantidades de letras



