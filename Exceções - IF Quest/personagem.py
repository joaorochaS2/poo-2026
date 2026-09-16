from abc import ABC, abstractmethod

class Personagem(ABC):

    def __init__(self, n="Nome", v=50, f=5, ni=1):
        self.nome=n
        self.vida=v
        self.forca=f
        self.nivel=ni
        self._inventario = []

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    @property
    def forca(self):
        return self._forca

    @property
    def nivel(self):
        return self._nivel

    @nome.setter
    def nome(self, n):
        if (n != None):
            self._nome= n
        else:
            raise ValueError("Nome inválido!")

    @vida.setter
    def vida(self, v):
        if v>=0:
            self._vida = v
        else:
            raise ValueError("Vida inválida!")

    @forca.setter
    def forca(self, f):
        self._forca=f

    @nivel.setter
    def nivel(self, ni):
        if ni>=1:
            self._nivel = ni
        else:
            raise ValueError("Nível inválido!")

    def pegarItem(self, item):
        self._inventario.append(item)
        self._forca = self._forca + item.bonus

    @property
    def inventario(self):
        return self._inventario

    def receberDano(self, d):
        self._vida = self._vida - d
        if (self._vida<0):
            self._vida = 0
        print(self._nome, " recebeu ", d, " de dano.")

    def atacar(self, alvo):
        print(self._nome, " atacou ", alvo.nome)
        alvo.receberDano(self._forca)

    @abstractmethod
    def habilidade(self):
        pass

    def ficha(self):
        print(
            "\n====FICHA==== \nNome: " + self.nome +
            "\nVida: " + str(self.vida) +
            "\nForça: " + str(self.forca) +
            "\nNivel: " + str(self.nivel) +
            "\nInventario:"
        )

        if len(self.inventario) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.inventario)):
                print(self.inventario[i].descricao())

        print("===========")
