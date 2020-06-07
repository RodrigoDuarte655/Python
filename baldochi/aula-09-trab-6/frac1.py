def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class Fracao:

    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum

    def __add__(self, outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        novaFracao = Fracao(novoNum//divComum, novoDen//divComum)

        if novaFracao.getNum() / novaFracao.getDen() < 1:
            return novaFracao
        elif novaFracao.getNum() / novaFracao.getDen() > 1:
            partInt = novaFracao.getNum() // novaFracao.getDen()
            num = novaFracao.getNum() - partInt * novaFracao.getDen()
            den = novaFracao.getDen()
            return FracaoMista(partInt, num, den)
        else:
            return novaFracao.getNum() // novaFracao.getDen()


class FracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira

    def __str__(self):
        return str(self.__parteInteira) + ' ' + str(self.getNum()) + '/' + str(self.getDen())


frac1 = Fracao(7, 6)
frac2 = Fracao(13, 7)
frac3 = frac1 + frac2
print(frac3)

print()

frac1 = Fracao(1, 3)
frac2 = Fracao(2, 3)
frac3 = frac1 + frac2
print(frac3)


print()

fmista1 = FracaoMista(3, 1, 2)
fmista2 = FracaoMista(4, 2, 3)
fmista3 = fmista1 + fmista2
print(fmista3)
