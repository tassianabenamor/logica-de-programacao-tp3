#Faça um algoritmo que leia um intervalo inferior e superior, e mostre os números primos existentes no intervalo. 
# Por exemplo, o algoritmo recebe 5 e 10, e mostra como saída 5 e 7. 
# Além disso, o algoritmo deve mostrar a quantidade de números primos encontrados no intervalo.

n1 = int(input("Insira n1: "))
n2 = int(input("Insira n2: "))
for num in range(n1, n2 + 1):
    primo = True 
    for index_divisao in range(2, num):
        if ((num % index_divisao) == 0):
            primo = False
            #print("Número não é primo:", num)
            break
    if(primo == True):
        print("Número primo:", num)