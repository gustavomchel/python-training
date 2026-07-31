"""
Você foi contratado para desenvolver um sistema para gerenciar
informações e estatísticas dos clubes participantes da Copa do Mundo de
Clubes da FIFA. 

Para isso, implemente uma classe abstrata chamada
ClubeParticipante com os atributos nome, pais, confederacao,
ranking_fifa, gols_marcados e vitorias, 
incluindo um método concreto exibir_dados() para mostrar os dados do clube, e métodos abstratos
calcular_desempenho() — que deve calcular um índice baseado na
fórmula específica da confederação (para clubes da UEFA: desempenho
= vitórias × 3 + gols marcados × 0,5; para clubes da CONMEBOL:
desempenho = vitórias × 3 + gols marcados × 0,7) — e
gerar_relatorio_tecnico(), que deve exibir as informações básicas do clube
junto com o desempenho calculado. 

Crie duas subclasses concretas, ClubeUEFA e ClubeCONMEBOL, que implementem esses métodos de
acordo com as regras definidas, e teste a aplicação criando instâncias de
cada tipo, demonstrando o uso de abstração, herança e polimorfismo em Python.

"""

from abc import ABC, abstractmethod

# Classe
class ClubeParticipante:
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self.nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(self):
        print(f"\nClube: {self.nome}")
        print(f"\nPaís: {self.pais}")
        print(f"\nConfederação: {self.confederacao}")
        print(f"\nRanking Fifa: {self.ranking_fifa}")

    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def gerar_relatorio(self):
        pass

# Subclasse
class ClubeUEFA(ClubeParticipante):
    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.7)

    def gerar_relatorio(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho técnico: {desempenho:.2f}\n")


# Subclasse
class ClubeCONMEBOL(ClubeParticipante):
    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.7)
    
    def gerar_relatorio(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho técnico: {desempenho:.2f}\n")


def main():
    real_madrid = ClubeUEFA("Real Madrid", "Espanha", "UEFA", 1, 10, 4)
    botafogo = ClubeCONMEBOL("Botafogo", "Brasil", "CONMEBOL", 5, 12, 3)

    clubes = [real_madrid, botafogo]

    for clube in clubes:
        print("\n" + "-" * 40)
        clube.gerar_relatorio()

if __name__ == "__main__":
    main()