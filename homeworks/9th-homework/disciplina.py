import tkinter as tk
from tkinter import messagebox


class CodeNameRepeated(Exception):
    pass


class EmptyField(Exception):
    pass


class FillAllFields(Exception):
    pass


class Disciplina:

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome


class LimiteInsereDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Disciplina")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=20)
        self.inputCodigo.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(
            self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(
            self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(
            self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraDisciplinas():
    def __init__(self, str):
        messagebox.showinfo('Lista de disciplinas', str)


class LimiteConsultaDisciplinas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar disciplinas")
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameCode.pack()
        self.frameButtons.pack()

        self.labelCode = tk.Label(self.frameCode, text='Código:  ')
        self.labelCode.pack(side='left')

        self.inputCode = tk.Entry(self.frameCode, width=20)
        self.inputCode.pack(side='left')

        self.buttonConsulta = tk.Button(
            self.frameButtons, text='Consultar', font=('Negrito', 9))
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(
            self.frameButtons, text='Concluído', font=('Negrito', 9))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlDisciplina():
    def __init__(self):
        self.listaDisciplinas = [
            Disciplina('COM220', 'Programação OO'),
            Disciplina('COM222', 'Programação Web'),
            Disciplina('COM111', 'Estruturas de Dados')
        ]

    def getListaDisciplinas(self):
        return self.listaDisciplinas

    def getDisciplina(self, codDisc):
        discRet = None
        for disc in self.listaDisciplinas:
            if disc.getCodigo() == codDisc:
                discRet = disc
        return discRet

    def getListaCodDisciplinas(self):
        listaCod = []
        for disc in self.listaDisciplinas:
            listaCod.append(disc.getCodigo())
        return listaCod

    def insereDisciplinas(self):
        self.limiteIns = LimiteInsereDisciplinas(self)

    def mostraDisciplinas(self):
        if len(self.listaDisciplinas) == 0:
            str = 'Não existe disciplinas cadastradas!'
        else:
            str = 'Código -- Nome\n'
            for disc in self.listaDisciplinas:
                str += disc.getCodigo() + ' -- ' + disc.getNome() + '\n'
            self.limiteLista = LimiteMostraDisciplinas(str)

    def consultaDisciplinas(self):
        self.limiteCon = LimiteConsultaDisciplinas(self)

    def enterHandler(self, event):
        try:
            if len(self.limiteIns.inputCodigo.get()) == 0 or len(self.limiteIns.inputNome.get()) == 0:
                raise FillAllFields()
            for disc in self.listaDisciplinas:
                if disc.getCodigo() == self.limiteIns.inputCodigo.get() or disc.getNome() == self.limiteIns.inputNome.get():
                    raise CodeNameRepeated()
        except FillAllFields:
            self.limiteIns.mostraJanela(
                'Cuidado, atenção!', 'Por favor, preencha todos os campos!')
        except CodeNameRepeated:
            str = f'O código {self.limiteIns.inputCodigo.get()} ou o nome {self.limiteIns.inputNome.get()} já estão sendo usado para alguma disciplina!'
            self.limiteIns.mostraJanela('Cuidado, atenção!', str)

        else:
            Code = self.limiteIns.inputCodigo.get()
            nome = self.limiteIns.inputNome.get()
            disciplina = Disciplina(Code, nome)
            self.listaDisciplinas.append(disciplina)
            self.limiteIns.mostraJanela(
                'Parabéns, sucesso', 'Disciplina cadastrada com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(
            0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputCode.get()) == 0:
                raise FillAllFields()
        except FillAllFields:
            str = 'Campo de matrícula vazio! Por favor, digite um número de matrícula!'
            self.limiteCon.mostraJanela('Falha', str)

        else:
            Code = self.limiteCon.inputCode.get()
            disc = self.getDisciplina(Code)
            if disc == None:
                str = ('Não existe disciplina com o código {}'.format(Code))
                self.limiteCon.mostraJanela(
                    'Disciplina não foi encontrada', str)
                self.limiteCon.inputCode.delete(
                    0, len(self.limiteCon.inputCode.get()))
            else:
                str = 'Informações da disciplina consultada:\n'
                str += 'Código -- Nome\n'
                str += disc.getCodigo() + ' -- ' + disc.getNome()
                self.limiteCon.mostraJanela('Opa, Disciplina encontrada!', str)
                self.limiteCon.inputCode.delete(
                    0, len(self.limiteCon.inputCode.get()))

    def concluiHandler(self, event):
        self.limiteCon.destroy()
