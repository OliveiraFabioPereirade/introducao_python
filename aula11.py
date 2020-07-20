# lista de exceções nativas do python
# https://docs.python.org/3/library/exceptions.html

lista = [10, 1]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10/0 # força erro: divisão por zero
    # numero = lista[3] # força erro: excedeu número de elementos da lista
    # x = a # força erro: variável não definida
    # print('fechando arquivo') #neste ponto, o arquivo não será fechado, caso ocorra um erro
    # arquivo.close()
except ZeroDivisionError: # trata erro de divisão por zero
    print('Não é possível realizar uma divisão por zero!')
except IndexError: # trata erro de índice
    print('Erro ao acessar um índice inválido da lista!')
except BaseException as ex: # trata erro pela exceção pai de todas as exceções: pega descrição da exceção e chama de "ex"
    print('Erro desconhecido. Erro: {}' .format(ex)) # exibe a descrição da exceção
except: # trata  erro genérico
    print('Ocorreu um erro desconhecido!')
else: # trata quando não ocorre erro
    print('Executa quando não ocorreu nenhum erro!')
finally: # trecho que é executado com ou sem erro
    print('Sempre executa!')
    print('fechando arquivo') #neste ponto, o arquivo sempre será fechado, caso ocorra um erro ou não
    arquivo.close()


### lembrar que o tratamento é uma árvore e é melhor colocar as exceções filhas antes das exceções pais
### a primeira que atender salta as demais



