# Lucas de Oliveira Silva - 220715
# Versao modificada do jogo Batalha naval para dois jogadores.
def read_t(l):
    ret = {'count': 0, 't': {}}
    for i in range(l):
        ret['t'][i] = {}
        for j, v in enumerate(input()):
            ret['count'] += v == '@'
            ret['t'][i][j] = v
    return ret


def eliminate_path(x, y, t):
    tab = t['t']
    if tab[x][y] == '@':
        tab[x][y] = '-'
        t['count'] -= 1
        if tab.get(x - 1, {}).get(y, '-') == '@':
            eliminate_path(x - 1, y, t)
        if tab.get(x + 1, {}).get(y, '-') == '@':
            eliminate_path(x + 1, y, t)
        if tab[x].get(y - 1, '-') == '@':
            eliminate_path(x, y - 1, t)
        if tab[x].get(y + 1, '-') == '@':
            eliminate_path(x, y + 1, t)


L, C = [int(v) for v in input().split('x')]
t1, t2 = read_t(L), read_t(L)

jog = False
while t1['count'] > 0 and t2['count'] > 0:
    X, Y = [int(v) for v in input().split(',')]
    eliminate_path(X - 1, Y - 1, t1 if jog else t2)
    enem_list = t1['t'].values() if jog else t2['t'].values()
    enem_lines = map(lambda line: ''.join(line.values()), enem_list)

    print('Ataque em (%i,%i) do jogador %i' % (X, Y, int(jog) + 1))
    print('\n'.join(enem_lines))
    jog = not jog
