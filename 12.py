#Faça um algoritmo que leia uma opção de um menu sendo [1] Soma, [2] Subtração, [3] Multiplicação e [4] Divisão. Se a opção for válida, o programa deverá ler os operandos, realizar a operação e mostrar o resultado. Caso contrário, o programa deverá exibir uma mensagem de operação inválida. O programa termina quando o usuário digita 0.

print("Opções de menu: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão. \n[0] Para sair.")
escolhaUsuario = int(input("Escolha uma das opções do menu: "))
while (escolhaUsuario != 0): #o teste do while acontece quando ele terminar de ler tudo
    n1 = float(input("Insira o número: "))
    n2 = float(input("Insira o segundo número: "))
    if(escolhaUsuario == 1): 
        print("[1] Soma =", (n1 + n2))
    elif(escolhaUsuario == 2):
        print("[2] Subtração =", (n1 - n2))
    elif(escolhaUsuario == 3):
        print("[3] Multiplicação =", (n1 * n2))
        # escolhaUsuario = 0 => essa linha não encerra o programa, porque a linha 20 está esperando um novo input. por isso que a ultima coisa executada no looping é a escolha de usuario
    elif(escolhaUsuario == 4):
        print("[4] Divisão =", (n1 / n2))
    else:
        print("Operação inválida.")
    print("Opções de menu: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão. \n[0] Para sair.")
    escolhaUsuario = int(input("Escolha uma das opções do menu: "))