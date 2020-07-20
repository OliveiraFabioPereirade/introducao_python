import shutil  # módulo nativo do python que permite copiar e mover arquivos entre outras coisas


# arquivo = open('teste.txt', 'w') # cria (se não existe), ou abre (se já existe) o arquivo 'teste.txt'
#                            |
#                            +---> sobreescreve o arquivo

# arquivo = open('teste.txt', 'a') # cria (se não existe), ou abre (se já existe) o arquivo 'teste.txt'
#                            |
#                            +---> acrescenta ao arquivo

# arquivo.write('Primeira linha') # escreve no arauivo 'teste.txt'
# arquivo.write('\nSegunda linha') # escreve no arauivo 'teste.txt'
# arquivo.write('\nTerceira linha') # escreve no arauivo 'teste.txt'

# arquivo.close() # fecha o arquivo 'teste.txt'


def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # 'r' abre o arquivo para leitura
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read() # aluno_nota recebe o conteúdo do arquivo
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # aluno nota passa a ter uma lista com o conteúdo do arquivo separado por linhas
    # print(aluno_nota)
    lista_media = [] # cria dicionário de listas de médias vazio
    for x in aluno_nota: # para cada elemento de aluno_nota
        lista_linha = x.split(',') # usa a virgula para quebrar a linha atual e formar uma lista salva em lista_linha
        # print(lista_linha)
        aluno = lista_linha.pop(0) # retira o primeiro elemento da lista_linha e salva em aluno_
        lista_notas = lista_linha # lista_notas recebe lista_linha sem nome do aluno
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int (i) for i in notas]) / 4
#                              |  \_______________________/   |
#                              |               |              +--> divide tudo por 4
#                              |               +---> transforma todos os elementos de notas em interiros
#                              +---> soma todos os elementos convertidos em inteiros
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)}) # acrescenta lista no dicionário de listas com nome e média do aluno
    return lista_media

def copia_arquivo(nome_arquivo):
    # import shutil # módulo nativo do python  # melhor importá-lo no início deste módulo para não importar toda a vez que usar
    # shutil.copy(nome_arquivo, 'c:/documentos/') # sem especificar nome: copia com nome original
    shutil.copy(nome_arquivo, 'c:/documentos/notas_alunos.txt') # especificando nome: copia com nome especificado

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'c:/documentos/') # sem especificar nome: move com nome original
    # shutil.move(nome_arquivo, 'c:/documentos/notas_alunos.txt') # especificando nome: move com nome especificado



if __name__ == '__main__':
    # nome_arquivo = 'teste.txt'
    #nome_arquivo = 'c:/documentos/teste.txt' # notar que usa barra invertida (/) no lugar de barra comum (\)
    # escrever_arquivo(nome_arquivo, 'Primeira linha.\n')
    # atualizar_arquivo(nome_arquivo, 'Segunda linha.\n')
    # atualizar_arquivo(nome_arquivo, 'Terceira linha.\n')
    # ler_arquivo(nome_arquivo)

    nome_arquivo = 'notas.txt'
    # aluno = 'Rafael, 10, 10, 5, 5\n'
    # aluno = 'Felipe, 7, 8, 5, 6\n'
    # aluno = 'Galleani, 7, 8, 5, 6\n'
    # aluno = 'Cesar, 7, 9, 3, 8\n'
    # atualizar_arquivo(nome_arquivo, aluno)
    # lista_media_notas = media_notas(nome_arquivo) # guarda lista de médias em lista_media_notas
    # print(lista_media_notas)

    # copia_arquivo(nome_arquivo)
    move_arquivo(nome_arquivo)




