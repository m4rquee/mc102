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
            print(' '.join(map(str, inds)))
            return True, meio

        if ras_ord == 'c':
            l, r = (meio, r) if v > aux else (l, meio)
        elif ras_ord == 'd':
            l, r = (meio, r) if v < aux else (l, meio)

        if l == r:
            print(' '.join(map(str, inds)))
            return False, meio


def print_ras():
    print(' '.join(map(str, ras)))


def busca_cmd():
    global ra, achou, pos
    if ras_ord:
        ra = int(cmd[1])
        achou, pos = busca(ra)
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

        achou, pos = busca(ra)
        if achou:
            print('Aluno ja matriculado na turma!')
        else:
            ras.insert(pos, ra)


while True:
    cmd = input()
    if cmd == 's':
        break

    cmd = cmd.split()
    if cmd[0] == 'p':
        print_ras()
    elif cmd[0] == 'c':
        ras.sort()
        print_ras()
        ras_ord = 'c'
    elif cmd[0] == 'd':
        ras.sort(reverse=True)
        print_ras()
        ras_ord = 'd'
    elif cmd[0] == 'b':
        busca_cmd()
    elif cmd[0] == 'i':
        in_cmd()
    elif cmd[0] == 'r':
        if len(ras):
            print('Nao ha alunos cadastrados na turma!')
            continue

        ra = int(cmd[1])
        try:
            pos = ras.index(ra)
            del ras[pos]
        except Exception:
            print("Aluno nao matriculado na turma!")
