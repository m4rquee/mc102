# Lucas de Oliveira Silva 220715
import re


# Recebe as operações
def read_ops():
    line = input()
    while line.upper() != 'Q':
        yield line
        line = input()


reg_pal = '(?<!\w)%s(?!\w)'  # Regex para dar match em palavras separadas
ops_nargs = {'D': 1 + 1, 'I': 1 + 1, 'R': 2 + 1}  # Número de parâmetros de cada operação, por conveniência soma-se 1

texto = input()
cmds = list(read_ops())

i = 0
while i < len(cmds):
    print(texto)
    operacao = cmds[i].upper()
    nargs = ops_nargs[operacao]  # Número de parâmetros dessa operação

    args = cmds[i + 1:i + nargs]  # Parâmetros da operação
    i += nargs  # Pula para a próxima operação

    if operacao == 'I':
        reg = re.compile(reg_pal % args[0], flags=re.IGNORECASE)
        matches = reg.findall(texto)
        for match in matches:
            texto = re.sub(match, match[::-1], texto, 1)
    else:
        if operacao == 'R':
            new_str = args[1]
        elif operacao == 'D':
            new_str = ''

        # Substitui o argumento da operação pela nova string:
        texto = re.sub(reg_pal % args[0], new_str, texto, flags=re.IGNORECASE)

        if operacao == 'D':
            texto = re.sub('\s[,\.\?\!\:]', '', texto)
            texto = re.sub('\s\s+', ' ', texto)

texto = re.sub('\s\s+', ' ', texto)
print(texto)
