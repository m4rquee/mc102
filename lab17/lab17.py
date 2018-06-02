class EmailInvalido(Exception):
    pass


class SenhaFraca(Exception):
    pass


class RAInvalido(Exception):
    pass


class Repositorio:
    def __init__(self):
        self.alunos = []

    # Este método recebe o parâmetro aluno e o insere no repositório
    def adicionar(self, aluno):
        pass

    # Este método recebe o parâmetro aluno e altera, no repositório, os dados do aluno com RA igual a aluno.ra
    def alterar(self, aluno):
        pass

    # Este método recebe o parâmetro ra e deve retornar o aluno que possui o RA informado como parâmetro
    def achaAluno(self, ra):
        pass

    # Este método recebe o parâmetro ra e deve remover o aluno correspondente do repositório
    def remover(self, ra):
        pass

    # Este método exclui todos os alunos do repositório.
    def limparRepositorio(self):
        pass
