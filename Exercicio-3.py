# Questão 3: Analisador de Dados de Equipe 
# Escreva um programa que ajude um treinador a coletar dados de seus atletas. O programa 
# deve pedir o nome e a idade de vários atletas. Para encerrar a entrada de dados, o usuário 
# deve digitar "Sair" no nome. Ao final, o programa deve exibir: 
# 1. A média de idade do grupo. 
# 2. O nome e a idade do atleta mais velho. 
# 3. Quantos atletas têm mais de 18 anos. 
# • Requisito: Use variáveis para acumular a soma das idades e um contador para o 
# total de atletas. 

# Inicialização das variáveis
soma_idades = 0
total_atletas = 0
maior_idade = 0
nome_mais_velho = ""
maiores_18 = 0

# Loop para entrada de dados
while True:
    nome = input("Digite o nome do atleta (ou 'Sair' para encerrar): ")
    
    if nome == "Sair":
        break
    
    idade = int(input("Digite a idade do atleta: "))
    
    # Acumulador e contador
    soma_idades += idade
    total_atletas += 1
    
    # Verifica atleta mais velho
    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome
    
    # Conta maiores de 18
    if idade > 18:
        maiores_18 += 1

# Evita divisão por zero
if total_atletas > 0:
    media = soma_idades / total_atletas
    
    print("\n--- RESULTADOS ---")
    print("Média de idade:", media)
    print("Atleta mais velho:", nome_mais_velho, "-", maior_idade, "anos")
    print("Quantidade com mais de 18 anos:", maiores_18)
else:
    print("Nenhum atleta foi cadastrado.")