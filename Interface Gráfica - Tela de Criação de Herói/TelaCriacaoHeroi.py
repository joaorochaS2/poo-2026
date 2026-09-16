import tkinter as tk


class TelaCriacaoHeroi(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("IF Quest")
        self.geometry("600x300")

        self.titulo = tk.Label(
            self,
            text="Criação de Herói"
        )
        self.titulo.pack(side="top")

        painel = tk.Frame(self)

        rotulo_nome = tk.Label(
            painel,
            text="Nome:"
        )
        rotulo_nome.grid(row=0, column=0)

        self.campo_nome = tk.Entry(
            painel,
            width=15
        )
        self.campo_nome.grid(row=0, column=1)

        rotulo_vida = tk.Label(
            painel,
            text="Vida:"
        )
        rotulo_vida.grid(row=1, column=0)

        self.campo_vida = tk.Entry(
            painel,
            width=15
        )
        self.campo_vida.grid(row=1, column=1)

        rotulo_forca = tk.Label(
            painel,
            text="Força:"
        )
        rotulo_forca.grid(row=2, column=0)

        self.campo_classe = tk.Entry(
            painel,
            width=15
        )
        self.campo_classe.grid(row=2, column=1)

        painel.pack(expand=True)

        self.botao_criar = tk.Button(
            self,
            text="Criar Herói",
            state="disabled"
        )
        self.botao_criar.pack(side="bottom")

        self.titulo.config(
            text="Criação de Herói - IF Quest"
        )


if __name__ == "__main__":
    tela = TelaCriacaoHeroi()
    tela.mainloop()