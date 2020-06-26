def getCargaHorariaObrigatoria(aluno, historico, grade1, grade2):
    cargaHoraria = 0
    if aluno.getCurso() == grade1.getCurso():
        for disc in historico.getHistorico():
            for grade in grade1.getDisciplina():
                if disc.getNomeDisciplina() == grade.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()

    elif aluno.getCurso() == grade2.getCurso():
        for disc in historico.getHistorico():
            for grade in grade2.getDisciplina():
                if disc.getNomeDisciplina() == grade.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()

    return cargaHoraria


def getCargaHorariaOptativa(aluno, historico, grade1, grade2):
    cargaHoraria = 0
    if aluno.getCurso() != grade1.getCurso():
        for disc in historico.getHistorico():
            for grade in grade1.getDisciplina():
                if disc.getNomeDisciplina() == grade.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()

    elif aluno.getCurso() != grade2.getCurso():
        for disc in historico.getHistorico():
            for grade in grade2.getDisciplina():
                if disc.getNomeDisciplina() == grade.getNomeDisciplina():
                    cargaHoraria += disc.getCargaHoraria()

    return cargaHoraria


class Aluno:

    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    def getnroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome

    def getCurso(self):
        return self.__curso


class Curso:

    def __init__(self, nome):
        self.__nome = nome
        self.__grade = None

    def getNomeCurso(self):
        return self.__nome

    def getGrade(self):
        return self.__grade


class Grade:

    def __init__(self, ano, curso):
        self.__ano = ano
        self.__curso = curso
        self.__disciplinas = []

    def getAno(self):
        return self.__ano

    def getCurso(self):
        return self.__curso

    def getDisciplina(self):
        return self.__disciplinas

    def addDisciplina(self, codigo, nome, cargaHoraria):
        disci = Disciplina(codigo, nome, cargaHoraria, self)
        self.__disciplinas.append(disci)


class Historico:

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def getAluno(self):
        return self.__aluno

    def getHistorico(self):
        return self.__disciplinas

    def addDisciplina(self, codigo, nome, cargaHoraria):
        disc = Disciplina(codigo, nome, cargaHoraria)
        self.__disciplinas.append(disc)


class Disciplina:

    def __init__(self, codigo, nome, cargaHoraria, grade=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__grade = grade

    def getNomeDisciplina(self):
        return self.__nome

    def getCodigo(self):
        return self.__codigo

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getGrade(self):
        return self.__grade


Curso1 = Curso('Sistemas de informação')
grade1 = Grade(2020, Curso1)
grade1.addDisciplina(1, 'Estrutura de dados', 48)
grade1.addDisciplina(2, 'Computação Orientada a Objetos I', 32)
grade1.addDisciplina(3, 'Probabilidade e estatística', 64)
grade1.addDisciplina(4, 'Matemática discreta', 64)

Curso2 = Curso('Administração')
grade2 = Grade(2016, Curso2)
grade2.addDisciplina(1, 'Introducão a administração', 64)
grade2.addDisciplina(2, 'Comportamento Organizacional', 32)
grade2.addDisciplina(3, 'Contabilidade', 64)

Aluno1 = Aluno(2019003520, 'Rodrigo Duarte', Curso1)
Historico1 = Historico(Aluno1)
Historico1.addDisciplina(1, 'Estrutura de dados', 48)
Historico1.addDisciplina(2, 'Computação Orientada a Objetos I', 32)
Historico1.addDisciplina(3, 'Probabilidade e estatística', 64)
Historico1.addDisciplina(4, 'Comportamento Organizacional', 32)

Aluno2 = Aluno(2019006235, 'Sofia Ribeiro', Curso2)
Historico2 = Historico(Aluno2)
Historico2.addDisciplina(1, 'Introducão a administração', 64)
Historico2.addDisciplina(2, 'Comportamento Organizacional', 32)
Historico2.addDisciplina(3, 'Computação Orientada a Objetos I', 32)

print('\n-----------------------Aluno 1------------------------\n')
print(f'Aluno: {Aluno1.getNome()}')
print(f'Matrícula: {Aluno1.getnroMatric()}')

print('\n-----------------------Histórico------------------------\n')
for historico in Historico1.getHistorico():

    print(f'Código: {historico.getCodigo()},  Disciplina: {historico.getNomeDisciplina()}, Carga horária: {historico.getCargaHoraria()}')

print(
    f'Total de carga horária obrigatória cursada: {getCargaHorariaObrigatoria(Aluno1, Historico1, grade1, grade2)}')
print(
    f'Total de carga horária optativa cursada: {getCargaHorariaOptativa(Aluno1, Historico1, grade1, grade2)}')

print('\n-----------------------Aluno 2-------------------------\n')

print(f'Aluno: {Aluno2.getNome()}')
print(f'Matricula: {Aluno2.getnroMatric()}')

print('\n-----------------------Histórico------------------------\n')

for historico in Historico2.getHistorico():

    print(f'Código: {historico.getCodigo()},  Disciplina: {historico.getNomeDisciplina()}, Carga horária: {historico.getCargaHoraria()}')
print(
    f'Total de carga horária obrigatória cursada: {getCargaHorariaObrigatoria(Aluno2, Historico2, grade1, grade2)}')
print(
    f'Total de carga horária optativa cursada: {getCargaHorariaOptativa(Aluno2, Historico2, grade1, grade2)}')

print()
