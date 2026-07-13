"""
Desenvolva uma classe Departamento com nome e um vetor
de objetos Funcionario, onde cada funcionário tem nome e
salário, permitindo que funcionários existam
independentemente do departamento para que possam ser
adicionados ou removidos livremente (agregação).
Implemente métodos no Departamento para adicionar
funcionários, calcular a média salarial e listar todos os
funcionários. Crie um programa com menu interativo no
console que permita criar departamentos, criar funcionários,
adicionar funcionários a departamentos, listar funcionários e
mostrar a média salarial, além de permitir sair do programa.

classe Departamento
Atributos: nome, lista_funcionarios
Métodos: adicionar_funcionarios, calcular__media_salarial, listar_funcionarios

classe Funcionario
Atributos: nome, salario

def menu
Opcoes: criar departamentos, criar funcionarios, adicionar funcionarios a departamentos, listar funcionarios, mostrar meédia salarial e sair do programa
"""

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.lista_funcionarios = list()

    def adicionar_funcionario(self, funcionario):
        self.lista_funcionarios.append(funcionario)

    def listar_funcionarios(self, funcionarios):
        for funcionario in funcionarios:
            print(f"- {funcionario.get_nome}")
            break


"""
    def calcular_media_salarial(self, funcionarios):
        soma = 0.0
        contador = 0
        for funcionario in funcionarios:
            soma += funcionario.get_salario()
            contador += 1
            break
        media = soma / contador

        print(f"Média salarial: {media}")
"""


def main():
    departamentos = list()
    funcionarios = list()
    
    while True:
        print("=== SISTEMA DE FUNCIONARIOS ===")
        print("1 - Criar departamentos")
        print("2 - Criar funcionários")
        print("3 - Adicionar funcionários a departamentos")
        print("4 - Listar funcionários")
        print("5 - Mostrar média salarial")
        print("6 - Sair")

        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            nome = input("Informe o nome do departamento: ")
            novo_departamento = Departamento(nome)
            departamentos.append(novo_departamento)

            print("Departamento cadastrado com sucesso!")

        elif opcao == "2":
            nome = input("Informe o nome do funcionário: ")
            salario = float(input("Informe o salário do funcionário: "))

            funcionario = Funcionario(nome, salario)
            funcionarios.append(funcionario)

            print("Funcionário cadastrado com sucesso!")

        elif opcao == "3":
            if not funcionarios:
                print("Não há funcionários cadastrados!")
            elif not departamentos:
                print("Não há departamentos cadastrados!")
            else:
                nome_funcionario = input("Informe o nome do funcionário: ")
                nome_departamento = input("Informe o nome do departamento: ")

                funcionario_encontrado = None
                departamento_encontrado = None

                for funcionario in funcionarios:
                    if funcionario.get_nome() == nome_funcionario:
                        funcionario_encontrado = funcionario
                        break

                for departamento in departamentos:
                    if departamento.nome == nome_departamento:
                        departamento_encontrado = departamento
                        break

                if funcionario_encontrado and departamento_encontrado:
                    departamento_encontrado.adicionar_funcionario(funcionario_encontrado)
                    print("Funcionário adicionado ao departamento com sucesso!")

                else:
                    print("Funcionário ou departamento não encontrado!")

        elif opcao == "4":
            if not funcionarios:
                print("Não há funcionários cadastrados!")
            else:
                Departamento.listar_funcionarios()
            
        elif opcao == "5":
            if not funcionarios:
                print("Não há funcionários para calcular a média salarial!")
            else:
                Departamento.calcular_media_salarial()
        
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida!")


if __name__=="__main__":
    main()
     

        
        