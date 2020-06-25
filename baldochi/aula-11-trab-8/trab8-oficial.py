# Trabalho 08 - Rodrigo Duarte Silva Luz - 2019003520

from abc import ABC, abstractmethod


class InvalidTitulation(Exception):
    pass


class ProfessorAgeInvalid(Exception):
    pass


class InvalidCourse(Exception):
    pass


class StudentAgeInvalid(Exception):
    pass


class CpfDuplicated(Exception):
    pass


class Pessoa(ABC):

    def __init__(self, nome, endereco, idade, CPF):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__CPF = CPF

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getCPF(self):
        return self.__CPF

    @abstractmethod
    def printDescricao(self):
        pass


class Professor(Pessoa):

    def __init__(self, nome, endereco, idade, CPF, titulacao):
        super().__init__(nome, endereco, idade, CPF)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('--------Professor cadastrado com sucesso-------')
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Titulação: {self.__titulacao}')
        print()


class Aluno(Pessoa):

    def __init__(self, nome, endereco, idade, CPF, curso):
        super().__init__(nome, endereco, idade, CPF)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('--------Aluno cadastrado com sucesso-------')
        print(f'Nome: {self.getNome()}')
        print(f'Endereço: {self.getEndereco()}')
        print(f'Idade: {self.getIdade()}')
        print(f'CPF: {self.getCPF()}')
        print(f'Curso: {self.__curso}')
        print()


Alunos = [
    ('Rodrigo', 'Itajubá', 22, '12766425632', 'SIN'),
    ('Sofia', 'Itajuba', 20, '66394007668', 'SIN'),
    ('Maria', 'Piranguinho', 18, '12766425632', 'CCO'),
    ('Elizabeth', 'Pouso Alegre', 17, '44573957263', 'CCO'),
    ('Matheus', 'São Tomé das Letras', 21, '73266456745', 'ADM')
]

Professores = [
    ('José', 'Piranguçu', 31, '84728454243', 'Doutor'),
    ('Alberto', 'Poços de Caldas', 47, '53453986538', 'Doutor'),
    ('Márcio', 'Campos do Jordão', 32, '84728454243', 'Doutor'),
    ('Rosana', 'Delfim Moreira', 26, '53593245639', 'Doutor'),
    ('Sebastiana', 'Itajuba', 30, '31948395039', 'Mestre'),
]

cadastroAluno = {}
cadastroProfessor = {}

print('\n----------Cadastro de alunos----------\n')
for nome, end, idade, cpf, curso in Alunos:
    try:
        if curso != 'SIN' and curso != 'CCO':
            raise InvalidCourse()

        if idade < 18:
            raise StudentAgeInvalid()

        if cpf in cadastroAluno:
            raise CpfDuplicated()

    except InvalidCourse:
        print(f'Cadastro incorreto: Curso {curso} não permitido!\n')

    except StudentAgeInvalid:
        print(
            f'Cadastro incorreto: Idade {idade} não permitida! (Deve ser igual ou maior que 18 anos)\n')

    except CpfDuplicated:
        print(f'Cadastro incorreto: CPF {cpf} já existente!\n')

    else:
        cadastroAluno[cpf] = Aluno(nome, end, idade, cpf, curso)
        cadastroAluno[cpf].printDescricao()

print('\n----------Cadastro de professores----------\n \n')
for nome, end, idade, cpf, titulo in Professores:
    try:
        if titulo != 'Doutor':
            raise InvalidTitulation()

        if idade < 30:
            raise ProfessorAgeInvalid()

        if cpf in cadastroProfessor:
            raise CpfDuplicated()

    except InvalidTitulation:
        print(
            f'Cadastro incorreto: Títulação de {titulo} não permitido! (Deve ser Doutor)\n')

    except ProfessorAgeInvalid:
        print(
            f'Cadastro incorreto: Idade {idade} não permitida! (Deve ser igual ou maior que 30 anos)\n')

    except CpfDuplicated:
        print(f'Cadastro incorreto: CPF {cpf} já existe!\n')

    else:
        cadastroProfessor[cpf] = Professor(nome, end, idade, cpf, titulo)
        cadastroProfessor[cpf].printDescricao()
