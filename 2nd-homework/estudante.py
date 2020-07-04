import tkinter as tk
from tkinter import messagebox

#Exceptions de tratamento:
class CampoVazio(Exception):
    pass

class PreenchaTudo(Exception):
    pass

class MatricRepetida(Exception):
    pass

class alunoJaCadastrado(Exception):
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
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome:              ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Inserir", font = ('Negrito', 9))      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear", font = ('Negrito', 9))      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído", font = ('Negrito', 9))      
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
        self.geometry('280x60')
        self.title("Consultar estudante")
        self.controle = controle

        self.frameMatric = tk.Frame(self)
        self.frameButtons = tk.Frame(self)
        self.frameMatric.pack()
        self.frameButtons.pack()

        self.labelMatric = tk.Label(self.frameMatric, text = 'Matrícula:  ')
        self.labelMatric.pack(side = 'left')

        self.inputMatric = tk.Entry(self.frameMatric, width = 20)
        self.inputMatric.pack(side = 'left')

        self.buttonConsulta = tk.Button(self.frameButtons, text = 'Consultar', font = ('Negrito', 9))
        self.buttonConsulta.pack(side = 'left')
        self.buttonConsulta.bind("<Button>", controle.consultaHandler)

        self.buttonConcluido = tk.Button(self.frameButtons, text = 'Concluído', font = ('Negrito', 9))
        self.buttonConcluido.pack(side = 'left')
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
            str = "Não há alunos cadastrados"
            self.limiteLista = LimiteMostraEstudantes(str)
        else:
            str = "Nro Matric. -- Nome\n"
            for est in self.listaEstudantes:
                str += est.getNroMatric() + ' -- ' + est.getNome() + '\n'
            self.limiteLista = LimiteMostraEstudantes(str)
    
    def consultaEstudantes(self):
        self.limiteCon = LimiteConsultaEstudantes(self)

    def insereHandler(self, event):
        try:
            if len(self.limiteIns.inputNro.get()) == 0 or len(self.limiteIns.inputNome.get()) == 0:
                raise PreenchaTudo()
            for estud in self.listaEstudantes:
                if estud.getNroMatric() == self.limiteIns.inputNro.get() and estud.getNome() == self.limiteIns.inputNome.get():
                    raise alunoJaCadastrado()
                if estud.getNroMatric() == self.limiteIns.inputNro.get():
                    raise MatricRepetida()
        except alunoJaCadastrado:
            self.limiteIns.mostraJanela('Cadastro não permitido', 'Este aluno já foi cadastrado!')
        except PreenchaTudo:
            self.limiteIns.mostraJanela('Cadastro não permitido', 'Preencha todos os campos!')
        except MatricRepetida:
            self.limiteIns.mostraJanela('Cadastro não permitido', 'Este número de matrícula já está em uso por outro aluno!')

        else:
            nroMatric = self.limiteIns.inputNro.get()
            nome = self.limiteIns.inputNome.get()
            estudante = Estudante(nroMatric, nome)
            self.listaEstudantes.append(estudante)
            self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    
    def consultaHandler(self, event):
        try:
            if len(self.limiteCon.inputMatric.get()) == 0:
                raise CampoVazio()
        except CampoVazio:
            str = 'Digite um número de matrícula primeiro!'
            self.limiteCon.mostraJanela('Falha', str)
            
        else:
            Matric = self.limiteCon.inputMatric.get()
            est = self.getEstudante(Matric)
            if est == None:
                str = ('Nenhum aluno possui a matrícula {}'.format(Matric))
                self.limiteCon.mostraJanela('Aluno não encontrado', str)
                self.limiteCon.inputMatric.delete(0, len(self.limiteCon.inputMatric.get()))
            else:
                str = 'Informações do aluno consultado:\n'
                str += 'Nro Matric. -- Nome\n'
                str += est.getNroMatric() + ' -- ' + est.getNome()
                self.limiteCon.mostraJanela('Aluno encontrado', str)
                self.limiteCon.inputMatric.delete(0, len(self.limiteCon.inputMatric.get()))

    def concluiHandler(self, event):
        self.limiteCon.destroy()