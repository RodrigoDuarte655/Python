import tkinter as tk
from tkinter import messagebox


class ModelCliente():
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email


class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()
        self.viewPanel = ViewPanel(master, controller)


class ViewPanel():
    def __init__(self, root, controller):
        self.controller = controller
        self.janela = tk.Frame(root)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()

        self.labelInfo1 = tk.Label(self.frame1, text="Nome:")
        self.labelInfo2 = tk.Label(self.frame2, text="Email:")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")

        self.buttonSubmit = tk.Button(self.janela, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)

        self.buttonClear = tk.Button(self.janela, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonClients = tk.Button(self.janela, text="Show clients")
        self.buttonClients.pack(side='left')
        self.buttonClients.bind("<Button>", controller.clientsHandler)

    def showWindow(self, title, message):
        messagebox.showinfo(title, message)


class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.listaClientes = []

        # Create the view passing reference of the main window and itself
        self.view = View(self.root, self)

        self.root.title('MVC example')
        # Initiate the mainloop
        self.root.mainloop()

    def enterHandler(self, event):
        clientName = self.view.viewPanel.inputText1.get()
        clientEmail = self.view.viewPanel.inputText2.get()
        client = ModelCliente(clientName, clientEmail)
        self.listaClientes.append(client)
        self.view.viewPanel.showWindow(
            'Success', 'Client successfully registered ')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.viewPanel.inputText1.delete(
            0, len(self.view.viewPanel.inputText1.get()))
        self.view.viewPanel.inputText2.delete(
            0, len(self.view.viewPanel.inputText2.get()))

    def clientsHandler(self, event):
        self.message = 'Yeahhhhh, Clients registered:\n'
        for clients in self.listaClientes:
            self.message += clients.getNome() + ' - ' + clients.getEmail() + '\n'
        self.view.viewPanel.showWindow('Clients List', self.message)


if __name__ == '__main__':
    c = Controller()


""" 
https://drive.google.com/file/d/1r2VfrlWAawKB79ruMmbU0NPOtOgBDHZb/view

53:12 """
