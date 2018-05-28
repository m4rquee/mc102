#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    return num in conj


# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    ret = True
    for v in conj1:
        ret &= v in conj2

    return ret


# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if num not in conj:
        conj.append(num)


def subtracao(conj, num):
    if num in conj:
        conj.remove(num)


# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    return list(set(conj1) | set(conj2))


def intersecao(conj1, conj2):
    return list(set(conj1) & set(conj2))


def diferenca(conj1, conj2):
    return list(set(conj1) - set(conj2))


def uniao_disjunta(conj1, conj2):
    return list(set(conj1) ^ set(conj2))
