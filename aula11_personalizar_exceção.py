class Error(Exception): # cria uma classe Error que herda características de Exception
    pass # esta classe não faz nada, mas é obrigatório para criar exceções personalizadas

class InputError(Error): # cria uma classe InputError que herda características de Error
    def __init__(self, message): #message permite personalizar a mensagem de erro
        self.message = message # passa mensagem recebida para o erro




while True: # laço infinito
    try:
        x = int(input('entre com uma nota entre 0 e 10: '))
        print(x)
        if x > 10: # se entrou com número maior que 10:
            raise InputError('Nota não pode ser maior que 10!') # força erro e envia mensagem do erro
        elif x < 0:# se entrou com número maior que 10:
            raise InputError('Nota não pode ser menor que 0!') # força erro e envia mensagem do erro
        break # se não ocorrer erro no input, sai do laço infinito
    except ValueError: #se digitou algo que não pode ser convertido em inteiro
        print('Valor inválido! Deve-se digitar apenas números!')
    except InputError as ex: # trata erro personalizado e pega a mensagem do erro e guarda em ex
        print(ex) # exibe mensagem do erro personalizado