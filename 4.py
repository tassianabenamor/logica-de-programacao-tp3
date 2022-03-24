#Faça um algoritmo que leia uma sequência de n números inteiros e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
maior = 0
menor = 0
cont = 0
num = input("Entre com um número inteiro: ")
while (num != "."):
    soma = soma + int(num)
    cont += 1
    if cont == 0:
        maior = int(num)
        menor = int(num)
    else:
        if int(num) > maior:
            maior = int(num)
        if int(num) < menor:
            menor = int(num) 
    num = input("Entre com o próximo número: ")
print("Soma =", soma)
print("Média =", soma / cont)
print("Maior =", maior)
print("Menor =", menor)