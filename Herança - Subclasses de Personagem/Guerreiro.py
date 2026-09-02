class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca, nivel):
        super().__init__(nome, vida, forca, nivel)
        self.setDefesa(5)

    def getDefesa(self):
        return self.defesa

    def setDefesa(self, d):
        if d >= 0:
            self.defesa = d

    def receberDano(self, dano):
        dano_efetivo = dano - self.getDefesa()

        if dano_efetivo < 0:
            dano_efetivo = 0

        self.setVida(self.getVida() - dano_efetivo)
        print(self.getNome() + " recebeu " + str(dano_efetivo) + " de dano")

    def ficha(self):
        print("\n====FICHA==== \nNome: " + self.getNome() +
              "\nVida: " + str(self.getVida()) +
              "\nForça: " + str(self.getForca()) +
              "\nNivel: " + str(self.getNivel()) +
              "\nDefesa: " + str(self.getDefesa()) +
              "\nInventario:")

        if len(self.getInventario()) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.getInventario())):
                print(self.getInventario()[0].descricao())

        print("===========")
