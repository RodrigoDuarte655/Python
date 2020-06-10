# Rodrigo Duarte Silva Luz, 2019003520.


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

        if novaFracao.getNum() / novaFracao.getDen() > 1:
            intPart = novaFracao.getNum() // novaFracao.getDen()
            novoNum2 = novaFracao.getNum() - intPart * novaFracao.getDen()
            fracMista = fracaoMista(intPart, novoNum2, novaFracao.getDen())
            return fracMista
        else:
            return novaFracao.getNum() // novaFracao.getDen()


class fracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira

    def __str__(self):
        return str(self.__parteInteira) + ' ' + str(self.getNum()) + '/' + str(self.getDen())

    def __add__(self, outraFrac):
        numerator = (self.getDen() * self.__parteInteira) + self.getNum()
        newNumerator = (outraFrac.getDen() *
                        outraFrac.getParteInteira()) + outraFrac.getNum()

        mmcNumerator = numerator * outraFrac.getDen() + self.getDen() * newNumerator
        mmcDenominator = self.getDen() * outraFrac.getDen()

        intPart = mmcNumerator // mmcDenominator
        FinalNum = mmcNumerator % mmcDenominator
        FinalDen = mmcDenominator
        return fracaoMista(intPart, FinalNum, FinalDen)


# 7/6 + 13/7 = 3 1/42
frac1 = Fracao(7, 6)
frac2 = Fracao(13, 7)
frac3 = frac1 + frac2
print(frac3)
print()

# 1/3 + 2/3 = 1
frac1 = Fracao(1, 3)
frac2 = Fracao(2, 3)
frac3 = frac1 + frac2
print(frac3)
print()

# 3 1/2 + 4 2/3 = 8 1/6
frac1 = fracaoMista(3, 1, 2)
frac2 = fracaoMista(4, 2, 3)
frac3 = frac1 + frac2
print(frac3)
print()
