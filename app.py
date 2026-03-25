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


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    ##print(f'Você escolheu a opção {opcao_escolhida}')
    # opcao_escolhida = int(opcao_escolhida) ##converte a opção escolhida para inteiro, caso contrário, exibe mensagem de opção inválida

    if opcao_escolhida == 1:
        print('Opção de cadastrar restaurante selecionada')
    elif opcao_escolhida == 2:
        print('Opção de listar restaurantes selecionada') ## o elif é usado para verificar cada opção escolhida, caso contrário, exibe mensagem de opção inválida
    elif opcao_escolhida == 3:
        print('Opção de ativar restaurante selecionada')  ##if para cada opção escolhida, caso contrário, exibe mensagem de opção inválida                                                        
    else:
        finalizar_app()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()