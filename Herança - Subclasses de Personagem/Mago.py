class Mago(Personagem):
    def __init__(self, nome, vida, forca, nivel):
        super().__init__(nome, vida, forca, nivel)
        self.setMana(50)

    def getMana(self):
        return self.mana

    def setMana(self, m):
        if m >= 0:
            self.mana = m
        else:
            print("Valor de mana inválido.")

    def ficha(self):
        print("\n====FICHA==== \nNome: " + self.getNome() +
              "\nVida: " + str(self.getVida()) +
              "\nForça: " + str(self.getForca()) +
              "\nNivel: " + str(self.getNivel()) +
              "\nMana: " + str(self.getMana()) +
              "\nInventario:")

        if len(self.getInventario()) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.getInventario())):
                print(self.getInventario()[0].descricao())

        print("===========")
