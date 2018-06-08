# Lucas de OLiveira Silva - RA: 220715
# Programa de convolucao de imagens
import sys

img_file = open(sys.argv[1], 'r')
m_file = open(sys.argv[2], 'r')

# Dados da foto
f_type = img_file.readline()
size = [int(v) for v in img_file.readline().split()]
max_v = int(img_file.readline())
img = [[int(v) for v in img_file.readline().split()] for _ in range(size[1])]

# Dados da matriz de convolucao
D = int(m_file.readline())
M = [[int(v) for v in m_file.readline().split()] for _ in range(3)]

# Aplicacao da matriz
print(f_type[:-1])
print(str(size[0]) + ' ' + str(size[1]))
print(max_v)


def p_prime():
    if i == 0 or i == size[1] - 1 or j == 0 or j == size[0] - 1:
        return img[i][j]

    avg = 0
    for x in range(3):
        for y in range(3):
            avg += M[x][y] * img[i + x - 1][j + y - 1]

    return min(max_v, max(0, avg // D))


for i in range(size[1]):
    for j in range(size[0]):
        print(p_prime(), end=' ')
    print(' ')
