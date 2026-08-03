"""
Implemente uma calculadora simples em Python que ofereça um
menu para o usuário escolher entre as operações: (1) soma, (2)
subtração, (3) multiplicação, (4) divisão e (5) sair. 

Para cada operação, o programa deve pedir dois números ao usuário e
mostrar o resultado. 

Use blocos try/except para garantir que o programa não quebre caso o usuário 
digite valores inválidos (ex:letras em vez de números) ou tente dividir por zero. 

O programa deve continuar funcionando normalmente após qualquer erro,
permitindo novas operações até o usuário escolher sair.
"""

class Calculadora:
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ZeroDivisionError("\nNão é possível dividir por zero!\n")
        return a / b

class Interface:
    def __init__(self):
        self.calc = Calculadora()

    def menu(self):
        while True:
            print("\n=== Calculadora Simples ===")
            print("1. Soma")
            print("2. Subtracao")
            print("3. Multiplicacao")
            print("4. Divisao")
            print("5. Sair")

            opcao = input("\nEscolha uma opção(1-5): ").strip()

            if opcao == "5":
                print("\nSaindo da calculadora. Até logo!")

            if opcao not in {"1", "2", "3", "4", "5"}:
                print("\nOpção inválida. Por favor, escolha entre 1 e 5.")
                continue

            try:
                a = float(input("\nDigite o primeiro número: "))
                b = float(input("\nDigite o segundo número: "))

                if opcao == "1":
                    resultado = self.calc.soma(a, b)
                elif opcao == "2":
                    resultado = self.calc.subtracao(a, b)
                elif opcao == "3":
                    resultado = self.calc.multiplicacao(a, b)
                elif opcao == "4":
                    resultado = self.calc.divisao(a, b)

                print(f"\nResultado: {resultado}\n")

            except ValueError:
                print("\nErro: Por favor, digite um número válido!\n")
            except ZeroDivisionError as e:
                print(f"\nErro: {e}\n")


if __name__=="__main__":
    interface = Interface()
    interface.menu()