"""
Desenvolva um sistema em Python para representar
personagens de um jogo de RPG. 

Crie uma classe base chamada Personagem, com os atributos nome e nivel, 
e um método atacar() que imprime uma mensagem genérica de
ataque. 

Em seguida, crie as subclasses Guerreiro e Mago. 

A classe Guerreiro deve possuir o atributo adicional forca e
sobrescrever o método atacar() para exibir uma mensagem de
ataque físico, enquanto a classe Mago deve ter o atributo
mana e sobrescrever o método atacar() para representar um
ataque mágico. 

Na classe principal, crie instâncias das três
classes e invoque o método atacar() para demonstrar o uso
de herança e polimorfismo em tempo de execução.
"""

class Personagem:
    def __init__(self, nome="", nivel=0):
        self.nome = nome
        self.nivel = nivel

    def atacar(self):
        print("Ataque realizado!")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca=0):
        super().__init__(nome, nivel)
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} realiza ataque com a força {self.forca}.")


class Mago(Personagem):
    def __init__(self, nome, nivel,mana=0):
        super().__init__(nome, nivel)
        self.mana = mana

    def atacar(self):
        print(f"{self.nome} realiza ataque com mana {self.mana}.")



def main():
    p1 = Guerreiro(nome="LumpaLumpa", nivel=8, forca=9)
    p2 = Mago(nome="Gandaff", nivel= 9, mana=53)

    personagens = [p1, p2]

    for personagem in personagens:
        personagem.atacar()
        print("\n" + "-" * 40)

if __name__=="__main__":
    main()

