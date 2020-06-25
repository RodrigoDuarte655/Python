def mdc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


def divideFrac(frac):
    integer = 0
    newNum = frac.getNum()

    while newNum > frac.getDen():
        newNum -= frac.getDen()
        integer += 1

    return integer, newNum


def sumInteger(parteInteira, parteNum):
    integer = parteInteira + parteNum
    return integer


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
        newNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(newNum, novoDen)
        return Fracao(newNum//divComum, novoDen//divComum)


class fracaoMista(Fracao):
    def __init__(self, parteInteira, num, den):
        super().__init__(num, den)
        self.__parteInteira = parteInteira

    def getParteInteira(self):
        return self.__parteInteira

    def merge(self):
        newNum = (self.__parteInteira * self.getDen()) + self.getNum()
        return Fracao(newNum, self.getDen())

    def __add__(self, outraFrac):
        newNum = self.getNum() * outraFrac.getDen() + self.getDen() * outraFrac.getNum()
        novoDen = self.getDen() * outraFrac.getDen()
        divComum = mdc(newNum, novoDen)
        return Fracao(newNum//divComum, novoDen//divComum)

    def __str__(self):
        if self.__parteInteira > 0 and self.getNum() < self.getDen():
            return str(self.__parteInteira) + ' ' + str(self.getNum()) + '/' + str(self.getDen())

        elif self.__parteInteira >= 0 and self.getNum() == self.getDen():
            integer = sumInteger(self.__parteInteira, 1)
            return str(integer)
        else:
            return str(self.getNum()) + '/' + str(self.getDen())


frac1 = Fracao(7, 6)
frac2 = Fracao(13, 7)
frac3 = frac1 + frac2
integer, numerador = divideFrac(frac3)

print(fracaoMista(integer, numerador, frac3.getDen()))
# 7/6 + 13/7 = 3 1/42

print()

frac1 = Fracao(1, 3)
frac2 = Fracao(2, 3)
frac3 = frac1 + frac2
integer, numerador = divideFrac(frac3)

print(fracaoMista(integer, numerador, frac3.getDen()))
# 1/3 + 2/3 = 1

print()

frac1 = fracaoMista(3, 1, 2)
frac2 = fracaoMista(4, 2, 3)
frac3 = frac1.merge() + frac2.merge()
integer, numerador = divideFrac(frac3)

print(fracaoMista(integer, numerador, frac3.getDen()))
# 3 1/2 + 4 2/3 = 8 1/6

print()
