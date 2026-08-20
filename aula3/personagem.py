class personagem():

    def __init__(self, nome, vida, nivel):
        self._nome=nome
        self._vida=vida
        self._nivel=nivel
    
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
    def vida(self, n):
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
        if n>=1:
            self._nivel = ni
        else:
            print("Nível inválido!")
