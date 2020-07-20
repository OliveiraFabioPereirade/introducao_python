# def soma(a, b):   # cria método soma: que recebe a e b
#     return a + b  #                     e retorna a + b
#
# def subtracao(a, b):   # cria método subtracao: que recebe a e b
#     return a - b  #                               e retorna a - b
#
# def multipicacao(a, b):   # cria método multipicacao: que recebe a e b
#     return a * b  #                                     e retorna a * b
#
# def divisao(a, b):   # cria método divisao: que recebe a e b
#     return a / b  #                           e retorna a / b
#
# print(soma(3, 2))
# print(subtracao(3, 2))
# print(multipicacao(3, 2))
# print(divisao(3, 2))


class Calculadora: # por convenção as classes devem começar com maiúsculas

    def __init__(self):   # cria método __init__: que sempre é executado quando a classe é instanciada
        pass              # informa que faz nada, por isto, este método pode ser apagado sem problemas

    def soma(self,valor_a, valor_b):   # cria método soma:   que recebe self
        return valor_a + valor_b  # e retorna valor_a + valor_b

    def subtracao(self,valor_a, valor_b):   # cria método subtracao: que recebe self
        return valor_a - valor_b  #         e retorna valor_a - valor_b

    def multipicacao(self,valor_a, valor_b):   # cria método multipicacao: que self
        return valor_a * valor_b  #             e retorna valor_a * valor_b

    def divisao(self,valor_a, valor_b):   # cria método divisao: que recebe self
        return valor_a / valor_b  #       e retorna valor_a / valor_b

calculator = Calculadora() # apenas instancia classe Calculadora e inicia parâmetros
print(calculator.soma(3,2))         # precisa iniciar parâmetros a cada execução
print(calculator.subtracao(3,2))
print(calculator.multipicacao(3,2))
print(calculator.divisao(3,2))





