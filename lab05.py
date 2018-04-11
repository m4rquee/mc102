import math

#       ryu     ken
vida = {-1: 50, 1: 50}
nomes = {-1: 'Ryu', 1: 'Ken'}

rounds_ganhos = [0, 0]

golpe_ant = None


def ganhador():
    if rounds_ganhos[0] > rounds_ganhos[1]:
        return nomes[-1]
    else:
        return nomes[1]


def sgn(x):
    return 0 if x == 0 else (x / math.fabs(x))


def acabou():
    return vida[-1] <= 0 or vida[1] <= 0


def read_golpes():
    while not acabou():
        try:
            yield int(input())
        except Exception:
            pass


def gen_combos():
    global golpe_ant
    if golpe_ant:
        soma = golpe_ant
        golpe_ant = None
    else:
        soma = 0

    for golpe in read_golpes():
        sgns = sgn(soma)
        if soma == 0 or sgns == sgn(golpe):
            soma += golpe
            sgns = sgn(soma)
            if vida[sgns] - soma <= 0:
                golpe_ant = None
                rounds_ganhos[int(jog)] += 1
                break
        else:
            golpe_ant = golpe
            break

    return sgns, math.fabs(soma)


for round in (1, 2):
    while not acabou():
        jog, combo = gen_combos()
        print('%s: %i - %i = %i'
              % (nomes[jog], vida[jog], combo, vida[jog] - combo))
        vida[jog] -= combo

    vida[-1] = 50
    vida[1] = 50

if rounds_ganhos[0] == rounds_ganhos[1]:
    print('empatou')
else:
    print('%s venceu' % ganhador())
