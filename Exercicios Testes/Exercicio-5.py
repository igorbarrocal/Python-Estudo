# Questão 5: Controle de Estoque de Loja 
# Uma loja precisa de um sistema simples para registrar vendas. O programa deve ler o nome 
# de um produto e o seu preço. Após cada produto, deve perguntar se o usuário deseja 
# continuar (S/N). No final, o programa deve mostrar: 
# 1. Qual é o total gasto na compra. 
# 2. Quantos produtos custam mais de R$ 100,00. 
# 3. Qual é o nome do produto mais barato. 
# • Requisito: Utilize o while para controlar a continuidade da inserção e o if para as 
# verificações de preço e produto mais barato.

# Inicialização das variáveis
total_gasto = 0
produtos_mais_100 = 0
nome_mais_barato = ""
preco_mais_barato = 0

# Controle do loop
continuar = "S"

while continuar == "S":
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    
    # Soma total
    total_gasto += preco
    
    # Conta produtos acima de 100
    if preco > 100:
        produtos_mais_100 += 1
    
    # Verifica produto mais barato
    if preco_mais_barato == 0 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome
    
    # Pergunta se continua
    continuar = input("Deseja continuar? (S/N): ").upper()

# Resultados
print("\n--- RESULTADO ---")
print("Total gasto: R$", total_gasto)
print("Produtos acima de R$100:", produtos_mais_100)
print("Produto mais barato:", nome_mais_barato, "- R$", preco_mais_barato)