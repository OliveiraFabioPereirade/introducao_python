class Televisao:
    def __init__(self):      # método executado no instanciamento da classe
        self.ligada = False  # inicia televisao desligada
        self.canal = 5       # inicia canal 5

    def power(self):              # método liga/desliga
        if self.ligada:           # se tv está ligada:
            self.ligada = False   #                    desliga
        else:                     # se tv está desligada:
            self.ligada = True    #                       liga

    def aumenta_canal(self):
        if self.ligada:           # se tv está ligada:
            self.canal += 1       # aumenta canal

    def diminui_canal(self):
        if self.ligada:           # se tv está ligada:
            self.canal -= 1       # diminui canal

# print(__name__) # informa que está executando o programa: o próprio arquivo  (__main__)
#                 #                                         um arquivo externo (aula7_televisao)

# o outro arquivo ou o console podem executar este módulo/programa
# - importando tudo:                        import aula7_televisao
# - imortando apenas a classe que desejar:  from aula7_televisao import Televisao


if __name__ == '__main__': # testa se está sendo executado do próprio arquivo antes de continuar
                           # se está sendo executado a partir de outro arquivo através de import: não executa este bloco
    tv = Televisao() # cria instância da classe Televisao e inicia desligada
                     # para instanciar a partir de outro arquivo devemos escrever: tv = aula7_televisao.Televisao()
    print('TV está ligada: {}' .format(tv.ligada)) #mostra condição inicial
    tv.power()       #liga tv
    print('TV está ligada: {}' .format(tv.ligada)) #mostra ligada
    tv.power()       #desliga tv
    print('TV está ligada: {}' .format(tv.ligada)) #mostra desligada
    tv.power()       #liga tv
    print('TV está ligada: {}' .format(tv.ligada)) #mostra ligada
    print('Canal: {}' .format(tv.canal)) #mostra canal inicial 5
    tv.aumenta_canal() #aumenta canal para 6
    print('Canal: {}' .format(tv.canal)) #mostra canal 6
    tv.aumenta_canal() #aumenta canal para 7
    print('Canal: {}' .format(tv.canal)) #mostra canal 7
    tv.diminui_canal() #diminui canal para 6
    print('Canal: {}' .format(tv.canal)) #mostra canal 6




