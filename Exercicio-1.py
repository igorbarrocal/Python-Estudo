# Questão 1: Simulador de Caixa Eletrônico (Saque) 
# Crie um programa que simule o funcionamento de um caixa eletrônico. O usuário deve 
# informar o valor que deseja sacar (apenas valores inteiros). O programa deve exibir quantas 
# cédulas de cada valor serão entregues, priorizando as de maior valor. Considere que o caixa 
# possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1. 
# • Requisito: Utilize um laço while para reduzir o valor total conforme as cédulas são 
# "entregues". 
# • Dica: Verifique com if se o valor restante é maior ou igual à cédula atual antes de 
# subtrair. 


# Solicita o valor ao usuário
valor = int(input("Digite o valor que deseja sacar: "))

# Inicializa contadores de cédulas
ced50 = 0
ced20 = 0
ced10 = 0
ced1 = 0

# Loop para calcular as cédulas
while valor > 0:
    if valor >= 50:
        valor -= 50
        ced50 += 1
    elif valor >= 20:
        valor -= 20
        ced20 += 1
    elif valor >= 10:
        valor -= 10
        ced10 += 1
    else:
        valor -= 1
        ced1 += 1

# Exibe o resultado
print("Cédulas entregues:")
print("R$50:", ced50)
print("R$20:", ced20)
print("R$10:", ced10)
print("R$1 :", ced1)