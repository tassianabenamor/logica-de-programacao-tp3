#Uma progressão aritmética é uma sequência numérica em que cada termo, a partir do segundo, é igual a soma do termo anterior com uma constante. A constante é calculada como sendo a diferença entre o segundo e o primeiro número. Faça um algoritmo que receba dois números inteiros e, a partir dessa informação, gere uma sequência em progressão aritmética.

n1 = int(input("Entre com o primeiro número: "))
n2 = int(input("Entre com o próximo número: "))
n3 = 0
const = n2 - n1
for i in range(10): #i é o indexador, o contador de qual o loop o for está. o valor de i muda enquanto está rodando o loop
    n3 = n2 + const
    n2 = n3
    print(n2, end = " ")