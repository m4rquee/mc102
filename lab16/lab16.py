#  Funcao: removePalavras
#
#  Parametros:
#    s: string contendo o texto de entrada
#    vs: vetor de strings com as palavras a serem removidas
#
#  Descricao:
#    Deve-se remover as palavras de s que estiverem listadas em vs.
#    Ao final, s nao deve conter espacos extras.
#
# Retorno:
#   string s sem as palavras de vs.

def removePalavras(s, vs):
    words = s.split()
    cleanned = []
    for w in words:
        if w not in vs:
            cleanned.append(w)

    return ' '.join(cleanned)


# Parametros:
#   paginas: lista de strings cada uma representando uma pagina
#   termosBusca: lista de strings com os termos a serem buscados
#
# Descricao:
#   Deve verificar se cada página em paginas contém todos os termos
#   de busca em termosBusca. Se a paginas[i] contiver todos os termos
#   então deve-se atribuir 1 para resp[i] e 0 caso não contenha pelo
#   menus um dos termos de busca.
#
# Retorno:
#   lista a ser preenchida como resposta, de dimensao numPag.

def pagsResposta(paginas, termosBusca):
    ret = []
    for pag in paginas:
        pag = pag.split()
        val = True
        for term in termosBusca:
            if term not in pag:
                val = False
                break
        ret.append(val)

    return ret


# Parametros:
#   links: matriz quadrada binária representando links entre as paginas
#   resp: vetor obtido apos execucao de pagsResposta
#
# Descricao:
#   Deve-se preencher uma lista numLinks da seguinte maneira: para cada
#   posicao i (0 <= i < numPags), se resp[i] == 1, então numLinks[i] deve conter
#   o numero de links de outras paginas resposta para i. Caso resp[i] == 0,
#   entao numLinks[i] deve ser -1.
#
# Retorno
#   lista numLinks a ser preenchida como resposta, de tamanho numPag

def linksResposta(links, resp):
    ret = []
    for i, r in enumerate(resp):
        ret.append(count_links(i, links, resp) if r else -1)

    return ret


def count_links(pag, links, resp):
    count = 0
    for i, l in enumerate(links):
        if resp[i]:
            count += l[pag]

    return count
