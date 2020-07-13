import tkinter as tk
from tkinter import messagebox


class FillAllFields(Exception):
    pass


class StudentAlreadyRegistered(Exception):
    pass


class EmptyField(Exception):
    pass


class MatriculaRepeated(Exception):
    pass


class Estudante:

    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    def getNroMatric(self):
        return self.__nroMatric

    def getNome(self):
        return self.__nome


class LimiteInsereEstudantes(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro, text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)


class LimiteConsultaEstudantes(tk.Toplevel):

    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar estudante")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameButton.pack()

        self.labelNro = tk.Label(self.frameNro, text='Nro Matrícula:  ')
        self.labelNro.pack(side='left')

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side='left')

        self.buttonConsulta = tk.Button(
            self.frameButton, text='Consultar', font=('Negrito', 9))
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(
            self.frameButton, text='Concluído', font=('Negrito', 9))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", controle.concluiHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlEstudante():
    def __init__(self):
        self.listaEstudantes = [
            Estudante('1001', 'Joao Santos'),
            Estudante('1002', 'Marina Cintra'),
            Estudante('1003', 'Felipe Reis'),
            Estudante('1004', 'Ana Souza')
        ]

    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.getNroMatric() == nroMatric:
                estRet = est
        return estRet

    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.getNroMatric())
        return listaNro

    def insereEstudantes(self):
        self.limiteIns = LimiteInsereEstudantes(self)

    def mostraEstudantes(self):
        if len(self.listaEstudantes) == 0:
            str = "Não existem alunos cadastrados"
            self.limiteLista = LimiteMostraEstudantes(str)
        else:
            str = "Nro Matric. -- Nome\n"
            for est in self.listaEstudantes:
                str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'
            self.limiteLista = LimiteMostraEstudantes(str)

    def consultaEstudantes(self):
        self.limiteCon = LimiteConsultaEstudantes(self)

    def enterHandler(self, event):
        try:
            if len(self.limiteIns.inputNro.get()) == 0 or len(self.limiteIns.inputNome.get()) == 0:
                raise FillAllFields()
            for estud in self.listaEstudantes:
                if estud.getNroMatric() == self.limiteIns.inputNro.get() and estud.getNome() == self.limiteIns.inputNome.get():
                    raise StudentAlreadyRegistered()
                if estud.getNroMatric() == self.limiteIns.inputNro.get():
                    raise MatriculaRepeated()
        except StudentAlreadyRegistered:
            self.limiteIns.mostraJanela(
                'Cuidado, atenção!', 'Estudante já cadastrado!')
        except FillAllFields:
            self.limiteIns.mostraJanela(
                'Cuidado, atenção!', 'Por favor, preencha todos os campos!')
        except MatriculaRepeated:
            self.limiteIns.mostraJanela(
                'Cuidado, atenção!', 'Número de matrícula já está existe!')

        else:
            nroMatric = self.limiteIns.inputNro.get()
            nome = self.limiteIns.inputNome.get()
            estudante = Estudante(nroMatric, nome)
            self.listaEstudantes.append(estudante)
            self.limiteIns.mostraJanela(
                'Sucesso', 'Estudante cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputNro.get()) == 0:
                raise EmptyField()
        except EmptyField:
            str = 'Campo de matrícula vazio! Por favor, digite um número de matrícula!'
            self.limiteCon.mostraJanela('Erro', str)

        else:
            nroMatric = self.limiteCon.inputNro.get()
            est = self.getEstudante(nroMatric)
            if est == None:
                str = (f'Não existe aluno com a matrícula {nroMatric}')
                self.limiteCon.mostraJanela('Aluno não encontrado', str)
                self.limiteCon.inputNro.delete(
                    0, len(self.limiteCon.inputNro.get()))
            else:
                str = 'Informações do aluno consultado:\n'
                str += 'Nro Matric. -- Nome\n'
                str += est.getNroMatric() + ' -- ' + est.getNome()
                self.limiteCon.mostraJanela('Aluno encontrado', str)
                self.limiteCon.inputNro.delete(
                    0, len(self.limiteCon.inputNro.get()))

    def concluiHandler(self, event):
        self.limiteCon.destroy()
