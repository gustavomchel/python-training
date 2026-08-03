"""
No universo de Dragon Ball, desenvolva um sistema em
Python para simular um torneio de artes marciais, utilizando
orientação a objetos. 

Crie uma classe totalmente abstrata chamada Lutador, contendo 
apenas métodos abstratos para obter o nome do lutador, o nível 
de poder e realizar um ataque. 

Em seguida, implemente subclasses como Saiyajin,
Androide e Namekuseijin, cada uma com um comportamento
específico ao atacar. 

O sistema deve conter um menu interativo que permita cadastrar 
lutadores de diferentes raças, listar todos os lutadores inscritos 
no torneio e simular ataques, demonstrando o uso de herança, abstração 
total e polimorfismo. 

Implemente também tratamento de exceções, garantindo que os nomes não estejam 
vazios e que o nível de poder seja um valor numérico positivo.
"""

from abc import ABC, abstractmethod

class Lutador(ABC):
    @abstractmethod
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    @abstractmethod
    def realizar_ataque(self):
        pass

class Saiyajin(Lutador):
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def realizar_ataque(self):
        print(f"{self.nome} com nivel {self.nivel} disparou feixe de luz!")

class Androide(Lutador):
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def realizar_ataque(self):
        print(f"{self.nome} com nivel {self.nivel} absorveu grande quantidade de energia!")

class Namekuseijin(Lutador):
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def realizar_ataque(self):
        print(f"{self.nome} com nivel {self.nivel} disparou rajada de energia!")
    

