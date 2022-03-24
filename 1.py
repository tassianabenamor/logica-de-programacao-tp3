#Faça um algoritmo que leia uma sequência de caracteres terminada por um ponto e mostre o número de vogais da frase. Cada caractere deve ser digitado/lido separadamente.

vogais = ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u")
caractere = input("Entre com um caractere: ")
soma = 0
while (caractere != "."):
    if (caractere in vogais):
        soma = soma + 1
    caractere = input("Entre com o próximo caractere: ")
print("O número total de vogais é: ", soma)