# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
num = int(input("Digite um número inteiro: "))

fatorial = 1

if num < 0:
    print("Não é possível calcular o fatorial de números negativos.")
elif num == 0:
    print(f"O fatorial de 0 é 1.")
else:
    while num > 1:
        fatorial *= num
        num -= 1