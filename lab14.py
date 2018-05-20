# Lucas de Oliveira Silva - 220715
# O sistema de gerenciamento de turmas da DAC deve ser capaz de realizar operações como impressão,
# ordenação, inclusão, remoção e busca de alunos matriculados em cada turma.
ras = [int(v) for v in input().split()]
ras_ord = None


def busca(ra):
    e, d = 0, len(ras) - 1
    inds = []
    while e <= d:
        meio = (e + d) // 2
        inds.append(meio)
        aux = ras[meio]

        if ra == aux:
            return True, meio, inds

        if ras_ord == 'c':
            e, d = (meio + 1, d) if ra > aux else (e, meio - 1)
        elif ras_ord == 'd':
            e, d = (meio + 1, d) if ra < aux else (e, meio - 1)

    if e == len(ras) or d == len(ras):
        meio = len(ras)

    return False, meio, inds


def print_array(vet):
    if len(vet) > 0:
        print(' '.join(map(str, vet)), '')


def busca_cmd(ra):
    if ras_ord:
        achou, pos, inds = busca(ra)
        print_array(inds)
        if achou:
            print(ra, 'esta na posicao:', pos)
        else:
            print(ra, 'nao esta na lista!')
    else:
        print('Vetor nao ordenado!')


def in_cmd(ra):
    if len(ras) == 150:
        print('Limite de vagas excedido!')
        return

    if ra in ras:
        print('Aluno ja matriculado na turma!')
    else:
        ras.append(ra)
        if ras_ord == 'c':
            ras.sort()
        elif ras_ord == 'd':
            ras.sort(reverse=True)


def rem_cmd(ra):
    if len(ras) == 0:
        print('Nao ha alunos cadastrados na turma!')
        return

    try:
        pos = ras.index(ra)
        del ras[pos]
    except Exception:
        print("Aluno nao matriculado na turma!")


while True:
    cmd = input()
    if cmd == 's':
        break

    cmd = cmd.split()
    if cmd[0] == 'p':
        print_array(ras)
    elif cmd[0] == 'c':
        ras.sort()
        ras_ord = 'c'
    elif cmd[0] == 'd':
        ras.sort(reverse=True)
        ras_ord = 'd'
    elif cmd[0] == 'b':
        busca_cmd(int(cmd[1]))
    elif cmd[0] == 'i':
        in_cmd(int(cmd[1]))
    elif cmd[0] == 'r':
        rem_cmd(int(cmd[1]))
