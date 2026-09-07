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
        return self._nome, " (+", self._bonus, ")"

from abc import ABC, abstractmethod
class Personagem(ABC):

    def __init__(self, n="Nome", v=50, f=5, ni=1):
        self._nome=n
        self._vida=v
        self._forca=f
        self._nivel=ni
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
            print("Nome inválido!")

    @vida.setter
    def vida(self, v):
        if v>=0:
            self._vida = v
        else:
            print("Vida inválida!")

    @forca.setter
    def forca(self, f):
        self._forca=f

    @nivel.setter
    def nivel(self, ni):
        if ni>=1:
            self._nivel = ni
        else:
            print("Nível inválido!")

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
        return "rajada arcana"

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
        print(self.nome + " recebeu " + dano_efetivo + " de dano")

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
        return "escudo de aço"

class Chefe(Personagem):
    def __init__(self, n="Chefe"):
        super().__init__(n, 200, 20, 1)
    def habilidade(self):
        return "ataque devastador"
    def ficha(self):
        print("\n[Chefe]", self._nome, "( Vida:", self._vida, "Força:", self._forca, ")")

herois = []
herois.append(Mago("Elara", 60, 5, 1))
herois.append(Guerreiro("Bran", 100, 3, 1))
chefe = Chefe("Rei Julian")

for h in herois:
    h.ficha()
    print("\n" + h.nome + " usou " + h.habilidade())
    h.atacar(chefe)
chefe.ficha()
for h in herois:
    if isinstance (h,Mago):
        print("\n", h.nome, " tem ", h.mana, " de mana")
if (chefe.vida>0):
    print("\nChefe [" + chefe.nome + "] não foi derrotado.")  
