class EmailInvalido(Exception):
    pass


class SenhaFraca(Exception):
    pass


class RAInvalido(Exception):
    pass


def checa_senha(senha):
    if len(senha) < 8:
        return False

    ESP = '!@#$&*'
    maiu, minu, num, car = 0, 0, 0, 0
    for c in senha:
        if c.isupper():
            maiu += 1
        elif c.islower():
            minu += 1
        elif c.isdigit():
            num += 1
        elif c in ESP:
            car += 1
    return maiu >= 1 and minu >= 2 and \
           num >= 2 and car >= 1


def checa_email(email):
    usr, ser_dom = email.split('@')
    ser, dom = ser_dom.split('.')

    if not 2 <= len(dom) <= 4:
        return False
    elif not dom.isalpha():
        return False

    if not ser.isalnum():
        return False

    ESP = '_.+-'
    for c in usr:
        if not (c.isalnum() or c in ESP):
            return False

    return True


def checa_aluno(aluno):
    if not checa_senha(aluno.senha):
        raise SenhaFraca()
    elif not checa_email(aluno.email):
        raise EmailInvalido()


class Repositorio:
    def __init__(self):
        self.alunos = []

    def filtro(self, ra):
        return filter(lambda a: a.ra == ra, self.alunos)

    # Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        if any(self.filtro(aluno.ra)):
            raise RAInvalido()
        checa_aluno(aluno)

        self.alunos.append(aluno)

    # Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        try:
            velho = next(self.filtro(aluno.ra))
        except StopIteration:
            raise RAInvalido()
        checa_aluno(aluno)

        velho.nome = aluno.nome
        velho.ra = aluno.ra
        velho.email = aluno.email
        velho.usuario = aluno.usuario
        velho.senha = aluno.senha

    # Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        try:
            return next(self.filtro(ra))
        except StopIteration:
            raise RAInvalido()

    # Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        old_size = len(self.alunos)
        self.alunos = [a for a in self.alunos if a.ra != ra]
        if old_size == len(self.alunos):
            raise RAInvalido()

    # Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        del self.alunos[:]
