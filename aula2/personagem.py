class personagem():
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def receberDano(self, dano):
        self.vida = self.vida - dano
        print("%s recebeu %d de dano" %(self.nome, dano))
        if self.vida<0:
            self.vida=0
    
    def estaVivo(self):
        if self.vida>0:
            return True
        else:
            return False

    def ficha(self):
        print("\nNome: ", self.nome)
        print("Vida: ", self.vida)
        print("Força: ", self.forca)
    
    def atacar(self, alvo):
        print(self.nome, " ataca ", alvo.nome)
        alvo.receberDano(self.forca)

if __name__ == "__main__":

    jogador = personagem("Raquel", 100, 10)
    chefe = personagem("Barbie", 500, 40)

    print("===Ficha===")
    jogador.ficha()
    chefe.ficha()
    print("===Batalha===")
    while jogador.estaVivo() and chefe.estaVivo():
        jogador.atacar(chefe)
        if not chefe.estaVivo():
            break
        chefe.atacar(jogador)
        if not jogador.estaVivo():
            break

    print("===Ficha===")
    jogador.ficha()
    chefe.ficha()
