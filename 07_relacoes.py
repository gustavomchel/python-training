"""
Implemente um sistema orientado a objetos em Python para
representar uma biblioteca com as 
classes Biblioteca, Livro, Autor e Usuario, 
aplicando os conceitos de associação, agregação, composição e dependência. 

A classe Autor deve armazenar nome e nacionalidade; 
A classe Livro deve conter título, ano e uma referência a um Autor (agregação). 
A classe Biblioteca deve possuir um nome e ser responsável por criar e armazenar os livros internamente (composição). 
A classe Usuario deve conter o nome e manter uma referência à Biblioteca à qual está associado (associação), 
além de possuir um método para pegar um livro emprestado, usando temporariamente o livro sem
armazená-lo (dependência).
"""

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor.nome # Relação de agregação        

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def criar_livro(self, titulo, ano, autor):
        livro = Livro(titulo, ano, autor) #Relação de composição
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' criado com sucesso!")

class Usuario:
    def __init__(self, nome, biblioteca):
        self.nome = nome 
        self.biblioteca = biblioteca #Relação de associação
        
    def pegar_emprestado(self, livro):
        print(f"{self.nome} pegou o livro {livro.titulo} emprestado na Biblioteca {self.biblioteca.nome}!") #Relação de dependência


#autor
nome = input("Informe o nome do autor: ")
nacionalidade = input("Informe a nacionalidade do autor: ")
autor = Autor(nome, nacionalidade)
print(autor.nome)
print(autor.nacionalidade)

#livro
titulo = input("Informe o titulo do livro: ")
ano = input("Informe o ano do livro: ")
livro = Livro(titulo, ano, autor)
print(livro.titulo)
print(livro.ano)
print(livro.autor)

#biblioteca
nome = input("Informe o nome da biblioteca: ")
biblioteca = Biblioteca(nome)
biblioteca.criar_livro(titulo, ano, autor)
print(biblioteca.nome)
for livro in biblioteca.livros:
    print(f"- {livro.titulo}")

#usuario
nome = input("Informe o nome do usuário: ")
usuario = Usuario(nome, biblioteca)
usuario.pegar_emprestado(livro)

