numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(3)]
duplicados = [num * 2 for num in numeros]
print(f"Lista original: {numeros}")
print(f"Lista com números multiplicados por 2: {duplicados}")
print(f"Soma dos números originais: {sum(numeros)}")
print(f"Soma dos números multiplicados por 2: {sum(duplicados)}")