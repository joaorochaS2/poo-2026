from personagem import Personagem
from SemManaException import SemManaException

class Mago(Personagem):
    def __init__(self, nome, vida, forca, nivel):
        super().__init__(nome, vida, forca, nivel)
        self._mana=50

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, m):
        if m >= 0:
            self._mana = m
        else:
            print("Valor de mana inválido.")

    def ficha(self):
        print("\n====FICHA==== \nNome: " + self.nome +
              "\nVida: " + str(self.vida) +
              "\nForça: " + str(self.forca) +
              "\nNivel: " + str(self.nivel) +
              "\nMana: " + str(self.mana) +
              "\nInventario:")

        if len(self.inventario) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.inventario)):
                print(self.inventario[i].descricao())
        print("===========")

    def habilidade(self):
        if self.mana < 10:
            raise SemManaException(self.mana)
        self.mana = self.mana - 10
        return "rajada arcana"
