import tkinter as tk
from app.cadastro_produto import cadastrar_produto

class CadastroProdutoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produto")
        self.root.geometry("400x200")
        self.root.maxsize(1920, 1080)
        self.root.config(bg="lightgrey")
        
        # Adicione os elementos da interface, como campos de entrada, botões, etc., aqui

        # entrada do nome do produto
        tk.Label(root, text="Nome do Produto", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5)
        name = tk.Entry(root, bd=3)
        name.grid(row=1, column=2, padx=5, pady=5)

        #valor unitário do produto
        tk.Label(root, text="Valor Unitário R$", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
        valor_unit = tk.Entry(root, bd=3)
        valor_unit.grid(row=3, column=2, padx=5, pady=5)

        salvar_produto = tk.Button(root, text="Salvar", command=lambda: cadastrar_produto(valor_unit.get(), name.get()))
        salvar_produto.grid(row=4, column=1, padx=5, pady=3)

        self.root.mainloop()