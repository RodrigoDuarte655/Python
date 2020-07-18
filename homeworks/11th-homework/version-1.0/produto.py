# Importando bibliotecas
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os.path
# importando nota fiscal
import notaFiscal as notfis


# # ----Possíveis erros que vão ser tratados----

# # Caso o nome seja inválido
# class InvalidName(Exception):
#     pass


# # Caso a matrícula seja inválida
# class InvalidMatricula(Exception):
#     pass


# # Caso tenha alguma informação repetida
# class InformationAlreadyExists(Exception):
#     pass


# # Caso tenha algum campo de preenchimento em branco
# class EmptyField(Exception):
#     pass


# Classe do aluno
class Produto:
    # Método construtor do aluno
    def __init__(self, codigo, descricao, valorUnitario):
        self.__codigo = codigo
        self.__descricao = valorUnitario
        self.__valorUnitario = valorUnitario

    # ----Métodos Getters----
    def getCodigoProduto(self):
        return self.__codigo

    def getDescricaoProduto(self):
        return self.__descricao

    def getValorUnitarioProduto(self):
        return self.__valorUnitario


# Limite da tela de inserção do aluno
class cadastraProdutoView(tk.Toplevel):
    # Método construtor
    def __init__(self, control, produtosList):
        tk.Toplevel.__init__(self)
        # Tamanho da janela
        self.geometry('350x300')
        # Cria o título
        self.title("Cadastre o produto")
        # Controle
        self.control = control

        # Criar as partes necessárias de pegar o código do produto
        self.frameCodigoProduto = tk.Frame(self)
        self.frameCodigoProduto.pack()
        self.labelCodigoProduto = tk.Label(self.frameCodigoProduto, text=' Código:')
        self.labelCodigoProduto.pack(side='left')
        self.inputCodigoProduto = tk.Entry(self.frameCodigoProduto, width=20)
        self.inputCodigoProduto.pack(side='left')

        # Criar as partes necessárias de pegar a descrição do produto
        self.frameDescricaoProduto = tk.Frame(self)
        self.frameDescricaoProduto.pack()
        self.labelDescricaoProduto = tk.Label(self.frameDescricaoProduto, text='Descrição:')
        self.labelDescricaoProduto.pack(side='left')
        self.inputDescricaoProduto = tk.Entry(self.frameDescricaoProduto, width=20)
        self.inputDescricaoProduto.pack(side='left')

        # Criar as partes necessárias de pegar o valor unitário do produto
        self.frameValorUnitario = tk.Frame(self)
        self.frameValorUnitario.pack()
        self.labelValorUnitario = tk.Label(self.frameValorUnitario, text='Valor unitário:')
        self.labelValorUnitario.pack(side='left')
        self.inputValorUnitario = tk.Entry(self.frameValorUnitario, width=20)
        self.inputValorUnitario.pack(side='left')

        # Criar o frame dos botões
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        # --- Botões---
        # Botão para cadastrar o produto
        self.buttonCadastrar = tk.Button(
            self.frameButton, text='Cadastrar', font=('Negrito', 11))
        self.buttonCadastrar.pack(side='left')
        self.buttonCadastrar.bind("<Button>", control.cadastraHandler)

        # Botão para limpar os campos já preenchidos pelo usuário
        self.buttonClear = tk.Button(
            self.frameButton, text='Clear', font=('Negrito', 11))
        self.buttonClear.pack(side='left')
        self.buttonClear.bind("<Button>", control.clearHandler)

        # Botão para sair após cadastrar o produto
        self.buttonConcluido = tk.Button(
            self.frameButton, text='Concuído', font=('Negrito', 11))
        self.buttonConcluido.pack(side='left')
        self.buttonConcluido.bind("<Button>", control.concluidoHandler)

    # Método para mostrar mensagens de aviso para o usuário
    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)


# Limite para mostrar as informações que já foram cadastradas
class MostraProdutoView():
    def __init__(self, str):
        messagebox.showinfo('Lista de produtos cadastrados', str)

class ConsultaProdutosView(tk.Toplevel):

    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar produto")
        self.controle = controle

        self.frameCodeProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodeProduto.pack()
        self.frameButton.pack()

        self.labelCodeProduto = tk.Label(self.frameCodeProduto, text='Código do produto:  ')
        self.labelCodeProduto.pack(side='left')

        self.inputCodeProduto = tk.Entry(self.frameCodeProduto, width=20)
        self.inputCodeProduto.pack(side='left')

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

# Classe controladora do aluno
class CtrlProduto():
    # Método construtor
    def __init__(self, mainControl):
        # Passando como parâmetro controlador principal
        self.ctrlMain = mainControl

        # ---Ler as informações dos arquivos que foram salvos ---
        if not os.path.isfile("produto.pickle"):
            self.produtosList = []
        else:
            with open("produto.pickle", "rb") as f:
                self.produtosList = pickle.load(f)

    # Método para cadastrar o produto
    def cadastraProduto(self):
        # Lista com apenas a lista de cursos do aluno
        produtosList = self.ctrlMain.ctrlProduto.getProdutosList()
        # Chama o limite da inserção do aluno, passando como parâmetro a lista de cursos

        self.limiteIns = cadastraProdutoView(self, produtosList)

    # Método getter para pegar a lista de produtos
    def getProdutosList(self):
        return self.produtosList

    # Método handler para inserir, ele irá lidar com possíveis erros e cadastrar os alunos
    def cadastraHandler(self, event):
        # try:

        #     # Veirificando se tem algum campo de preenchimento vazio
        #     if len(self.limiteIns.inputCodigoProduto.get()) == 0 or len(self.limiteIns.inputDescricaoProduto.get()) == 0 or len(self.limiteIns.inputCursoAluno.get()) == 0:
        #         raise EmptyField()

        #     # Verificando se já o existe o nome ou a matrícula
        #     for aluno in self.alunosList:
        #         if self.limiteIns.inputDescricaoProduto.get() == aluno.getNomeAluno() or self.limiteIns.inputCodigoProduto.get() == aluno.getNroMatric():
        #             raise InformationAlreadyExists()

        #     # Verifica se o nome está inválido
        #     if len(self.limiteIns.inputDescricaoProduto.get()) < 3 or len(self.limiteIns.inputDescricaoProduto.get()) > 30 or not self.limiteIns.inputDescricaoProduto.get().replace(" ", "").isalpha():
        #         raise InvalidName()

        #     # Verifica se a matrícula está inválida
        #     if len(self.limiteIns.inputCodigoProduto.get()) < 4 or len(self.limiteIns.inputCodigoProduto.get()) > 5 or not self.limiteIns.inputCodigoProduto.get().isdigit():
        #         raise InvalidMatricula()

        # # Mostra mensagem avisando o usuário sobre o erro
        # except EmptyField:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "Por favor, preencha todos os campos!")

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InformationAlreadyExists:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "Este nome ou número de matrícula já está existe!")

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidName:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "O nome está inválido! Exemplo válido: Rodrigo Duarte")

        # # Mostra mensagem avisando o usuário sobre o erro
        # except InvalidMatricula:
        #     self.limiteIns.mostraJanela(
        #         "Cuidado, atenção!", "A matrícula está inválida! Exemplo válido: 1001")

        # else:
            # ---Caso não tenha erros cadastra o aluno---
            codigo = self.limiteIns.inputCodigoProduto.get()
            descricao = self.limiteIns.inputDescricaoProduto.get()
            valorUnitario = self.limiteIns.inputValorUnitario.get()
            # Instancia o aluno
            produto = Produto(codigo, descricao, valorUnitario)
            # Adiciona o aluno instanciado na lista de alunos
            self.produtosList.append(produto)
            self.limiteIns.mostraJanela(
                'Parabéns, perfeito!', 'O produto foi cadastrado com sucesso!')

            # Limpa os campos preenchidos
            self.clearHandler(event)

    def consultaProdutos(self):
        self.limiteCon = ConsultaProdutosView(self)

    # Método para mostrar os alunos
    def mostraProdutos(self):
        if len(self.produtosList) != 0:
            str = "Código -- Descrição -- Valor unitário\n"
            str += '------------------------------------\n'
            for produto in self.produtosList:
                str += f'{produto.getCodigoProduto()} -- {produto.getDescricaoProduto()} -- {produto.getValorUnitarioProduto()}'
                str += '\n------------------------------------\n'
        else:
            str = 'Não existem produtos cadastrados!'

        self.limiteLista = MostraProdutoView(str)

    # Método getter para pegar a lista de disciplina da grade do aluno
    # def getListDisciplinaGrade(self, alunoHistorico):
    #     # Declara uma lista para as disciplinas da grade do aluno
    #     listDisciplinaGrade = []

    #     # Pega o objeto do curso do aluno que foi passado por parâmetro
    #     curso = self.ctrlMain.ctrlCurso.getCursoObj(
    #         alunoHistorico.getCursoAluno())

    #     # Pega o objeto da grade do curso do aluno
    #     grade = self.ctrlMain.ctrlGrade.getGradeObjByCurso(curso)

    #     # Lista com apenas a lista de grades
    #     gradesList = self.ctrlMain.ctrlGrade.getGradesList()

    #     # Se os códigos das grades forem iguais, então a lista de disciplinas da grade do aluno
    #     for grad in gradesList:
    #         if grade.getCodigoGrade() == grad.getCodigoGrade():
    #             listDisciplinaGrade = grad.getDisciplinasGradeList()

    #     return listDisciplinaGrade

    # # Método getter para pegar o objeto aluno
    # def getAlunoObj(self, matriculaHistorico):
    #     # Declara um objeto vazio
    #     objAluno = None
    #     # Se a matrícula passada como parâmetro é igual então ele retorna o objeto aluno inteiro para passar pro histórico
    #     for aluno in self.alunosList:
    #         if aluno.getNroMatric() == matriculaHistorico:
    #             objAluno = aluno
    #     return objAluno

    def getProdutoObject(self, code):
        produtoObject = None
        for pro in self.produtosList:
            if pro.getCodigoProduto() == code:
                produtoObject = pro
        return produtoObject

    def consultaHandler(self, event):
        # try:
        #     if len(self.limiteCon.inputNro.get()) == 0:
        #         raise EmptyField()
        # except EmptyField:
        #     str = 'Campo de matrícula vazio! Por favor, digite um número de matrícula!'
        #     self.limiteCon.mostraJanela('Erro', str)

        # else:
            codigo = self.limiteCon.inputCodeProduto.get()
            produto = self.getProdutoObject(codigo)

            if produto == None:
                str = (f'Não existe produto com o código {codigo}')
                self.limiteCon.mostraJanela('Produto não encontrado', str)
                self.limiteCon.inputCodeProduto.delete(
                    0, len(self.limiteCon.inputCodeProduto.get()))
            else:
                str = 'Informações do produto consultado:\n'
                str += 'Descrição -- Valor unitário\n'
                str += produto.getDescricaoProduto() + ' -- ' + produto.getValorUnitarioProduto()
                self.limiteCon.mostraJanela('Produto encontrado', str)
                self.limiteCon.inputCodeProduto.delete(
                    0, len(self.limiteCon.inputCodeProduto.get()))

    # Método para limpar os campos de preenchimento que foram preenchidos 
    def clearHandler(self, event):
        self.limiteIns.inputCodigoProduto.delete(
            0, len(self.limiteIns.inputCodigoProduto.get()))

        self.limiteIns.inputDescricaoProduto.delete(
            0, len(self.limiteIns.inputDescricaoProduto.get()))

        self.limiteIns.inputValorUnitario.delete(
            0, len(self.limiteIns.inputValorUnitario.get()))

    # Método para destruir a tela e sair
    def concluidoHandler(self, event):
        self.limiteIns.destroy()

    def concluiHandler(self, event):
        self.limiteCon.destroy()

    # Método para salvar todas as informações que foram registradas
    def saveProdutos(self):
        if len(self.produtosList) != 0:
            with open("produtos.pickle", "wb") as f:
                pickle.dump(self.produtosList, f)