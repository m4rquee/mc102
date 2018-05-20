# Lucas de Oliveira Silva - 220715
# O sistema de gerenciamento de turmas da DAC deve ser capaz de realizar operações como impressão,
# ordenação, inclusão, remoção e busca de alunos matriculados em cada turma.
ras = [int(v) for v in input().split()]
ras_ord = None


def busca(v):
    l, r = 0, len(ras)
    inds = []
    while True:
        meio = (l + r) // 2
        inds.append(meio)
        aux = ras[meio]

        if v == aux:
            return True, meio, inds

        if ras_ord == 'c':
            l, r = (meio, r) if v > aux else (l, meio)
        elif ras_ord == 'd':
            l, r = (meio, r) if v < aux else (l, meio)

        if r - l <= 1:
            return False, meio, inds


def print_vets(vet):
    print(' '.join(map(str, vet)))


def busca_cmd():
    global ra, achou, pos
    if ras_ord:
        ra = int(cmd[1])
        achou, pos, inds = busca(ra)
        print_vets(inds)
        if achou:
            print(ra, ' esta na posicao: ', pos)
        else:
            print(ra, ' nao esta na lista!')
    else:
        print('Vetor nao ordenado!')


def in_cmd():
    global ra, achou, pos
    if len(ras) == 150:
        print('Limite de vagas excedido!')
    else:
        ra = int(cmd[1])

        if not ras_ord:
            if not ra in ras:
                print('Aluno ja matriculado na turma!')
            else:
                ras.append(ra)
                return

        achou, pos, _ = busca(ra)
        if achou:
            print('Aluno ja matriculado na turma!')
        else:
            ras.insert(pos, ra)


def rem_cmd():
    if len(ras) == 0:
        print('Nao ha alunos cadastrados na turma!')
        return

    ra = int(cmd[1])
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
        print_vets(ras)
    elif cmd[0] == 'c':
        ras.sort()
        ras_ord = 'c'
    elif cmd[0] == 'd':
        ras.sort(reverse=True)
        ras_ord = 'd'
    elif cmd[0] == 'b':
        busca_cmd()
    elif cmd[0] == 'i':
        in_cmd()
    elif cmd[0] == 'r':
        rem_cmd()
