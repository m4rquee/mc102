#!/usr/bin/env python3
# *******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.
from functools import cmp_to_key


def atualizaTabela(tabela, jogo):
    vals = jogo.split()
    gols = (int(vals[1]), int(vals[-2]))
    jog1 = filter(lambda jogador: jogador[0] == vals[0], tabela).__next__()
    jog2 = filter(lambda jogador: jogador[0] == vals[-1], tabela).__next__()

    # Adiciona pontos
    jog1[1] += 1 if gols[0] == gols[1] else (3 if gols[0] > gols[1] else 0)
    jog2[1] += 1 if gols[0] == gols[1] else (3 if gols[1] > gols[0] else 0)

    # Adiciona vitorias
    jog1[2] += gols[0] > gols[1]
    jog2[2] += gols[1] > gols[0]

    # Adiciona saldo
    jog1[3] += gols[0] - gols[1]
    jog2[3] += gols[1] - gols[0]

    # Adiciona gols pros
    jog1[4] += gols[0]
    jog2[4] += gols[1]


# *******************************************************************************
# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.
def comparaTimes(time1, time2):
    for i in range(1, len(time1)):
        if time1[i] > time2[i]:
            return 1
        elif time1[i] < time2[i]:
            return -1

    return 0


# *******************************************************************************
# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):
    tabela = tabela.sort(key=cmp_to_key(comparaTimes), reverse=True)


# *******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):
    for jog in tabela:
        print('%s, %i, %i, %i, %i' % tuple(jog))
