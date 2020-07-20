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

    def __init__(self, num1, num2):   # cria método __init__: que sempre é executado quando a classe é instanciada
        self.valor_a =  num1          # inicia self.valor_a
        self.valor_b =  num2          # inicia self.valor_b

    def soma(self):   # cria método soma:   que recebe self
        return self.valor_a + self.valor_b  # e retorna self.valor_a + self.valor_b

    def subtracao(self):   # cria método subtracao: que recebe self
        return self.valor_a - self.valor_b  #         e retorna self.valor_a - self.valor_b

    def multipicacao(self):   # cria método multipicacao: que self
        return self.valor_a * self.valor_b  #             e retorna self.valor_a * self.valor_b

    def divisao(self):   # cria método divisao: que recebe self
        return self.valor_a / self.valor_b  #       e retorna self.valor_a / self.valor_b


if __name__ == '__main__':  # testa se está sendo executado do próprio arquivo antes de continuar
                            # se está sendo executado a partir de outro arquivo através de import: não executa este bloco
    calculator = Calculadora(3,2) # instancia classe Calculadora e inicia parâmetros
    print(calculator.valor_a) # exibe parâmetro da instância
    print(calculator.valor_b) # exibe parâmetro da instância
    print(calculator.soma())
    print(calculator.subtracao())
    print(calculator.multipicacao())
    print(calculator.divisao())





