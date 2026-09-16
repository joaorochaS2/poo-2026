from personagem import Personagem
from ForcaInsuficienteException import ForcaInsuficienteException

class Guerreiro(Personagem):
    def __init__(self, nome, vida, forca, nivel):
        super().__init__(nome, vida, forca, nivel)
        self._defesa=5

    @property
    def defesa(self):
        return self._defesa

    @defesa.setter
    def defesa(self, d):
        if d >= 0:
            self._defesa = d

    def receberDano(self, dano):
        dano_efetivo = dano - self.defesa

        if dano_efetivo < 0:
            dano_efetivo = 0

        self.vida=self.vida - dano_efetivo
        print(self.nome, " recebeu ", dano_efetivo, " de dano")

    def ficha(self):
        print("\n====FICHA==== \nNome: " + self.nome +
              "\nVida: " + str(self.vida) +
              "\nForça: " + str(self.forca) +
              "\nNivel: " + str(self.nivel) +
              "\nDefesa: " + str(self.defesa) +
              "\nInventario:")

        if len(self.inventario) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.inventario)):
                print(self.inventario[i].descricao())

        print("===========")

    def habilidade(self):
        if self.forca < 10:
            raise ForcaInsuficienteException(self.forca)
        return "escudo de aço"
