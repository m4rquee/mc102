#!/usr/bin/env python3
# Lucas de Oliveira SIlva - 220715

from lab20_main import print_sudoku


def valid_movs(tab, i, j):
    movs = set(range(1, 9 + 1))

    movs -= set([tab[x][j] for x in range(9)])
    movs -= set(tab[i])

    b_pos = [3 * (i // 3), 3 * (j // 3)]
    for x in range(b_pos[0], b_pos[0] + 3):
        for y in range(b_pos[1], b_pos[1] + 3):
            movs -= {tab[x][y]}

    return movs


# Funcao: resolve
# Resolve o Sudoku da matriz tab.
# Retorna True se encontrar uma resposta, False caso contrario
def resolve(tab, i_i=0):
    for i in range(i_i, 9):
        for j in range(9):
            if tab[i][j] == 0:
                for p in valid_movs(tab, i, j):
                    tab[i][j] = p
                    print_sudoku(tab)
                    if resolve(tab, i):
                        return True
                    tab[i][j] = 0
                return False
    return True
