#Faça um algoritmo para mostrar a tabuada de 1 a 10.

for i in range(1, 11): #os número a serem multiplicados são i
    #print("Multiplicado", i)
    print("Tabuada de", i)
    for j in range(0, 11): #Tem um for dentro de um for porque foi detectado um padrão de repetição dentro de outro padrão
        #print(j)
        print(i, "x", j, "=", i * j)

#Para todo i dentro do intervalo entre 1 e 10, faça:
#Para todo j dentro do intervalor entra 0 a 10, faça:
#Imprima a multiplicação de i por j.