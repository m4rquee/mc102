# Lucas de Oliveira Silva 220715
n = int(input())
pmatrix = [[float(input()) for v in range(n)] for _ in range(4)]
pdiff = [[l[i + 1] - l[i] for i in range(n - 1)] for l in pmatrix]
print(pdiff)
