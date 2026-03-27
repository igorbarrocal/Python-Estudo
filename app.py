import os

restaurantes=['Pizzaria do Zé', 'Churrascaria do João', 'Hamburgueria do Carlos'] ##lista de restaurantes cadastrados, inicialmente com alguns restaurantes pré-cadastrados para fins de teste


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o aplicativo. Até logo!\n')

def opcao_invalida():
    print('Opção inválida.\n')
    input('Pressione Enter para continuar...') ##pausa o programa para que o usuário possa ler a mensagem de opção inválida antes de retornar ao menu principal
    main() ##chama a função main para exibir o menu principal novamente após o usuário ler a mensagem de opção inválida

def cadastrar_novo_restaurante():
    os.system('cls')
    print('--- Cadastrar Novo Restaurante ---\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante) ##adiciona o nome do restaurante à lista de restaurantes cadastrados
    print(f'Restaurante "{nome_do_restaurante}" cadastrado com sucesso!\n')
    input('Pressione Enter para continuar...') ##pausa o programa para que o usuário possa ler a mensagem de restaurante cadastrado com sucesso antes de retornar ao menu principal
    main() ##chama a função main para exibir o menu principal novamente após o usuário
    
def listar_restaurantes():
    os.system('cls')
    print('--- Lista de Restaurantes Cadastrados ---\n')
    for restaurante in restaurantes: ##percorre a lista de restaurantes cadastrados e exibe cada um deles
        print(f'- {restaurante}')
    input('Pressione Enter para continuar...') ##pausa o programa para que o usuário possa ler a mensagem de restaurante cadastrado com sucesso antes de retornar ao menu principal
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        ##print(f'Você escolheu a opção {opcao_escolhida}')
        # opcao_escolhida = int(opcao_escolhida) ##converte a opção escolhida para inteiro, caso contrário, exibe mensagem de opção inválida

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes() ## o elif é usado para verificar cada opção escolhida, caso contrário, exibe mensagem de opção inválida
        elif opcao_escolhida == 3:
            print('Opção de ativar restaurante selecionada')  ##if para cada opção escolhida, caso contrário, exibe mensagem de opção inválida    
        elif opcao_escolhida == 4:
            finalizar_app()                                                    
        else:
            opcao_invalida() ##chama a função de opção inválida, caso o usuário escolha uma opção que não esteja entre as opções disponíveis
    except:
        opcao_invalida() ##chama a função de opção inválida, caso o usuário digite um valor que não seja um número inteiro, como uma letra ou símbolo, o que resultaria em um erro de conversão para inteiro

def main():
    os.system('cls') ##limpa a tela do terminal para exibir o nome do programa e as opções de forma mais clara
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()