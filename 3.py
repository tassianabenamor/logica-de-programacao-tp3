#Faça um algoritmo que leia uma sequência de 20 números inteiros e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
maior = 0
menor = 0
for i in range(20):
    num = int(input("Número: "))
    soma += num #É a mesma coisa que dizer: soma = soma + num
    print(i)
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print("Soma:", soma)
print("Média:", soma / (i + 1))
print("Maior:", maior)
print("Menor:", menor)