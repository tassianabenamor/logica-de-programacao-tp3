#Faça um algoritmo que leia uma sequência de números inteiros terminado por zero e mostre a soma, média, o maior número e o menor número da sequência.

soma = 0
maior = 0
menor = 0
cont = 0
num = int(input("Entre com um número diferente de zero: "))
while (num != 0):
    # if o valor inputado pelo usuário corresponde ao que deve ser adicionado, va p/ proxima linha
    soma = soma + num #é o mesmo que dizer soma += num
    cont += 1
    num = int(input("Entre com o próximo número: "))
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
print("Soma =", soma)
print("Média =", soma / cont)
print("Maior =", maior)
print("Menor =", menor)