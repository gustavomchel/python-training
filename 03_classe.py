"""
Faça um programa em Python orientado a objetos que receba
uma frase dada pelo usuário e a criptografe. A criptografia
consistirá na troca das vogais da frase por um número
correspondente: A – 4, E – 3, I – 1, O – 0, U – 8.
"""

class Criptografia:
    def __init__(self, frase):
        self.frase = frase
    
    def criptografar(self):
        frase_criptografada = ""
        for letra in self.frase:
            if letra.upper() == 'A':
                frase_criptografada += '4'
            elif letra.upper() == 'E':
                frase_criptografada += '3'
            elif letra.upper() == 'I':
                frase_criptografada += '1'
            elif letra.upper() == 'O':
                frase_criptografada += '0'
            elif letra.upper() == 'U':
                frase_criptrograda += '8'
            else:
                frase_criptografada += letra
        return frase_criptografada
    
def main():
    frase = input("Digite uma frase: ")
    criptografia = Criptografia(frase)
    frase_criptografada = criptografia.criptografar()
    print(f"Frase criptografada: {frase_criptografada}")

if __name__ == "__main__":
    main()