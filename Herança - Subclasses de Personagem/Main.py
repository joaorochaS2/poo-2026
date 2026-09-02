item = Item("Espada de Aço", 3)

m = Mago("Elara", 65, 15, 4)
m.pegarItem(item)
m.ficha()

g = Guerreiro("Bran", 100, 5, 3)
g.receberDano(8)
g.ficha()

m.setMana(-10)
