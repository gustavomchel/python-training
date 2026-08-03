"""
Desenvolva um sistema para gerenciar veículos de transporte
público em uma cidade inteligente. 

Crie uma classe abstrata VeiculoTransporte, com os atributos placa e
capacidadePassageiros, e um método abstrato calcularCustoOperacional() 
que retorna o custo por quilômetro. 

Crie as subclasses Onibus, com o atributo consumoPorKm (litros/km), e Metro, 
com consumoEnergiaPorKm (kWh/km). 

Cada uma deve implementar o cálculo do custo com valores fictícios: R$ 6,00
por litro de diesel e R$ 0,80 por kWh. 

Na função principal, permita criar objetos dos dois tipos e exibir os custos
operacionais usando polimorfismo. 

Implemente tratamento de exceções para validar os dados de entrada: placa não pode
ser vazia, e os valores numéricos devem ser positivos.
"""
from abc import ABC, abstractmethod

class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidadePassageiros):
        self.placa = placa
        self.capacidadePassageiros = capacidadePassageiros

    @abstractmethod
    def calcularCustoOperacional(self):
        pass

class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoPorKm):
        super().__init__(placa, capacidadePassageiros)
        self.consumoPorKm = consumoPorKm

    def calcularCustoOperacional(self):
        return self.consumoPorKm * 6.0


class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidadePassageiros, consumoEnergiaPorKm):
        super().__init__(self, placa, capacidadePassageiros)
        self.consumoEnergiaPorKm = consumoEnergiaPorKm

    def calcularCustoOperacional(self):
        return self.consumoEnergiaPorKm * 0.80

def main():
    veiculos = []

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Ônibus")
        print("2. Cadastrar Metrô")
        print("3. Mostrar custos operacionais")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastro de Ônibus:")

            try:
                placa = input("Placa: ").strip()

                if placa == "":
                    raise ValueError("A placa não pode estar vazia.")

                capacidade = int(input("Capacidade de Passageiros: "))

                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")

                consumo = float(input("Consumo por km (litros/km): "))

                if consumo <= 0:
                    raise ValueError("O consumo deve ser positivo.")

                veiculos.append(Onibus(placa, capacidade, consumo))

                print("\nÔnibus cadastrado com sucesso!")

            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":  
            print("\nCadastro de Metrô:")
        
            try:
                placa = input("Identificação: ").strip()

                if placa == "":
                    raise ValueError("A identificação não pode estar vazia.")

                capacidade = int(input("Capacidade de Passageiros: "))

                if capacidade <= 0:
                    raise ValueError("A capacidade deve ser positiva.")

                consumo = float(input("Consumo por km (kWh/km): "))

                if consumo <= 0:
                    raise ValueError("O consumo deve ser positivo.")

                veiculos.append(Metro(placa, capacidade, consumo))

                print("\nMetrô cadastrado com sucesso!")

            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "3":
            if not veiculos:
                print("\nNenhum veículo cadastrado!\n")
            else:
                print("\n--- Custos operacionais por km ---")
                for v in veiculos:
                    tipo = "Ônibus" if isinstance(v, Onibus) else "Metrô"
                    custo = v.calcularCusto()
                    print(f"{tipo} {v.placa}: R$ {custo:.2f} por km")
                print()
                    
        

        elif opcao == "0":
            print("\nEncerrando o sitema...")
            break

        else:
            print("Opção inválida! Por favor, tente novamente...")


if __name__=="__main__":
    main()

