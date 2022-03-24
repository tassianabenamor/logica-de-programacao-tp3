#Faça um algoritmo que leia uma sequência de números terminada em zero e mostre para cada número lido se ele é primo ou não. 

num = int(input("Entre com um número diferente de zero: "))
while (num != 0):
    primo = True
    for i in range(2, num):
        if((num % i) == 0):
            primo = False
            print(num, "não é primo")
            break
    if(primo == True):
        print("Número primo:", num)
    num = int(input("Entre com um número diferente de zero: "))