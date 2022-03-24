#Faça um algoritmo que informe se um número é primo ou não. Um número primo é aquele que é divisível por um e por ele mesmo. Por exemplo, 17 é um número primo.

num = int(input("Entre com um número: "))
primo = True
for i in range(2, num):
    if ((num % i) == 0):
        primo = False
        break
if (primo):
    print("Número é primo")
else:
    print("Número não é primo")