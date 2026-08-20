class Personagem():

    def __init__(self):
        self._nome=""
        self._vida=0
        self._nivel=1
    
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

if __name__ == "__main__":
    p = Personagem()
    p.nome = "nome"
    p.nome = None #Nome inválido!
    p.vida = 100
    p.vida = -10 #Vida inválida!
    p.nivel = 10
    p.nivel = 0 #Nível inválido!
