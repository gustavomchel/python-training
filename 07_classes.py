"""
Implemente uma classe Casa que contenha vários objetos do
tipo Comodo, sendo que cada cômodo possui nome (ex: sala,
cozinha, banheiro) e área. 

Os cômodos devem ser implementados de forma que só existam se a casa existir
(relação de composição), e não devem ser acessados ou
manipulados diretamente de fora. 

Implemente um método na casa para calcular a área total, somando as áreas de todos os cômodos. 

Desenvolva um programa com menu interativo no console que permita criar uma casa, adicionar cômodos à
casa, listar os cômodos da casa, calcular e exibir a área total
da casa e encerrar o programa.

"""
class Comodo:
    def __init__(self, nome, comprimento, largura):
        self.nome = nome
        self.comprimento = comprimento
        self.largura = largura

class Casa:
    def __init__(self, casa):
        self.casa = casa

    def criar_comodos(self, nome, comprimento, largura):
        self.comodo = Comodo(nome, comprimento, largura) #Relação de Composição
        self.comodos = []

    def calcular_area_total(self):
        total = 0.0
        for self.comodo in self.comodos:
            area = self.comodo.comprimento * self.comodo.largura
            total += area
            return total
        print()

def main():
    casas = []
    while True:
        print("=== SISTEMA DE ENGENHARIA CIVIL ===")
        print("1 - Criar uma casa")
        print("2 - Adicionar cômodos à casa")
        print("3 - Listar cômodos da casa")
        print("4 - Calcular e exibir a área total")
        print("5 - Sair")

        opcao = input("Informe a opção desejada(1-5): ")

        if opcao == "1":
            
            nova_casa.casa = input("Informe o nome da casa: ")
            nova_casa = Casa(nova_casa.casa)
            casas.append(nova_casa.casa)

        elif opcao == "2":
            if not casas:
                print("Não casas cadastradas!")
            else:
                print("Casas cadastradas:")
                for i, casa in enumerate(casas):
                    print(f"{i + 1} - {casa}")

                opcao = input("Informe a casa desejada pera cadastrar cômodos: ")

                if opcao == casa:
                    nome = input("Informe o nome do cômodo: ")
                    comprimento = input("Informe o tamanho do comprimento do cômodo: ")
                    largura = input("Informe o tamanho da largura do cômodo: ")

                    comodo = casa.comodo(nome, comprimento, largura)
                    casa.comodos.append(comodo)

                    print(f"O cômodo {comodo.nome} foi adicionado a casa com sucesso!")

        elif opcao == "3":
            if not casa.comodos:
                print("Não há cômodos na casa!")
            else:
                for casa.comodo in casa.comodos:
                    print(f"- Cômodo: {casa.comodo}\n")
                    break
            
        elif opcao == "4":
            if not casa.comodos:
                print("Não há cômodos para calcular!")
            else:
                print(f"Total da área calculada: {casa.calcular_area_total.total}")
        
        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")


                
if __name__=="__main__":
    main()





