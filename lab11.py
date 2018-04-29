# Lucas de Oliveira Silva 220715
m, n = (int(i) for i in input().split())
ites = int(input())
grade = {l: dict(enumerate(input().split())) for l in range(m)}
regras = {'0': lambda viz: '1' if viz[0] == 2 else '0', '1': lambda viz: '2' if viz[1] >= 1 else '1',
          '2': lambda viz: '0' if viz[0] >= 2 else ('0' if viz[0] == 0 else '2')}


def n_viz(i, j):
    ret = [-(grade[i][j] == '1'), -(grade[i][j] == '2')]
    for y in range(-1, 2):
        for x in range(-1, 2):
            viz = grade.get(i + y, {}).get(j + x, '0')
            ret[0] += viz == '1'
            ret[1] += viz == '2'
    return ret


print('iteracao 0\n' + '\n'.join(map(lambda l: ''.join(l.values()), grade.values())))
for it in range(ites):
    grade = {i: {j: regras[v](n_viz(i, j)) for j, v in l.items()} for i, l in grade.items()}
    print('iteracao %i\n' % (it + 1) + '\n'.join(map(lambda l: ''.join(l.values()), grade.values())))
