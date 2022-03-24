#Faça um algoritmo que apresente a sequência de Fibonacci. A sequência começa com 0 e 1, e então produz o próximo número de Fibonacci somando os dois anteriores para formar o próximo.

n1 = 0
n2 = 1
out = 0
n = int(input("Quantos elementos da sequência de Fibonacci você deseja? "))
for i in range(1, n+1):
    if (i == 1):
        print(0)
    elif (i == 2):
        print(1)
    else:
        out = n1 + n2
        n1 = n2
        n2 = out
        print(out)