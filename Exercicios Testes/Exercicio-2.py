# Questão 2: O Jogo da Adivinhação Progressiva 
# Desenvolva um programa onde o computador "escolhe" um número secreto (você pode 
# definir uma variável numero_secreto = 42). O aluno deve tentar adivinhar o número. A cada 
# tentativa errada, o programa deve dizer se o número secreto é maior ou menor que o 
# palpite atual. 
# • Requisito: O laço while deve continuar até que o usuário acerte. Ao final, o 
# programa deve exibir o total de tentativas que o aluno precisou para vencer. 

# Número secreto definido
numero_secreto = 42

# Contador de tentativas
tentativas = 0

# Inicializa com valor diferente do secreto
palpite = 0

# Loop até acertar
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    
    tentativas += 1
    
    if palpite < numero_secreto:
        print("O número secreto é MAIOR!")
    elif palpite > numero_secreto:
        print("O número secreto é MENOR!")
    else:
        print("Parabéns! Você acertou!")

# Mostra total de tentativas
print("Você precisou de", tentativas, "tentativas.")