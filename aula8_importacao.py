# print(__name__) # informa que está executando o programa: o próprio arquivo  (__main__)
#                 #                                         um arquivo externo (aula7_televisao)
#
# # o outro arquivo ou o console podem executar este módulo/programa
# # - importando tudo:                        import aula7_televisao
# # - imortando apenas a classe que desejar:  from aula7_televisao import Televisao
#
#
# if __name__ == '__main__': # testa se está sendo executado do próprio arquivo antes de continuar
#                            # se está sendo executado a partir de outro arquivo através de import: não executa este bloco
#     tv = Televisao() # cria instância da classe Televisao e inicia desligada
#                      # para instanciar a partir do console  devemos escrever: tv = aula7_televisao.Televisao()


from aula7_televisao import Televisao # importa classe do arquivo aula7_televisao
from aula7_1 import Calculadora # importa classe do arquivo aula7_1
from aula8_contador_letras import contador_letras, teste # importa métodos do arquivo aula8_contador_letras

if __name__ == '__main__':  # testa se está sendo executado do próprio arquivo antes de continuar
                            # se está sendo executado a partir de outro arquivo através de import: não executa este bloco

    tele = Televisao() # instancia classe a partir deste arquivo
    print(tele.ligada)
    tele.power()
    print(tele.ligada)

    calc = Calculadora(12,5) # instancia classe a partir deste arquivo
    print(calc.soma())

    listagem = ['camelo', 'hipopótamo', 'zebra']      # cria a lista de palavras
    print(listagem)                  # exibe a lista de palavras
    print(contador_letras(listagem)) # exibe a lista de quantidades de letras
                                     # métodos não precisam ser instanciados

    print(teste())  # exibe teste