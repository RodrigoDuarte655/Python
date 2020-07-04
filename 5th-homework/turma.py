import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est
import disciplina as disc


class ClassDuplicated(Exception):
    pass


class FillAllFields(Exception):
    pass


class Turma:

    def __init__(self, codigo, disciplina, estudantes):
        self.__codigo = codigo
        self.__disciplina = disciplina
        self.__estudantes = estudantes

    def getCodigo(self):
        return self.__codigo

    def getDisciplina(self):
        return self.__disciplina

    def getEstudantes(self):
        return self.__estudantes


class LimiteInsereTurma(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Disciplina")
        self.controle = controle

        self.frameCodTurma = tk.Frame(self)
        self.frameDiscip = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodTurma.pack()
        self.frameDiscip.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()

        self.labelCodTurma = tk.Label(
            self.frameCodTurma, text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(
            self.frameDiscip, text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(
            self.frameDiscip, width=15, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip

        self.labelEst = tk.Label(
            self.frameEstudante, text="Escolha o estudante: ")
        self.labelEst.pack(side="left")
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(
            self.frameButton, text="Insere Aluno", font=('Negrito', 9))
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(
            self.frameButton, text="Cria Turma", font=('Negrito', 9))
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)

        self.buttonConcluido = tk.Button(
            self.frameButton, text='Concluído', font=('Negrito', 9))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", controle.concluiInsertionHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)


class LimiteConsultaTurmas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('350x100')
        self.title("Consultar turmas")
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameCode.pack()
        self.frameButtons.pack()

        self.labelCode = tk.Label(
            self.frameCode, text='Código da disciplina:  ')
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
        self.buttonConcluido.bind("<Button>", controle.concluiConsultaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlTurma():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaTurmas = []
        self.listaAlunosTurma = []

        self.listaNroMatric = []

    def insereTurmas(self):
        self.listaAlunosTurma = []
        listaCodDisc = self.ctrlPrincipal.ctrlDisciplina.getListaCodDisciplinas()
        self.listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = LimiteInsereTurma(
            self, listaCodDisc, self.listaNroMatric)

    def criaTurma(self, event):
        try:
            if len(self.limiteIns.inputCodTurma.get()) == 0 or len(self.limiteIns.escolhaCombo.get()) == 0:
                raise FillAllFields()
        except FillAllFields:
            self.limiteIns.mostraJanela(
                'Cuidado, atenção!', 'Preencha todos os campos! Está faltando o código ou a disciplina!')

        else:
            codTurma = self.limiteIns.inputCodTurma.get()
            discSel = self.limiteIns.escolhaCombo.get()
            disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
            turma = Turma(codTurma, disc, self.listaAlunosTurma)
            try:
                for turmas in self.listaTurmas:
                    if turma.getCodigo() == turmas.getCodigo():
                        raise ClassDuplicated()
            except ClassDuplicated:
                str = f'Turma com o código {codTurma} já está cadastrada!'
                self.limiteIns.mostraJanela('Erro', str)

            else:
                self.listaTurmas.append(turma)
                self.limiteIns.mostraJanela(
                    'Sucesso', 'A Turma foi criada com sucesso')
                self.limiteIns.inputCodTurma.delete(
                    0, len(self.limiteIns.inputCodTurma.get()))

    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosTurma.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno foi matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    def mostraTurmas(self):
        str = ''
        if len(self.listaTurmas) == 0:
            str += 'Não há turmas cadastradas ainda!'
            self.limiteLista = LimiteMostraTurmas(str)
        else:
            for turma in self.listaTurmas:
                str += 'Código: ' + turma.getCodigo() + '\n'
                str += 'Disciplina: ' + turma.getDisciplina().getCodigo() + '\n'
                str += 'Estudantes:\n'
                for estud in turma.getEstudantes():
                    str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
                str += '------\n'

            self.limiteLista = LimiteMostraTurmas(str)

    def consultaTurmas(self):
        self.limiteCon = LimiteConsultaTurmas(self)

    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputCode.get()) == 0:
                raise FillAllFields()
        except FillAllFields:
            str = 'Por favor, digite o código da disciplina!'
            self.limiteCon.mostraJanela('Cuidado, atenção!', str)

        else:
            Code = self.limiteCon.inputCode.get()
            listaTurmaPorCodigo = []
            for trm in self.listaTurmas:
                if trm.getDisciplina().getCodigo() == Code:
                    listaTurmaPorCodigo.append(trm)
            if len(listaTurmaPorCodigo) == 0:
                str = (
                    f'Não há algum turma que possui uma disciplina com o código {Code}')
                self.limiteCon.mostraJanela('A Turma não foi encontrada', str)
                self.limiteCon.inputCode.delete(
                    0, len(self.limiteCon.inputCode.get()))
            else:
                str = 'Informações da turma consultada:\n'
                for trm in listaTurmaPorCodigo:
                    str += 'Código: ' + trm.getCodigo() + '\n'
                    str += 'Disciplina: ' + trm.getDisciplina().getCodigo() + ' - ' + \
                        trm.getDisciplina().getNome() + '\n'
                    str += 'Estudantes:\n'
                    for estud in trm.getEstudantes():
                        str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
                    str += '-------------\n'
                self.limiteCon.mostraJanela('Turma existe', str)
                self.limiteCon.inputCode.delete(
                    0, len(self.limiteCon.inputCode.get()))

    def concluiConsultaHandler(self, event):
        self.limiteCon.destroy()

    def concluiInsertionHandler(self, event):
        self.limiteIns.destroy()
