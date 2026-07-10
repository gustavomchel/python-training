"""
Crie um programa em Python utilizando orientação a objetos
para gerenciar uma lista de produtos de um carrinho de
compras. Implemente uma classe chamada Produto, com
atributos privados (__nome, __preco e __quantidade) e
métodos públicos para acessar e modificar esses valores de
forma segura (getters e setters). Em seguida, implemente uma
classe CarrinhoDeCompras, que mantém uma lista de objetos
Produto e possui métodos para adicionar um produto ao
carrinho, remover um produto pelo nome, calcular o valor total
da compra e listar os produtos com suas quantidades e
preços individuais. O programa principal deve permitir que o
usuário adicione e remova produtos, visualize o conteúdo do
carrinho e o total da compra. Utilize encapsulamento para
proteger os dados dos produtos e boas práticas de
organização orientada a objetos.
"""

"""
# Fragmentando o código em partes para melhor compreensão:

Classe Produto
Atributos privados: (__nome, __preco e __quantidade) ok
métodos públicos: (get-acesso e set-modificação) ok

Classe CarrinhoDeCompras
Lista de objetos(Produto) ok
Métodos: adicionar_produto, remover_produto, calcular_total, listar_produtos ok

Programa principal(main):
Usuario adicionar, remover, visualizar o carrinho e o total da compra ok

"""
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade


class CarrinhoDeCompras:
    def __init__(self):
        self.lista_produtos = list()

    def adicionar_produto(self, produto):
        self.lista_produtos.append(produto)

    def remover_produto(self, nome_excluir):
        for produto in self.lista_produtos:
            if produto.get_nome().lower() == nome_excluir.lower():
                self.lista_produtos.remove(produto)
                return True
        return False
    
    def calcular_total(self):
        total = 0.0
        for produto in self.lista_produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total 

    def listar_produtos(self):
        if not self.lista_produtos:
            print("Seu carrinho está vazio!")
        else:
            print("=== Carrinho de Compras ===")
            for produto in self.lista_produtos:
                print(f"\n- {produto.get_nome()} = {produto.get_preco()} x {produto.get_quantidade()}")


def main():
    carrinho = CarrinhoDeCompras()

    while True:
        print("===== SISTEMA E-COMMERCE =====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Visualizar carrinho e total")
        print("4 - Sair")

        opcao = input("Escolha uma opção(1-4): ")

        if opcao == "1":
            nome = input("Informe o nome do produto: ")
            preco = float(input("Informe o valor do produto: "))
            quantidade = int(input("Informe a quantidade de produtos: "))

            produto = Produto(nome, preco, quantidade)
            carrinho.adicionar_produto(produto)

            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            nome_excluir = input("Informe o nome do produto que deseja excluir: ")
            if carrinho.remover_produto(nome_excluir):
                print("Produto removido com sucesso!")
            else:
                print("Produto não encontrado no carrinho!")

        elif opcao == "3":
            carrinho.listar_produtos()
            total = carrinho.calcular_total()
            print(f"Total da compra: R$ {total:.2f}")

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()