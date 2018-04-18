# Lucas de Oliveira Silva 220715
import re


def read_ops():
    line = input()
    while line.upper() != 'Q':
        yield line
        line = input()


reg_pal = '((?<=^)|(?<=\s))%s(?!\w)'  # Regex para dar match em palavras
ops_nargs = {'D': 1 + 1, 'I': 1 + 1, 'R': 2 + 1}  # Número de parâmetros de cada operação, por conveniência soma-se 1

texto = input()
cmds = list(read_ops())

i = 0
while i < len(cmds):
    print(texto)
    operacao = cmds[i].upper()
    nargs = ops_nargs[operacao]
    args = cmds[i + 1:i + nargs]  # Parâmetros da operação
    i += nargs  # Pula para a próxima operação

    new_str = ''  # String a ser colocada no lugar do argumento da operação
    if operacao == 'I':
        reg = re.compile(reg_pal % args[0], flags=re.IGNORECASE)
        new_str = reg.search(texto).group()[::-1]
    elif operacao == 'R':
        new_str = args[1]

    # Substitui o argumento da operação pela nova str:
    texto = re.sub(reg_pal % args[0], new_str, texto, flags=re.IGNORECASE)

    texto = re.sub('\s+', ' ', texto)
    texto = re.sub('\s\W', '', texto)

print(texto)
