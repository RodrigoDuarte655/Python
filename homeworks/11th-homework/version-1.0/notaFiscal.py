# Importando bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os.path
# importando disciplina
import produto as pro


# ----Possíveis erros que vão ser tratados----
# Caso o ano seja inválido
# class InvalidYear(Exception):
#     pass


# # Caso a disciplina já exista
# class DisciplinaAlreadyExists(Exception):
#     pass


# # Caso o código da grade seja inválido
# class InvalidCode(Exception):
#     pass


# # Caso tenha alguma informação repetida
# class informationAlreadyExists(Exception):
#     pass


# # Caso tenha algum campo de preenchimento em branco 
# class EmptyField(Exception):
#     pass


# Classe do grade
class NotaFiscal:
    # Método construtor da grade
    def __init__(self, numeroNF, nomeCliente):
        self.__numeroNF = numeroNF
        self.__nomeCliente = nomeCliente

         # Lista com os produtos da nota fiscal
        self.__itensNota = []

    # ----Métodos Getters----
    def getItensNota(self):
        return self.__itensNota

    def getNumeroNf(self):
        return self.__numeroNF

    def getNomeCliente(self):
        return self.__nomeCliente

    # Método para adicionar disciplina
    def addNotaFiscal(self, notaFiscal):
        self.__itensNota.append(notaFiscal)


# Limite da tela de inserção da grade
class CriaNotaFiscalView(tk.Toplevel):
    # Método construtor
    def __init__(self, control, produtosList):
        tk.Toplevel.__init__(self)
        # Tamanho da janela
        self.geometry("350x400")
        # Cria o título
        self.title('Crie a nota fiscal')
        # Controle
        self.control = control

        # Criar as partes necessárias de pegar o número da nota fiscal
        self.frameNumeroNF = tk.Frame(self)
        self.frameNumeroNF.pack()
        self.labelNumeroNF = tk.Label(
            self.frameNumeroNF, text='Número NF:')
        self.labelNumeroNF.pack(side='left')
        self.inputNumeroNF = tk.Entry(self.frameNumeroNF, width=20)
        self.inputNumeroNF.pack(side='left')

        # Criar as partes necessárias de pegar o nome do cliente
        self.frameNomeCliente = tk.Frame(self)
        self.frameNomeCliente.pack()
        self.labelNomeCliente = tk.Label(
            self.frameNomeCliente, text='Nome cliente:')
        self.labelNomeCliente.pack(side='left')
        self.inputNomeCliente = tk.Entry(self.frameNomeCliente, width=20)
        self.inputNomeCliente.pack(side='left')

        # Criar as partes necessárias dos produtos da nota fiscal
        self.frameProdutosNotaFiscal = tk.Frame(self)
        self.frameProdutosNotaFiscal.pack()
        self.labelProdutosNotaFiscal = tk.Label(
            self.frameProdutosNotaFiscal, text='\n\nProdutos:')
        self.labelProdutosNotaFiscal.pack()
        self.chooseComboProduto = tk.StringVar()
        self.comboboxProduto = ttk.Combobox(
            self.frameProdutosNotaFiscal, width=20, textvariable=self.chooseComboProduto)
        self.comboboxProduto.pack(side='top')

        # cria uma lista para os código do produto
        codigosProdutos = []
        for code in produtosList:
            codigosProdutos.append(code.getCodigoProduto())

        # Adiciona os valores da lista no combobox
        self.comboboxProduto['values'] = codigosProdutos

        # Criar o frame dos botões
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        # --- Botões---
        # Botão para inserir produto
        self.buttonInsere = tk.Button(
            self.frameProdutosNotaFiscal, text='Inserir produto')
        self.buttonInsere.pack(side='top')
        self.buttonInsere.bind("<Button>", control.insereProduto)

        # Botão para criar a nota fiscal
        self.buttonCria = tk.Button(
            self.frameButton, text='Criar nota fiscal', font=('Negrito', 11))
        self.buttonCria.pack(side='left')
        self.buttonCria.bind("<Button>", control.createNotaFiscal)

        # Botão para limpar os campos já preenchidos pelo usuário
        self.buttonClear = tk.Button(
            self.frameButton, text='Clear', font=('Negrito', 11))
        self.buttonClear.pack(side='left')
        self.buttonClear.bind("<Button>", control.clearHandler)

        # Botão para sair após criar a grade
        self.buttonConcluido = tk.Button(
            self.frameButton, text='Concluído', font=('Negrito', 11))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", control.concluiHandler)

    # Método para mostrar mensagens de aviso para o usuário
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


# Limite para mostrar as informações que já foram cadastradas
class MostraNotaFiscalView():
    def __init__(self, str):
        messagebox.showinfo('Lista de notas fiscais cadastradas!', str)

class ConsultaNotaFiscalView(tk.Toplevel):

    def __init__(self, control):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar nota fiscal")
        self.control = control

        self.frameNroNotaFiscal = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNroNotaFiscal.pack()
        self.frameButton.pack()

        self.labelNroNotaFiscal = tk.Label(self.frameNroNotaFiscal, text='Número da nota fiscal:  ')
        self.labelNroNotaFiscal.pack(side='left')

        self.inputNroNotaFiscal = tk.Entry(self.frameNroNotaFiscal, width=20)
        self.inputNroNotaFiscal.pack(side='left')

        self.buttonConsulta = tk.Button(
            self.frameButton, text='Consultar', font=('Negrito', 9))
        self.buttonConsulta.pack(side='left')
        self.buttonConsulta.bind("<Button>", control.consultaHandler)

        self.buttonConcluido = tk.Button(
            self.frameButton, text='Concluído', font=('Negrito', 9))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", control.concluidoHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

# Classe controladora da grade
class CtrlNotaFiscal():
    # Método construtor
    def __init__(self, mainControl):
        # Passando como parâmetro controlador principal
        self.ctrlMain = mainControl

        # ---Ler as informações dos arquivos que foram salvos ---
        if not os.path.isfile("notaFiscal.pickle"):
            self.notasFiscaisList = []
        else:
            with open("notaFiscal.pickle", "rb") as f:
                self.notasFiscaisList = pickle.load(f)

        # Lista com produtos
        self.produtoNotaFiscalList = []

    # Método para inserir a grade
    def criaNotaFiscal(self):
        # Lista com apenas a lista de disciplinas
        produtosList = self.ctrlMain.ctrlProduto.getProdutosList()
        # Chama o limite da inserção da grade, passando como parâmetro a lista de disciplinas
        self.limiteIns = CriaNotaFiscalView(self, produtosList)

    # Método para inserirs as disciplinas na grade
    def insereProduto(self, event):
        # try:
        #     # Verificando se tem algum campo de preenchimento vazio
        #     if len(self.limiteIns.inputNomeCliente.get()) == 0 or len(self.limiteIns.chooseCombo.get()) == 0 or len(self.limiteIns.inputNumeroNF.get()) == 0:
        #         raise EmptyField()

        #     # Verifica se o código da grade é inválido
        #     if len(self.limiteIns.inputNumeroNF.get()) != 2 or not self.limiteIns.inputNumeroNF.get().isdigit():
        #         raise InvalidCode()

        #     # Verificando se tem o ano está inválido. Precisa estar entre 2012 e 2021
        #     if int(self.limiteIns.inputNomeCliente.get()) > 2021 or int(self.limiteIns.inputNomeCliente.get()) < 2012 or not self.limiteIns.inputNomeCliente.get().isdigit():
        #         raise InvalidYear()

        # # Mostra mensagem avisando o usuário sobre o erro
        # except EmptyField:
        #     self.limiteIns.mostraJanela(
        #         'Cuidado, atenção!', 'Por favor, preencha todos os campos!')

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidCode:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "O código está inválido! Exemplos válidos: 01, 02, 03, etc")

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidYear:
        #     self.limiteIns.mostraJanela(
        #         'Cuidado, atenção!', 'O ano é inválido! Precisa estar entre 2012 a 2021!')
        # else:

            currentProduct = self.limiteIns.comboboxProduto.get()

            objectProduto = self.ctrlMain.ctrlProduto.getProdutoObject(
                currentProduct)

            # try:
            #     # Verifica se a disciplina já existe
            #     for disciplina in self.produtoNotaFiscalList:
            #         if objectProduto.getCodigoDisciplina() == disciplina.getCodigoDisciplina():
            #             raise DisciplinaAlreadyExists()

            # # Mostra mensagem avisando o usuário sobre o erro
            # except DisciplinaAlreadyExists:
            #     self.limiteIns.mostraJanela(
            #         "Cuidado, atenção!", "Disciplina já foi inserida nessa grade")

            # else:

                # Adiciona-se o objeto dessa disciplina na lista de disciplinas
            self.produtoNotaFiscalList.append(objectProduto)
            self.limiteIns.mostraJanela(
                'Parabéns, produto adicionado!', 'O produto foi adicionada com sucesso!')

    # Método para criar a grade
    def createNotaFiscal(self, event):
        # try:
        #     # Verificando se tem algum campo de preenchimento vazio
        #     if len(self.limiteIns.inputNomeCliente.get()) == 0 or len(self.limiteIns.chooseCombo.get()) == 0 or len(self.limiteIns.inputNumeroNF.get()) == 0:
        #         raise EmptyField()

        #     # Verifica se o código da grade é inválido
        #     if len(self.limiteIns.inputNumeroNF.get()) != 2 or not self.limiteIns.inputNumeroNF.get().isdigit():
        #         raise InvalidCode()

        #     # Verificando se tem o ano está inválido. Precisa estar entre 2012 e 2021
        #     if int(self.limiteIns.inputNomeCliente.get()) > 2021 or int(self.limiteIns.inputNomeCliente.get()) < 2012 or not self.limiteIns.inputNomeCliente.get().isdigit():
        #         raise InvalidYear()

        # # Mostra mensagem avisando o usuário sobre o erro
        # except EmptyField:
        #     self.limiteIns.mostraJanela(
        #         'Cuidado, atenção!', 'Por favor, preencha todos os campos!')

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidCode:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "O código está inválido! Exemplos válidos: 01, 02, 03, etc")

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidYear:
        #     self.limiteIns.mostraJanela(
        #         'Cuidado, atenção!', 'O ano é inválido! Precisa estar entre 2012 a 2021!')

        # else:
            # ---Caso não tenha erros cadastra o curso---
            numeroNF = self.limiteIns.inputNumeroNF.get()
            nomeClient = self.limiteIns.inputNomeCliente.get()
            
            # Instancia a grade
            notaFiscal = NotaFiscal(numeroNF, nomeClient)

            # Adiciona as disciplina na grade
            for notfis in self.produtoNotaFiscalList:
                notaFiscal.addNotaFiscal(notfis)

            # try:
            #     # Verificando se já o existe o código da grade
            #     for gra in self.gradesList:
            #         if gra.getCodigoGrade() == grade.getCodigoGrade():
            #             raise informationAlreadyExists()

            # # Mostra mensagem avisando o usuário sobre o erro
            # except informationAlreadyExists:
            #     self.limiteIns.mostraJanela(
            #         'Cuidado, atenção!', 'O código dessa grade já existe!')

            # else:
                # Adiciona a grade instanciada na lista de grades
            self.notasFiscaisList.append(notaFiscal)
            self.limiteIns.mostraJanela(
                'Parabéns, sucesso!', 'A nota fiscal foi criada com sucesso!')

    def getNotaFiscalObject(self, numberNF):
        NotaFiscalObject = None
        for nf in self.notasFiscaisList:
            if nf.getNumeroNf() == numberNF:
                NotaFiscalObject = nf
        return NotaFiscalObject

    def consultaHandler(self, event):
        # try:
        #     if len(self.limiteCon.inputNro.get()) == 0:
        #         raise EmptyField()
        # except EmptyField:
        #     str = 'Campo de matrícula vazio! Por favor, digite um número de matrícula!'
        #     self.limiteCon.mostraJanela('Erro', str)

        # else:
            numberNF = self.limiteCon.inputNroNotaFiscal.get()
            notaFiscalObj = self.getNotaFiscalObject(numberNF)
            
            if notaFiscalObj == None:
                str = (f'Não existe nota fiscal com o número {numberNF}')
                self.limiteCon.mostraJanela('Nota fiscal não encontrada', str)
                self.limiteCon.inputNroNotaFiscal.delete(
                    0, len(self.limiteCon.inputNroNotaFiscal.get()))
            else:
                str = 'Informações da nota fiscal consultada:\n'
                str += f'Nome {notaFiscalObj.getNomeCliente()}\n'

                str += '\n------------------------------------\n'

                str += f'Produtos da nota fiscal {notaFiscalObj.getNumeroNf()}:\n'
                for prod in notaFiscalObj.getItensNota():
                    str += "Código -- Descrição -- Valor unitário\n"
                    str += f'{prod.getCodigoProduto()} -- {prod.getDescricaoProduto()} -- {prod.getValorUnitarioProduto()}'
                    str += '\n------------------------------------\n'
                self.limiteCon.mostraJanela('Nota fiscal encontrada', str)
                self.limiteCon.inputNroNotaFiscal.delete(
                    0, len(self.limiteCon.inputNroNotaFiscal.get()))

                # str += 'Código -- Descrição -- Valor unitário\n'
                # str += f'{notaFiscalObj.getCodigoProduto()} -- {notaFiscalObj.getDescricaoProduto()} -- {notaFiscalObj.getValorUnitarioProduto()}'
                # self.limiteCon.mostraJanela('Nota fiscal encontrada', str)
                # self.limiteCon.inputNroNotaFiscal.delete(
                #     0, len(self.limiteCon.inputNroNotaFiscal.get()))

    def consultaNotasFiscais(self):
        self.limiteCon = ConsultaNotaFiscalView(self)

    # Método para mostrar as grades
    def mostrarNotasFiscais(self):
        str = ''
        if len(self.notasFiscaisList) != 0:

            for notfis in self.notasFiscaisList:

                str += '----------Nota fiscal----------\n'
                str += 'NúmeroNF -- Nome cliente\n'
                str += f'{notfis.getNumeroNf()} -- {notfis.getNomeCliente()}'
                str += '\n------------------------------------\n'

                str += f'Produtos da nota fiscal {notfis.getNumeroNf()}:\n'
                for prod in notfis.getItensNota():
                    str += "Código -- Descrição -- Valor unitário\n"
                    str += f'{prod.getCodigoProduto()} -- {prod.getDescricaoProduto()} -- {prod.getValorUnitarioProduto()}'
                    str += '\n------------------------------------\n'

        else:
            str += 'Não existem notas fiscais criadas!'
        self.limiteMost = MostraNotaFiscalView(str)

    # Método getter para pegar a lista de grades
    # # def getGradesList(self):
    # #     return self.gradesList

    # # # Método getter para pegar o objeto grade
    # # def getGradeObj(self, codigoGrade):
    # #     # Declara um objeto vazio
    # #     objGrade = None
    # #     # Se o código da grade passado como parâmetro é igual então ele retorna o objeto grade inteiro
    # #     for gra in self.gradesList:
    # #         if codigoGrade == gra.getCodigoGrade():
    # #             objGrade = gra
    # #     return objGrade

    # def getGradeObjByCurso(self, cursoAluno):
    #     temp = self.ctrlMain.ctrlCurso.getCursosList()

    #     # Declara um objeto vazio
    #     objGrade = None
    #     # Se a curso passado como parâmetro é igual então ele retorna o objeto grade inteiro para passar para o aluno
    #     for curso in temp:
    #         if cursoAluno.getCodigoCurso() == curso.getCodigoCurso():
    #             objGrade = cursoAluno.getGrade()
    #     return objGrade

    # Método para limpar os campos de preenchimento que foram preenchidos
    def clearHandler(self, event):
        self.limiteIns.inputNumeroNF.delete(
            0, len(self.limiteIns.inputNumeroNF.get()))

        self.limiteIns.inputNomeCliente.delete(
            0, len(self.limiteIns.inputNomeCliente.get()))

    # Método para destruir a tela e sair
    def concluiHandler(self, event):
        self.limiteIns.destroy()

    def concluidoHandler(self, event):
        self.limiteCon.destroy()

    # Método para salvar todas as informações que foram registradas
    def saveNotasFiscais(self):
        if len(self.notasFiscaisList) != 0:
            with open("notaFiscal.pickle", "wb") as f:
                pickle.dump(self.notasFiscaisList, f)