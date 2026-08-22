class Personagem():

    def __init__(self, n="Nome", v=50, ni=10):
        self._nome=n
        self._vida=v
        self._nivel=ni
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def vida(self):
        return self._vida
    
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
        if v<=100 and v>=0:
            self._vida = v
        else:
            print("Vida inválida!")


    @nivel.setter
    def nivel(self, ni):
        if ni>=1:
            self._nivel = ni
        else:
            print("Nível inválido!")

    def atacar(self, f=10):
        print(self._nome, "atacou com ", f, "de força")

if __name__ == "__main__":
    p1 = Personagem()
    p1.nome = "Raquel"
    p1.vida = 50
    p1.nivel = 10
    p2 = Personagem("Barbie", 100, 40)

    p1.atacar()
    p2.atacar(40)
