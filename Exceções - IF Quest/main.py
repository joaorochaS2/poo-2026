from mago import Mago
from guerreiro import Guerreiro
from chefe import Chefe

herois = []
herois.append(Mago("Elara", 60, 5, 1))
herois.append(Mago("Elsa", 700, 3, 1))

while True:
    print("\n=== ESCOLHA SEU HERÓI ===")
    for i in range(len(herois)):
        print(i, "-", herois[i].nome)

    print("Digite o número do herói: ")

    try:
        q = int(input())
        h = herois[q]
        print("Herói escolhido: " + h.nome)
        break
    except ValueError:
        print("digite um número!")
    except IndexError:
        print("Esse herói não existe!")

h1 = Mago("Elara", 60, 5, 1)
h2 = Guerreiro("Bran", 100, 4, 1)
chefe = Chefe("Rei Julian")

try:
    print(h1.nome + " Personagem criado!")
    print(h2.nome + " Personagem criado!")
    print("Chefe criado!")

    h3 = Mago("Merida", -60, 5, 1)
    print("Personagem criado!")

except ValueError as e:
    print("Erro ao criar personagem!")
    print(e)

from SemManaException import SemManaException
from ForcaInsuficienteException import ForcaInsuficienteException

try:
    print("\nBatalha!!!")

    for i in range(6):
        print("\n" + h1.nome + " usou " + h1.habilidade())
        h1.atacar(chefe)

except SemManaException as e:
    try:
        print(e)
        print("O Mago perde o turno, e o Guerreiro ataca no lugar dele")
        print("\n" + h2.nome + " usou " + h2.habilidade())
        h2.atacar(chefe)

    except ForcaInsuficienteException as i:
        print(i)
        print("Ninguem pode batalhar.")

finally:
    print("\nFim do turno!\n")
