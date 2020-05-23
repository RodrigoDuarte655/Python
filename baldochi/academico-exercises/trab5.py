from abc import ABC, abstractclassmethod


class EmpDomestica(ABC):
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def getNome(self):
        return self.__nome

    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setTelefone(self, telefone):
        self.__telefone = telefone

    @abstractclassmethod
    def getSalario(self):
        pass


class Horista(EmpDomestica):
    def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorPorHora = valorPorHora

    def getSalario(self):
        return self.__horasTrabalhadas * self.__valorPorHora


class Diarista(EmpDomestica):
    def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorPorDia = valorPorDia

    def getSalario(self):
        return self.__diasTrabalhados * self.__valorPorDia


class Mensalista(EmpDomestica):
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def getSalario(self):
        return self.__valorMensal


# faça um teste automatizado para imprimir qual será mais barato para a república (Imprimir nome, telefone e salário)
def valorMensalMaisBarato(emp1, emp2, emp3):
    maisBarato = emp1
    if emp2.getSalario() < maisBarato.getSalario():
        maisBarato = emp2
    if emp3.getSalario() < maisBarato.getSalario():
        maisBarato = emp3

    print(
        f'O valor mensal mais barato é o da empregada {maisBarato.getNome()}, cujo telefone é {maisBarato.getTelefone()} e salário é {maisBarato.getSalario()} reais.')


# Instanciando os objetos que são as empregadas
horista = Horista('', 553599925634, 160, 10)
horista.setNome('Sofia')

diarista = Diarista('', 5535998341256, 20, 55)
diarista.setNome('Gabrielly')

mensalista = Mensalista('', 5535999231285, 1000)
mensalista.setNome('Letícia')

# Imprima o valor mensal de salário de cada empregada
print('--------------Valores mensais das empregadas:--------------\n')
print(
    f'O salário mensal da horista {horista.getNome()} é {horista.getSalario()} reais, e seu telefone é {horista.getTelefone()}.')

print()

print(
    f'O salário mensal da diarista {diarista.getNome()} é {diarista.getSalario()} reais, e seu telefone é {diarista.getTelefone()}.')

print()

print(
    f'O salário mensal da mensalista {mensalista.getNome()} é {mensalista.getSalario()} reais, e seu telefone é {mensalista.getTelefone()}.')

print()

print('--------------Teste automatizado para detectar a empregada mais barata:--------------\n')
# Chamada do teste automatizado
valorMensalMaisBarato(horista, diarista, mensalista)
