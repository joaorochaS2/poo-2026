class Personagem:
    def __init__(self, n=None, v=0, f=0, ni=1):
        self.nome = None
        self.vida = 0
        self.forca = 0
        self.nivel = 1
        self.inventario = []

        if n is not None:
            self.setNome(n)
        self.setVida(v)
        self.setForca(f)
        self.setNiveL(ni)

    def getNome(self):
        return self.nome

    def getVida(self):
        return self.vida

    def getForca(self):
        return self.forca

    def getNivel(self):
        return self.nivel

    def getInventario(self):
        return self.inventario

    def setNome(self, n):
        if n is not None:
            self.nome = n
        else:
            print("Nome inválido!")

    def setVida(self, v):
        if v >= 0 and v <= 100:
            self.vida = v
        else:
            print("Vida inválida!")

    def setForca(self, f):
        self.forca = f

    def setNiveL(self, n):
        if n >= 1:
            self.nivel = n
        else:
            print("Nível inválida!")

    def setInventario(self, i):
        self.inventario = i

    def pegarItem(self, i):
        self.inventario.append(i)
        self.calcular_forca()

    def calcular_forca(self):
        for i in range(len(self.getInventario())):
            self.setForca(
                self.getForca() + self.getInventario()[i].getBonus()
            )

    def receberDano(self, d):
        self.vida = self.vida - d

        if self.vida < 0:
            self.vida = 0

        print(self.getNome() + " recebeu " + str(d) + " de dano")

    def atacar(self):
        self.atacar_forca(10)

    def atacar_forca(self, f):
        print(self.nome + " atacou com " + str(f) + " de força")

    def ficha(self):
        print(
            "\n====FICHA==== \nNome: " + self.getNome() +
            "\nVida: " + str(self.getVida()) +
            "\nForça: " + str(self.getForca()) +
            "\nNivel: " + str(self.getNivel()) +
            "\nInventario:"
        )

        if len(self.getInventario()) == 0:
            print("Inventario Vazio.")
        else:
            for i in range(len(self.getInventario())):
                print(self.getInventario()[0].descricao())

        print("===========")
