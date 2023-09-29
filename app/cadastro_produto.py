import sqlite3
import tkinter as tk
from tkinter import Button, Entry, Label, messagebox

__all__ = ['cadastrar_produto']

def salvar_img():
    '''Implemente a lógica para salvar a imagem aqui'''
    messagebox.showinfo("Informação", "Imagem Salva com Sucesso")

def cadastrar_produto(valor_unitario, Nome_produto):
    global conn  # Variável de conexão com o banco de dados
    conn = sqlite3.connect("SPDV.db")  # Conectar-se ao banco de dados
    '''Implemente a lógica para salvar o produto aqui'''
    try:
        # Conectar-se ao banco de dados (supondo que você já criou a conexão em algum lugar)
        cursor = conn.cursor()

        # Definir a instrução SQL para inserir um produto na tabela de produtos
        sql = "INSERT INTO PRODUTOS (PRODUTO, VALOR_UNITARIO) VALUES (?, ?)"

        # Executar a instrução SQL com os valores do produto
        cursor.execute(sql, (Nome_produto, valor_unitario))

        # Confirmar a transação para salvar as alterações no banco de dados
        conn.commit()

        # Exibir uma mensagem de sucesso
        messagebox.showinfo("Informação", "Produto Cadastrado com Sucesso")
    except Exception as e:
        print("Erro ao salvar o produto:", e)
        messagebox.showerror("Erro", "Erro ao salvar o produto.")
    
def main():
    

    root = tk.Tk()
    root.title("Cadastro de Produtos")
    root.geometry("1333x720")
    root.maxsize(1920, 1080)
    root.config(bg="lightgrey")

    # entrada do nome do produto
    Label(root, text="Nome do Produto", bg="lightgrey").grid(row=1, column=1, padx=5, pady=5)
    name = Entry(root, bd=3)
    name.grid(row=1, column=2, padx=5, pady=5)

    # valor unitário do produto
    Label(root, text="Valor Unitário R$", bg="lightgrey").grid(row=3, column=1, padx=5, pady=5)
    valor_unit = Entry(root, bd=3)
    valor_unit.grid(row=3, column=2, padx=5, pady=5)

    # Botão para salvar o produto com os valores das entradas de texto como argumentos
    salvar_produto = Button(root, text="Salvar", command=lambda: cadastrar_produto(valor_unit.get(), name.get()))
    salvar_produto.grid(row=4, column=1, padx=5, pady=3)

    root.mainloop()

if __name__ == "__main__":
    main()