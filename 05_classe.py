"""
Implemente uma classe Impressora com o método
imprimir(Documento d), que recebe um objeto da classe
Documento e imprime suas informações na tela. A classe
Documento deve conter os atributos título e conteúdo. A
classe Impressora apenas utiliza o documento, sem manter
uma referência permanente a ele, caracterizando uma relação
de dependência. Desenvolva um programa com um menu
interativo no console que permita criar vários documentos,
visualizar seu conteúdo por meio da impressora e encerrar o
programa.

# Fragmentando o código em partes para melhor compreensão:

class Impressora
    método: imprimir(Documento d)

class Documento
    atributos: título, conteúdo
    métodos: __init__, get_titulo, get_conteudo
"""

class Documento:
    def __init__(self, titulo, conteudo):
        self.__titulo = titulo
        self.__conteudo = conteudo

    def get_titulo(self):
        return self.__titulo
    
    def get_conteudo(self):
        return self.__conteudo
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    
    def set_conteudo(self, novo_conteudo):
        self.__conteudo = novo_conteudo

class Impressora:
    def imprimir(self, documento):
        print(f"\nTítulo: {documento.get_titulo()}")
        print(f"Conteúdo: {documento.get_conteudo()}\n")

def main():
    documentos = list()
    impressora = Impressora()

    while True:
        print("===== SISTEMA DE IMPRESSÃO =====")
        print("1 - Cadastrar documento")
        print("2 - Imprimir documento")
        print("3 - Sair")

        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
            titulo = input("Informe o título do documento: ")
            conteudo = input("Digite o conteúdo do documento: ")

            documento = Documento(titulo, conteudo)
            documentos.append(documento)

            print("Documento cadastrado com sucesso!")
        
        elif opcao == "2":
            for documento in documentos:
                impressora.imprimir(documento)
            break

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida!")

if __name__=="__main__":
    main()


