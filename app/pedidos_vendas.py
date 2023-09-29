import tkinter as tk
from tkinter import ttk

class PedidoDeVendasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pedidos de Vendas")
        self.root.geometry("1333x720")
        self.root.maxsize(1920, 1080)
        self.root.config(bg="lightgrey")

        self.left_frame = tk.Frame(root, width=650, height=400, bg='grey')
        self.left_frame.grid(row=0, column=0, padx=10, pady=5)

        self.novo_pedido_button = ttk.Button(self.left_frame, text="Novo Pedido", command=self.novo_pedido)
        self.novo_pedido_button.grid(row=0, column=0, padx=5, pady=3)

        self.pedidos_pendentes_listbox = tk.Listbox(self.left_frame, selectmode=tk.SINGLE)
        self.pedidos_pendentes_listbox.grid(row=1, column=0, padx=5, pady=5)
        self.populate_pedidos_pendentes()  # Preenche a lista de pedidos pendentes

    def novo_pedido(self):
        # Implemente a lógica para criar um novo pedido aqui
        print("Criar novo pedido")

    def populate_pedidos_pendentes(self):
        # Simula o preenchimento da lista de pedidos pendentes (substitua com seus próprios dados)
        for i in range(1, 6):
            self.pedidos_pendentes_listbox.insert(tk.END, f"Pedido {i}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PedidoDeVendasApp(root)
    root.mainloop()