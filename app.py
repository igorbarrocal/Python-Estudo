import os

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


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        ##print(f'Você escolheu a opção {opcao_escolhida}')
        # opcao_escolhida = int(opcao_escolhida) ##converte a opção escolhida para inteiro, caso contrário, exibe mensagem de opção inválida

        if opcao_escolhida == 1:
            print('Opção de cadastrar restaurante selecionada')
        elif opcao_escolhida == 2:
            print('Opção de listar restaurantes selecionada') ## o elif é usado para verificar cada opção escolhida, caso contrário, exibe mensagem de opção inválida
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