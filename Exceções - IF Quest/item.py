class item():
    def __init__(self, n="Sem nome", b=0):
        self.nome=n
        self.bonus=b
    @property
    def nome(self):
        return self._nome
    @property
    def bonus(self):
        return self._bonus
    @nome.setter
    def nome(self, n=""):
        self._nome = n
    @bonus.setter
    def bonus(self, b):
        if (b>=0):
            self._bonus = b

    def descricao(self):
        return self._nome + " (+" + str(self._bonus) + ")"
