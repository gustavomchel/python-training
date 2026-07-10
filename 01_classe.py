"""
Elabore um programa em Python orientado a objetos que leia
um número n (o número de termos de uma progressão
aritmética), a1 (o primeiro termo da progressão) e r (razão) e
escreva todos os termos dessa progressão, bem como a
soma dos elementos (Fórmulas da P.A.: an = a1 + r x (n – 1) e
S = n * (a1 + an) / 2).
"""

class ProgressaoAritmetica:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
    
    def gerar_termos(self):
        termos = []
        for i in range(self.n):
            termo = self.a1 + i * self.r
            termos.append(termo)
        return termos
    
    def calcular_soma(self):
        an = self.a1 + (self.n - 1) * self.r
        return self.n * (self.a1 + an) / 2

def main():
    print("===== PROGRESSÃO ARITMÉTICA =====")
    a1 = float(input("Digite o primeiro termo (a1) da PA: "))
    r = float(input("Digite a razão da PA (r): "))
    n = int(input("Digite o número de termos da PA (n): "))

    pa = ProgressaoAritmetica(a1, r, n)

    termos = pa.gerar_termos()

    print("\nTermos da PA:")
    contador = 1
    for termo in termos:
        print(f"termo {contador}: {termo}")
        contador += 1

    soma = pa.calcular_soma()
    print(f"\nA soma dos termos da PA é: {soma}")

if __name__ == "__main__":
    main()
