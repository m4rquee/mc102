from math import ceil

n = int(input())
db = [input().split() for i in range(n)]
db = [v for v in map(lambda e: (e[0], round(int(e[2]) / int(e[1]), 4)), db)]
esp = {e[0]: 0 for e in db}
for k in esp.keys():
    mults = [v[1] for v in filter(lambda e: e[0] == k, db)]
    esp[k] = round(sum(mults) / len(mults), 4)


def read_line():
    line = input()
    while line != '0 0':
        yield line.split()
        line = input()


result = [ceil(esp[q[0]] * int(q[1]), 1) for q in read_line()]
print(*result, sep='\n')
