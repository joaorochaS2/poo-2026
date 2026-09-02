class Item:
    def __init__(self, n="Sem nome", b=0):
        self.nome = n
        self.setBonus(b)

    def getNome(self):
        return self.nome

    def getBonus(self):
        return self.bonus

    def setNome(self, n):
        self.nome = n

    def setBonus(self, b):
        if b >= 0:
            self.bonus = b

    def descricao(self):
        return self.getNome() + " (+" + str(self.getBonus()) + ")"
