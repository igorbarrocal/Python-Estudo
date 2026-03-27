# Questão 4: Menu de Calculadora Geométrica 
# Crie um programa que apresente um menu interativo com as seguintes opções: 
# 1. Calcular área do Quadrado (Lado * Lado) 
# 2. Calcular área do Retângulo (Base * Altura) 
# 3. Calcular área do Triângulo (Base * Altura / 2) 
# 4. Sair do Programa 
# • Requisito: O programa deve usar um laço while para que o usuário possa fazer 
# vários cálculos seguidos. Se o usuário escolher uma opção inválida, o programa 
# deve exibir uma mensagem de erro e mostrar o menu novamente.

# Loop do menu
while True:
    print("\n--- MENU CALCULADORA GEOMÉTRICA ---")
    print("1. Área do Quadrado")
    print("2. Área do Retângulo")
    print("3. Área do Triângulo")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        lado = float(input("Digite o lado do quadrado: "))
        area = lado * lado
        print("Área do quadrado:", area)
    
    elif opcao == "2":
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print("Área do retângulo:", area)
    
    elif opcao == "3":
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print("Área do triângulo:", area)
    
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")