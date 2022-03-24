#Faça um algoritmo que calcule a soma dos números de 1 a 100.

soma = 0
num = 0
for num in range(1, 101):
    soma += num #prestar atenção nisso aqui!
    print(num)
print("A soma dos número de 1 a 100 é:", soma)