import tkinter as tk
import sqlite3
from tkinter import ttk
from app.cadastro_produto_ui import CadastroProdutoUI
from app.cadastro_produto import cadastrar_produto

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Software de Vendas")
        self.root.configure(background='#F5F5F5')
        self.root.minsize(742, 472)
        self.root.maxsize(1920, 1080)
        self.root.geometry("300x300+50+50")

        self.create_ui()

        self.pedidos_window = None
        self.produtos_window = None

    def create_ui(self):
        left_frame = ttk.Frame(self.root, width=200, height=400)
        left_frame.grid(row=1, column=0, padx=10, pady=5)

        pedidos_button = ttk.Button(left_frame, text="Pedidos", command=self.show_pedidos)
        pedidos_button.grid(row=0, column=0, padx=5, pady=5)

        right_frame = ttk.Frame(self.root, width=200, height=400)
        right_frame.grid(row=1, column=1, padx=10, pady=5)

        produtos_button = ttk.Button(right_frame, text="Listar Produtos", command=self.show_produtos)
        produtos_button.grid(row=0, column=0, padx=5, pady=5)

        cadastrar_produto_button = ttk.Button(right_frame, text="Cadastrar Produto", command=self.abrir_janela_cadastro_produto)
        cadastrar_produto_button.grid(row=1, column=0, padx=5, pady=5)

    def show_pedidos(self):
        if self.pedidos_window is None:
            self.pedidos_window = tk.Toplevel(self.root)
            self.pedidos_window.title("Pedidos")
            # Configurar a interface da tela de pedidos aqui
        else:
            self.pedidos_window.deiconify()  # Mostra a janela de pedidos
        if self.produtos_window is not None:
            self.produtos_window.withdraw()  # Esconde a janela de produtos se estiver aberta


    def show_produtos(self):
        if self.produtos_window is None:
            self.produtos_window = tk.Toplevel(self.root)
            self.produtos_window.title("Produtos")

            # Recuperar os produtos do banco de dados (exemplo)
            produtos = self.recuperar_produtos_do_banco()  # Implemente essa função

            # Criar uma lista para exibir os produtos
            produtos_listbox = tk.Listbox(self.produtos_window,width=40,height=40)
            produtos_listbox.pack()


            # Preencher a lista com os dados dos produtos
        for produto in produtos:
            produtos_listbox.insert(tk.END, f"codigo:{produto['COD_PRODUTO']} - Nome: {produto['PRODUTO']} - Valor: {produto['VALOR_UNITARIO']}")

        else:
            self.produtos_window.deiconify()  # Mostra a janela de produtos
        if self.pedidos_window is not None:
            self.pedidos_window.withdraw()  # Esconde a janela de pedidos se estiver aberta

        # Função de exemplo para recuperar produtos do banco de dados
    def recuperar_produtos_do_banco(self):
        # Conectar-se ao banco de dados (assumindo que já existe uma conexão)
        conn = sqlite3.connect("SPDV.db")
        cursor = conn.cursor()

        # Definir a instrução SQL de consulta para listar todos os produtos
        sql = "SELECT * FROM PRODUTOS"

        # Executar a instrução SQL
        cursor.execute(sql)

        # Recuperar os dados (todos os produtos) resultantes da consulta
        produtos = cursor.fetchall()

        # Fechar a conexão com o banco de dados
        conn.close()

        # Retorna os produtos como uma lista de dicionários
        return [{"COD_PRODUTO": produto[0],"PRODUTO": produto[1], "VALOR_UNITARIO": produto[2]} for produto in produtos]
    #def cadastrar_novo_produto(self):
     #   cadastrar_produto()

    def abrir_janela_cadastro_produto(self):
       cadastro_produto_window = tk.Toplevel(self.root)
       CadastroProdutoUI(cadastro_produto_window)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()