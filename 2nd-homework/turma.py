import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import estudante as est 
import disciplina as disc

#Exceptions de tratamento:
class CampoVazio(Exception):
    pass

class FaltouCodigo(Exception):
    pass

class FaltouAluno(Exception):
    pass

class turmaDuplicada(Exception):
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

        self.labelCodTurma = tk.Label(self.frameCodTurma,text="Informe o código da turma: ")
        self.labelCodTurma.pack(side="left")
        self.inputCodTurma = tk.Entry(self.frameCodTurma, width=20)
        self.inputCodTurma.pack(side="left")

        self.labelDiscip = tk.Label(self.frameDiscip,text="Escolha a disciplina: ")
        self.labelDiscip.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameDiscip, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: \n")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno", font = ('Negrito', 9))           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Turma", font = ('Negrito', 9))           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaTurma)   

        self.buttonConcluido = tk.Button(self.frameButton, text = 'Concluído', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
        self.buttonConcluido.bind("<Button>", controle.concluidoHandler) 

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraTurmas():
    def __init__(self, str):
        messagebox.showinfo('Lista de turmas', str)

class LimiteConsultaTurmas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('280x60')
        self.title("Consultar turmas")
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameCode.pack()
        self.frameButtons.pack()

        self.labelCode = tk.Label(self.frameCode, text = 'Código da disciplina:  ')
        self.labelCode.pack(side = 'left')

        self.inputCode = tk.Entry(self.frameCode, width = 20)
        self.inputCode.pack(side = 'left')

        self.buttonConsulta = tk.Button(self.frameButtons, text = 'Consultar', font = ('Negrito', 9))
        self.buttonConsulta.pack(side = 'left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(self.frameButtons, text = 'Concluído', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
        self.buttonConcluido.bind("<Button>", controle.concluiHandler)

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
        self.limiteIns = LimiteInsereTurma(self, listaCodDisc, self.listaNroMatric)

    def criaTurma(self, event):
        try:
            if len(self.limiteIns.inputCodTurma.get()) == 0 and len(self.limiteIns.escolhaCombo.get()) == 0:
                raise CampoVazio()
            if len(self.limiteIns.inputCodTurma.get()) == 0:
                raise FaltouCodigo()
            if len(self.limiteIns.escolhaCombo.get()) == 0:
                raise FaltouAluno()
        except CampoVazio:
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos!')
        except FaltouCodigo:
            self.limiteIns.mostraJanela('Erro', 'Informe um código!')
        except FaltouAluno:
            self.limiteIns.mostraJanela('Erro', 'Escolha alguma disciplina!')
        
        else:
            codTurma = self.limiteIns.inputCodTurma.get()
            discSel = self.limiteIns.escolhaCombo.get()
            disc = self.ctrlPrincipal.ctrlDisciplina.getDisciplina(discSel)
            turma = Turma(codTurma, disc, self.listaAlunosTurma)
            try:
                for turmas in self.listaTurmas:
                    if turma.getCodigo() == turmas.getCodigo():
                        raise turmaDuplicada()
            except turmaDuplicada:
                str = ("Uma turma com o código '{}'' já foi cadastrada!".format(codTurma))
                self.limiteIns.mostraJanela('Erro', str)
            
            else:
                self.listaTurmas.append(turma)
                self.limiteIns.mostraJanela('Inserção realizada', 'Turma criada com sucesso')
                self.limiteIns.inputCodTurma.delete(0, len(self.limiteIns.inputCodTurma.get()))
            
    def insereAluno(self, event):
        try:
            if len(self.limiteIns.listbox.get(tk.ACTIVE)) == None:
                raise CampoVazio()
        except CampoVazio:
            self.limiteIns.mostraJanela('Falha na matrícula do aluno', 'Nenhum aluno foi selecionado!')

        else:
            alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
            aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
            self.listaAlunosTurma.append(aluno)
            self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
            self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraTurmas(self):
        str = ''
        if len(self.listaTurmas) == 0:
            str += 'Nenhuma turma foi cadastrada ainda!'
            self.limiteLista = LimiteMostraTurmas(str)
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
                raise CampoVazio()
        except CampoVazio:
            str = 'Digite um código de disciplina primeiro!'
            self.limiteCon.mostraJanela('Falha', str)

        else:
            Code = self.limiteCon.inputCode.get()
            listaTurmaPorCodigo = []
            for trm in self.listaTurmas:
                if trm.getDisciplina().getCodigo() == Code:
                    listaTurmaPorCodigo.append(trm)
            if len(listaTurmaPorCodigo) == 0:
                str = ('Nenhuma turma possui uma disciplina com o código {}'.format(Code))
                self.limiteCon.mostraJanela('Turma não encontrada', str)
                self.limiteCon.inputCode.delete(0, len(self.limiteCon.inputCode.get()))
            else:
                str = 'Informações das turmas com a disciplina consultada:\n'
                for trm in listaTurmaPorCodigo:
                    str += 'Código: ' + trm.getCodigo() + '\n'
                    str += 'Disciplina: ' + trm.getDisciplina().getCodigo() +  ' - ' + trm.getDisciplina().getNome() + '\n'
                    str += 'Estudantes:\n'
                    for estud in trm.getEstudantes():
                        str += estud.getNroMatric() + ' - ' + estud.getNome() + '\n'
                    str += '-----------------\n'
                self.limiteCon.mostraJanela('Turma encontrada', str)
                self.limiteCon.inputCode.delete(0, len(self.limiteCon.inputCode.get()))
    
    def concluiHandler(self, event):
        self.limiteCon.destroy()
    
    def concluidoHandler(self, event):
        self.limiteIns.destroy()
    
