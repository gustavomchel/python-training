"""
Faça um programa em Python orientado a objetos que, a
partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando
maiúsculas/minúsculas).
"""
class AnaliseString:
    def __init__(self, texto):
        self.texto = texto
    
    def contar_caracteres(self):
        return len(self.texto)
    
    def deixar_maiusculo(self):
        return self.texto.upper()
    
    def deixar_minuscula(self):
        return self.texto.lower()
    
    def contar_vogais(self):
        vogais = "aeiouAEIOU"
        contador = 0
        for letra in self.texto:
            if letra in vogais:
                contador += 1
        return contador
    
    def contem_ifb(self):
        return "IFB" in self.texto.upper()


def main():
    texto = input("Digite uma string: ")
    analise = AnaliseString(texto)

    print(f"\nNúmero de caracteres: {analise.contar_caracteres()}")
    print(f"String em maiúsculo: {analise.deixar_maiusculo()}")
    print(f"String em minúsculo: {analise.deixar_minuscula()}")
    print(f"Número de vogais: {analise.contar_vogais()}")
    if analise.contem_ifb():
        print("A substring 'IFB' aparece no texto.")
    else:
        print("A substring 'IFB' não aparece no texto.")
if __name__ == "__main__":
    main()
