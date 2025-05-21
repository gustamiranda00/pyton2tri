palavra = input("Digite uma palavra: ").lower()
vogais = "aeiou"
contador = sum(1 for letra in palavra if letra in vogais)
print(f"Total de vogais: {contador}")
