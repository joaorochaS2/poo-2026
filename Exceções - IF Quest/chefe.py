from personagem import Personagem

class Chefe(Personagem):
    def __init__(self, n="Chefe"):
        super().__init__(n, 200, 20, 1)
    def habilidade(self):
        return "ataque devastador"
    def ficha(self):
        print("\n[Chefe] ", self._nome, " Força: ", self._forca, " Vida: ", self._vida)
