import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import disciplina as disc
import os.path
import pickle

#Exceptions de tratamento
class PreenchaTudo(Exception):
    pass

class FaltouAno(Exception):
    pass

class FaltouCode(Exception):
    pass

class FaltouSemestre(Exception):
    pass

class CodeInvalido(Exception):
    pass

class GradeDuplicada(Exception):
    pass

class AnoInvalido(Exception):
    pass

class GradeNaoExiste(Exception):
    pass

class VeioDoPassado(Exception):
    pass

class Grade: 
    #Construtor
    def __init__(self, codigo, ano, semestre):
        self.__codigo = codigo
        self.__ano = ano
        self.__semestre = semestre
    
        #A grade é composta por uma lista de disciplinas
        #Isto se torna uma agregação
        self.__disciplinas = []

    def getCodigo(self):
        return self.__codigo

    def getAno(self):
        return self.__ano
    
    def getSemestre(self):
        return self.__semestre

    def getDisciplina(self):
        return self.__disciplinas
    
    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

class LimiteInsereGrade(tk.Toplevel):
    def __init__(self, controle, listaDiscps):

        tk.Toplevel.__init__(self)
        self.geometry("250x300")
        self.title('Inserir Grade')
        self.controle = controle

        self.frameCode = tk.Frame(self)
        self.frameCode.pack()
        self.frameAno = tk.Frame(self)
        self.frameAno.pack()
        self.frameSemest = tk.Frame(self)
        self.frameSemest.pack()
        self.frameDisc = tk.Frame(self)
        self.frameDisc.pack()
        self.frameButtons = tk.Frame(self)
        self.frameButtons.pack()

        self.labelCode = tk.Label(self.frameCode, text = 'Informe o código:    ')
        self.labelCode.pack(side = 'left')
        self.inputCode = tk.Entry(self.frameCode, width = 20)
        self.inputCode.pack(side = 'left')

        self.labelAno = tk.Label(self.frameAno, text = 'Informe o ano:          ')
        self.labelAno.pack(side = 'left')
        self.inputAno = tk.Entry(self.frameAno, width = 20)
        self.inputAno.pack(side = 'left')

        self.labelSemest = tk.Label(self.frameSemest, text = 'Informe o semestre: ')
        self.labelSemest.pack(side = 'left')
        self.escolhaCombo = tk.StringVar()
        self.comboboxSemest = ttk.Combobox(self.frameSemest, width = 10, textvariable = self.escolhaCombo)
        self.comboboxSemest.pack(side = 'left')
        self.listaSemest = ['1', '2']
        self.comboboxSemest['values'] = self.listaSemest

        self.labelDisc = tk.Label(self.frameDisc, text = 'Escolha as disciplinas que vão a compor: ')
        self.labelDisc.pack()
        self.listboxDisc = tk.Listbox(self.frameDisc)
        self.listboxDisc.pack(side = 'left')
        for disc in listaDiscps:
            self.listboxDisc.insert(tk.END, disc.getCodigo())

        self.buttonInsere = tk.Button(self.frameDisc, text = 'Inserir disciplina')
        self.buttonInsere.pack(side = 'left')
        self.buttonInsere.bind("<Button>", controle.insereDisciplina)

        self.buttonCria = tk.Button(self.frameButtons, text = 'Criar grade', font = ('Negrito', 9))
        self.buttonCria.pack(side = 'left')
        self.buttonCria.bind("<Button>", controle.criaGrade)

        self.buttonSair = tk.Button(self.frameButtons, text = 'Sair', font = ('Negrito, 9'))
        self.buttonSair.pack(side = 'left')
        self.buttonSair.bind("<Button>", controle.exitHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteMostraGrades(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('500x100')
        self.title('Buscar Grade por Curso')
        self.controle = controle

        self.frameBusca = tk.Frame(self)
        self.frameBusca.pack()
        self.labelBusca = tk.Label(self.frameBusca, text = 'Informe o código ou o nome do curso: ')
        self.labelBusca.pack(side = 'left')
        self.inputNomeOuCode = tk.Entry(self.frameBusca, width = 20)
        self.inputNomeOuCode.pack(side = 'left')

        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.buttonBuscar = tk.Button(self.frameButton, text = 'Buscar', font = ('Negrito', 9))
        self.buttonBuscar.pack(side = 'left')
        self.buttonBuscar.bind("<Button>", controle.BuscarGradeHandler)

        self.buttonSai = tk.Button(self.frameButton, text = 'Sair', font = ('Negrito', 9))
        self.buttonSai.pack(side = 'left')
        self.buttonSai.bind("<Button>", controle.SaiHandler)

class CtrlGrade():
    def __init__(self, controlePrincipal):
        self.CtrlPrincipal = controlePrincipal
        self.listaDiscipGrade = []

        if not os.path.isfile("grades.pickle"):
            self.listaGrades = []
        else:
            with open("grades.pickle", "rb") as f:
                self.listaGrades = pickle.load(f)
        
    def salvaGrades(self):
        if len(self.listaGrades) != 0:
            with open("grades.pickle", "wb") as f:
                pickle.dump(self.listaGrades, f)
    
    def getGradePorCode(self, code):
        gradeRet = None
        for grade in self.listaGrades:
            if code == grade.getCodigo():
                gradeRet = grade
        return gradeRet
    
    def getGradePorCurso(self, NomeOuCode):
        gradeRet = None
        Code = NomeOuCode
        curso = self.CtrlPrincipal.ctrlCurso.getCursoPorCode(Code)
        if curso == None:
            str = ("Nenhum curso possui o código ou nome igual a '{}'".format(Code))
            messagebox.showinfo('Curso não encontrado', str)
            self.limiteMost.inputNomeOuCode.delete(0, len(self.limiteMost.inputNomeOuCode.get()))
        else:
            grade = curso.getGrade()
            gradeRet = grade        
        return gradeRet

    def getDiscGrade(self, gradeRef):
        grade = gradeRef
        listaDiscGrade = []
        for grad in self.listaGrades:
            if grade == grad.getCodigo():
                listaDiscGrade = grad.getDisciplina()
        return listaDiscGrade
    
    def getListaGrades(self):
        return self.listaGrades

    def getListaCodGrades(self):
        listaCodGrades = []
        for grade in self.listaGrades:
            listaCodGrades.append(grade.getCodigo())
        return listaCodGrades
    
    def insereGrade(self):
        listaDiscips = self.CtrlPrincipal.ctrlDisciplina.getListaDisciplinas()
        self.limiteIns = LimiteInsereGrade(self, listaDiscips)
    
    def isNumber(self, number):
        try:
            if number.isdigit() == True:
                return True
            float(number)
            return True
        except ValueError:
            return False
    
    def criaGrade(self, event):
        try:
            if len(self.limiteIns.inputCode.get()) == 0 and len(self.limiteIns.inputAno.get()) == 0 and len(self.limiteIns.escolhaCombo.get()) == 0:
                raise PreenchaTudo()
            if len(self.limiteIns.inputCode.get()) == 0:
                raise FaltouCode()
            if len(self.limiteIns.inputAno.get()) == 0:
                raise FaltouAno()
            if len(self.limiteIns.inputAno.get()) != 4 or self.isNumber(self.limiteIns.inputAno.get()) == False:
                raise AnoInvalido()
            if float(self.limiteIns.inputAno.get()) < 1990:
                raise VeioDoPassado()
            if len(self.limiteIns.escolhaCombo.get()) == 0:
                raise FaltouSemestre()
            if len(self.limiteIns.inputCode.get()) > 5 or len(self.limiteIns.inputCode.get().split(' ')) >= 2:
                raise CodeInvalido()
        except PreenchaTudo:
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos!')
        except FaltouCode:
            self.limiteIns.mostraJanela('Erro', 'Informe um código!')
        except FaltouAno:
            self.limiteIns.mostraJanela('Erro', 'Informe um ano!')
        except AnoInvalido:
            self.limiteIns.mostraJanela('Erro', 'Ano inválido!')
            self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        except VeioDoPassado:
            self.limiteIns.mostraJanela('Erro', 'Por que cadastrar uma grade do passado?')
            self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        except FaltouSemestre:
            self.limiteIns.mostraJanela('Erro', 'Informe um semestre!')
        except CodeInvalido:
            self.limiteIns.mostraJanela('Erro', """Seu código deve conter no máximo 5 caracteres e não pode conter espaços!
        Exemplos: 'SIN', 'CC01', '12345', 'ECO15' ...""")
            self.limiteIns.inputCode.delete(0, len(self.limiteIns.inputCode.get()))
        
        else:
            code = self.limiteIns.inputCode.get()
            ano = self.limiteIns.inputAno.get()
            semest = self.limiteIns.escolhaCombo.get()
            grade = Grade(code, ano, semest)
            for dis in self.listaDiscipGrade:
                grade.addDisciplina(dis)              
            try:
                for grad in self.listaGrades:
                        if grade.getCodigo() == grad.getCodigo() and grade.getAno() == grad.getAno() and grade.getSemestre() == grad.getSemestre():
                            raise GradeDuplicada()
            except GradeDuplicada:
                self.limiteIns.mostraJanela('Inserção não permitida', 'Esta grade já foi cadastrada!')

            else:        
                self.listaGrades.append(grade)
                self.limiteIns.mostraJanela('Inserção realizada', 'Grade cadastrada com sucesso!')
                self.limiteIns.destroy()
    
    def insereDisciplina(self, event):
        try:
            if len(self.limiteIns.inputCode.get()) == 0 and len(self.limiteIns.inputAno.get()) == 0 and len(self.limiteIns.escolhaCombo.get()) == 0:
                raise PreenchaTudo()
            if len(self.limiteIns.inputCode.get()) == 0:
                raise FaltouCode()
            if len(self.limiteIns.inputAno.get()) == 0:
                raise FaltouAno()
            if len(self.limiteIns.inputAno.get()) != 4 or self.isNumber(self.limiteIns.inputAno.get()) == False:
                raise AnoInvalido()
            if float(self.limiteIns.inputAno.get()) < 1990:
                raise VeioDoPassado()
            if len(self.limiteIns.escolhaCombo.get()) == 0:
                raise FaltouSemestre()
            if len(self.limiteIns.inputCode.get()) > 5 or len(self.limiteIns.inputCode.get().split(' ')) >= 2:
                raise CodeInvalido()
        except PreenchaTudo:
            self.limiteIns.mostraJanela('Erro', 'Preencha todos os campos!')
        except FaltouCode:
            self.limiteIns.mostraJanela('Erro', 'Informe um código!')
        except FaltouAno:
            self.limiteIns.mostraJanela('Erro', 'Informe um ano!')
        except AnoInvalido:
            self.limiteIns.mostraJanela('Erro', 'Ano inválido!')
            self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        except VeioDoPassado:
            self.limiteIns.mostraJanela('Erro', 'Por que cadastrar uma grade do passado?')
            self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))
        except FaltouSemestre:
            self.limiteIns.mostraJanela('Erro', 'Informe um semestre!')
        except CodeInvalido:
            self.limiteIns.mostraJanela('Erro', """Seu código deve conter no máximo 5 caracteres e não pode conter espaços!
        Exemplos: 'SIN', 'CC01', '12345', 'ECO15' ...""")
            self.limiteIns.inputCode.delete(0, len(self.limiteIns.inputCode.get()))
        
        else:
            discipSel = self.limiteIns.listboxDisc.get(tk.ACTIVE)
            disciplina = self.CtrlPrincipal.ctrlDisciplina.getDisciplina(discipSel)
            self.listaDiscipGrade.append(disciplina)
            self.limiteIns.mostraJanela('Sucesso', 'Disciplina adicionada')
            self.limiteIns.listboxDisc.delete(tk.ACTIVE)
    
    def mostraGrades(self):
        str = ''
        if len(self.listaGrades) == 0:
            str += 'Não há grades cadastradas'
        else:
            self.limiteMost = LimiteMostraGrades(self)
    
    def BuscarGradeHandler(self, event):
        try:
            if len(self.limiteMost.inputNomeOuCode.get()) == 0:
                raise PreenchaTudo()
        except PreenchaTudo:
            messagebox.showinfo('Erro', 'Digite o código ou o nome de um curso!')

        else:  
            grade = self.getGradePorCurso(self.limiteMost.inputNomeOuCode.get())      
            str = '------------------------------------------------------------\n'
            str += 'Código: ' + grade.getCodigo() + '   Ano/Semestre: ' + grade.getAno() + '.' + grade.getSemestre() + '\n'
            str += '\nLista de disciplinas:\n'
            for disc in grade.getDisciplina():
                str += '\n' + disc.getCodigo() + ' - ' + disc.getNome() + '\n'
                str += 'Carga horária: ' + disc.getCargaHoraria() + '\n'
            str += '------------------------------------------------------------\n'
            messagebox.showinfo('Grade encontrada', str)
            self.limiteMost.destroy()

    def exitHandler(self, event):
        self.limiteIns.destroy()
    
    def SaiHandler(self, event):
        self.limiteMost.destroy()
            