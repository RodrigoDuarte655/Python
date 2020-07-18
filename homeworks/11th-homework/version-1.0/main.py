# Importando biblioteca tkinter
import tkinter as tk
# Importando outras classes
import produto as pro
import notaFiscal as notfis

# Limite principal que mostra o menu com as opções 
class MainView():
    # Método construtor com a raíz e o controle
    def __init__(self, root, control):
        self.control = control
        self.root = root

        # Criando menu
        self.menuBar = tk.Menu(self.root)

        # Configuração
        self.root.config(menu=self.menuBar)

        # -------Opções do menu-------
        # Criar a opção de produto
        self.produtoMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Produto", menu=self.produtoMenu)
        self.produtoMenu.add_command(
            label="Cadastrar", command=self.control.cadastraProduto)
        self.produtoMenu.add_command(label="Consultar",
                                command=self.control.consultaProdutos)
        self.produtoMenu.add_command(
            label="Mostrar", command=self.control.mostraProduto)
        

        # Criar a opção de nota fiscal
        self.notaFiscalMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Nota fiscal", menu=self.notaFiscalMenu)
        self.notaFiscalMenu.add_command(
            label="Criar", command=self.control.criaNotaFiscal)   
        self.notaFiscalMenu.add_command(
            label="Consultar", command=self.control.consultaNotaFiscal)
        self.notaFiscalMenu.add_command(
            label="Mostrar", command=self.control.mostraNotaFiscal)
        

        # Criar a opção para sair e salvar ou sair sem salvar
        self.exitMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label="Sair", menu=self.exitMenu)
        self.exitMenu.add_command(
            label="Salvar tudo", command=self.control.saveData)
        self.exitMenu.add_command(
            label="Sair sem salvar", command=self.control.exitWithoutSaving)


# Classe do controlador principal
class MainController():
    def __init__(self):
        self.root = tk.Tk()
        # Passa a raíz que cria a janela principal e si mesma como parâmetro para o limite principal
        self.limite = MainView(self.root, self)

        # Isso irá chamar todos os controladores das outras classes, fazendo com que tudo funcione
        self.ctrlProduto = pro.CtrlProduto(self)
        self.ctrlNotaFiscal = notfis.CtrlNotaFiscal(self)

        # Cria o título do sistema
        self.root.title("Sistema MVC de emissão de nota fiscal para uma loja de confecções (POO)")
        # Tamanho da janela principal
        self.root.geometry('650x420')

        # Start the mainloop
        self.root.mainloop()

    # -----Metódos para inserir e mostrar----
    def cadastraProduto(self):
        self.ctrlProduto.cadastraProduto()

    def consultaProdutos(self):
        self.ctrlProduto.consultaProdutos()

    def mostraProduto(self):
        self.ctrlProduto.mostraProdutos()

    def criaNotaFiscal(self):
        self.ctrlNotaFiscal.criaNotaFiscal()

    def consultaNotaFiscal(self):
        self.ctrlNotaFiscal.consultaNotasFiscais()

    def mostraNotaFiscal(self):
        self.ctrlNotaFiscal.mostrarNotasFiscais()

    # ----Métodos para salvar e sair-----
    def saveData(self):
        self.ctrlProduto.saveProdutos()
        self.ctrlNotaFiscal.saveNotasFiscais()

        self.root.destroy()

    def exitWithoutSaving(self):
        self.root.destroy()


# Chamada do controlador principal que fará a aplicação rodar
if __name__ == '__main__':
    c = MainController()