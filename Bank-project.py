## BANCO - Jaynne

from datetime import datetime
import sys
import getpass
import os

## ARMAZENAMENTO DE INFORMAÇÕES
 
user_cnt = {}

utilizadores = { 
    'admin': {
        'ID': 'admin',
        'Senha' : 123,
        'Nome' : 'Administrador',
        'NIF' : 125478963,
        'CC' : 1257896562,
        'Tipo': 'adm'
    }
}

## FUNÇÕES

def dadosinciais():

    novo_ID = str(len(utilizadores)+1)
    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    utilizadores[novo_ID] = {
        'Nome' : 'Jorge ',
        'Senha' : 123,
        'NIF' : 456,
        'CC' : 123,
        'Saldo': 100,
        'Tipo': 'cliente',
        'DataCadastro': data_cadastro
    }

    novo_ID = str(len(utilizadores)+1)

    utilizadores[novo_ID] = {
        'Nome' : 'Jorge Igor',
        'Senha' : 124,
        'NIF' : 457,
        'CC' : 124,
        'Saldo': 100,
        'Tipo': 'cliente',
        'DataCadastro': data_cadastro
    }

    novo_ID = str(len(utilizadores)+1)

    utilizadores[novo_ID]  = {
        'Nome' : 'Carla Lima',
        'Senha' : 120,
        'NIF' : 123,
        'CC' : 128,
        'Saldo': 115,
        'Tipo': 'cliente',
        'DataCadastro': data_cadastro
    }

    print("\nDados iniciais cadastrados\n")

def data_hora():
    data_hora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    return data_hora    

## FUNCOES MENU ADMIN

def menuadmin():
        
        os.system('cls')
    
        while True:
            print(f"\n Bem-vindo, {utilizadores['admin']['Nome']}!")
            print("\nPressione 1 - Registar novo cliente")
            print("Pressione 2 - Listar clientes")
            print("Pressione 3 - Pesquisar por NIF")
            print("Pressione 4 - Estatísticas")
            print("Pressione 0 - Sair")
    

            op= int(input("\nDigite a opção desejada: "))
            os.system('cls')
            print(f"\nOpção escolhida: {op}\n")

            if op == 1:
                os.system('cls')
                reg_clientes()
            elif op == 2:
                os.system('cls')
                lista_clientes()
            elif op == 3:
                os.system('cls')
                pesq_NIF()
            elif op == 4:
                os.system('cls')
                estatisticas()
            elif op == 0:
                os.system('cls')
                print("Obrigado e volte sempre!")
                os.system ('cls')
                break
            else:
                print("Digite uma opção válida!")

def reg_clientes():
        
    confirmar = input("1 - Cadastrar um cliente\n0 - Sair\n")

    while True:

        if confirmar == 1:

            print("\n------Digite os dados do cliente------\n")

            nome = input("Digite o nome completo do cliente: ")

            while True:
                NIF = int(input("Digite o NIF: "))
                if any(cliente['NIF'] == NIF for cliente in utilizadores.values()):
                    print("NIF já cadastrado. Por favor, insira um NIF diferente.")
                elif len(str(NIF)) != 9:
                    print("NIF inválido!") 
                else:
                    break
            while True:
                CC = int(input("Digite o número do CC: "))
                if any(cliente['CC'] == CC for cliente in utilizadores.values()):
                    print("CC já cadastrado. Por favor, insira um CC diferente.")
                elif len(str(CC)) < 9 :
                    print("Cartão cidadão inválido!") 
                else:
                    break

            Saldo = float(input("Digite o valor do depósito inicial: "))

            while True:

                try:
                    senha = getpass.getpass("Senha do cliente: ")
                    confirmar_senha = getpass.getpass("Confirme a senha: ")
                except Exception:
                    print("Aviso: não foi possível ocultar a digitação da senha neste ambiente.")
                    senha = input("Senha do cliente: ")
                    confirmar_senha = input("Confirme a senha: ")

                if formato_senha(senha, confirmar_senha):
                    break
                else:
                    input("\nDigite enter para inserir uma nova senha\n")
                    os.system ('cls')
            
            data_cadastro = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

            novo_ID = str(len(utilizadores)+1)

            utilizadores[novo_ID] = {
                'Nome' : nome,
                'Senha' : senha,
                'NIF' : NIF,
                'CC' : CC,
                'Saldo': Saldo,
                'Tipo': 'cliente',
                'DataCadastro': data_cadastro
            }

            print(f"\nCliente cadastrado com sucesso em {data_cadastro}!\n")
        else:
            menuadmin()

def formato_senha(senha, confirmar_senha):

    if len(senha) < 3:
        print('Senha muito curta! Insira um formato de senha válido!')
        return False
    elif len(senha) > 16:
        print('Senha muito longa! Insira um formato de senha válido!')
        return False
    elif ' ' in senha:
        print('A senha não pode conter espaços!')
        return False
    elif senha != confirmar_senha:
        print("As senhas não coincidem! Tente novamente.")
        return False
    else:
        return True

def lista_clientes():
    if len(utilizadores) <= 0:
        print('Não há clientes cadastrados!')
    else:
        print('Lista de clientes:\n')
        for ID, cliente in utilizadores.items():
            if cliente['Tipo'] == 'cliente':
                print(f"\nID: {ID}")
                print(f"Nome: {cliente['Nome']}")
                print(f"NIF: {cliente['NIF']}")
                print(f"CC: {cliente['CC']}")
                print(f"Data de cadastro: {cliente['DataCadastro']}")
                print(f"Saldo: €{cliente['Saldo']:.2f} \n")
        
    continuar=input("Pressione enter para continuar ->")     
    return menuadmin()

def pesq_NIF():


    NIF = int(input("Digite o NIF a ser pesquisado: "))
    encontrado = False

    for ID_cliente, cliente in utilizadores.items():
        if cliente['Tipo'] == 'cliente' and cliente['NIF'] == NIF:
            print("\nCliente encontrado!\n")
            print(f"ID: {ID_cliente}")
            print(f"Nome: {cliente['Nome']}")
            print(f"NIF: {cliente['NIF']}")
            print(f"CC: {cliente['CC']}")
            print(f"CC: {cliente['DataCadastro']}")
            print(f"Saldo: €{cliente['Saldo']:.2f}\n")
            encontrado = True
            break
    
    if not encontrado:
            print("\nNIF não encontrado.\n")

def estatisticas():
    os.system('cls')

    while True:
        print("1 - Saldo total")
        print("2 - Média do saldo clientes")
        print("3 - Max Saldo/ Cliente")
        print("4 - Min Saldo/ Cliente")
        print("5 - Total de clientes")
        print('6 - Relatório completo')
        print("0 - Sair")

        op = int(input("Digite a opção desejada: "))

        if op == 1:
            os.system('cls')
            saldo_total_banco()   
        elif op == 2:
            os.system('cls')
            media_saldo_clientes()
        elif op == 3:
            os.system('cls')
            max_saldo_clientes()
        elif op == 4:
            os.system('cls')
            min_saldo_clientes()
        elif op == 5:
            os.system('cls')
            total_clientes()
        elif op == 6:
            os.system('cls')
            relatorio_completo()
        elif op == 0:
            print("\nAnálise encerrada.\n")
            break
        else:
            print("\nDigite uma opção válida!\n")

def saldo_total_banco():

    saldo_total = 0

    for chave, cliente in utilizadores.items():
        if cliente['Tipo'] == 'cliente':
            saldo_total += cliente['Saldo']
    print(f'\nO saldo total do banco é {saldo_total} euros. Relatório gerado em {data_hora()}.\n')

def total_clientes():
    total_clientes = 0

    for chave, cliente in utilizadores.items():
        if cliente['Tipo'] == 'cliente':
            total_clientes += 1

    print(f'\nO banco possui {total_clientes} clientes. Relatório gerado em {data_hora()}.\n') 

def media_saldo_clientes():
    saldo_total = 0
    total_cliente = 0

    for chave, cliente in utilizadores.items():
        if cliente['Tipo'] == 'cliente':
            saldo_total += cliente['Saldo']
            total_cliente += 1
    print(f'\nA média do saldo dos clientes é {saldo_total/total_cliente} euros. Relatório gerado em {data_hora()}\n') 

def max_saldo_clientes():
    maior_saldo = -1
    cliente_maior_saldo = None

    for cliente in utilizadores.values():
        if cliente.get('Tipo') == 'cliente':
            if cliente['Saldo'] > maior_saldo:
                maior_saldo = cliente['Saldo']
                cliente_maior_saldo = cliente

    if cliente_maior_saldo:
        print(f"\nO cliente com maior saldo é {cliente_maior_saldo['Nome']} e possui €{maior_saldo:.2f}. Relatório gerado em: {data_hora()}.\n")
    else:
        print(f"\nNenhum cliente possui saldo no banco.  Relatório gerado em: {data_hora()}.\n")

def min_saldo_clientes():
    menor_saldo = sys.maxsize
    cliente_menor_saldo = None

    for cliente in utilizadores.values():
        if cliente.get('Tipo') == 'cliente':
            if cliente['Saldo'] < menor_saldo:
                menor_saldo = cliente['Saldo']
                cliente_menor_saldo = cliente

    if cliente_menor_saldo:
        print(f"\nO cliente com menor saldo é {cliente_menor_saldo['Nome']} e possui €{menor_saldo:.2f}.  Relatório gerado em: {data_hora()}.\n")
    else:
        print(f"\nNenhum cliente possui saldo no banco.  Relatório gerado em: {data_hora()}.\n")

def relatorio_completo():
    saldo_total_banco() 
    media_saldo_clientes()
    max_saldo_clientes()
    min_saldo_clientes()
    total_clientes()

## FUNCOES MENU CLIENTE

def menucliente():

    os.system('cls')

    while True:
        print(f"\n Bem-vindo, {user_cnt['Nome']}!")
        print("\nPressione 1 - Ver saldo")
        print("Pressione 2 - Depósito")
        print("Pressione 3 - Transferências")
        print("Pressione 4 - Levantar dinheiro")
        print("Pressione 5 - Dados pessoais")
        print("Pressione 0 - Sair")

        op= int(input("Digite a opção desejada: "))
        print(f"Opção escolhida: {op}")

        if op == 1:
            os.system('cls')
            saldo_cliente()
        elif op == 2:
            os.system('cls')
            deposito_cliente()
        elif op == 3:
            os.system('cls')
            transferencia_cliente()
        elif op == 4:
            os.system('cls')
            levantar_dinheiro()
        elif op == 5:
            os.system('cls')
            dados_pessoais()
        elif op == 0:
            print("\nObrigado e volte sempre!\n")
            break
        else:
            print("Digite uma opção válida!")

def saldo_cliente():
    print (f"\nO seu saldo é: {user_cnt['Saldo']} euros em {data_hora()}.\n")
    input("Pressione enter para continuar ->")

def deposito_cliente():
    valor = float(input("\nDigite o valor a depositar: \n"))

    if valor <= 0: 
        print("Operação inválida!")
        input("Digite enter para fazer outra operação ->")
    else:
        input(f"Depósito de {valor} euros? Verifique e pressione enter para confirmar:")
        user_cnt['Saldo'] += valor
        print(f"\nSeu depósito foi realizado em {data_hora()}.\n\n Quer verificar o novo saldo?\n 1 - Saldo\n 0 - Sair ")
        op = int(input('\nDigite o opção desejada: '))
        if op == 1:
            saldo_cliente()
        elif op == 0:
            print("\nObrigado e volte sempre!")
        
def transferencia_cliente():
    ID_para_transferencia = input("Digite o ID da conta para onde quer fazer a transferência: \n")
    valor_para_transferencia = float(input("Digite o valor que desejas transferir: \n"))

    if ID_para_transferencia not in utilizadores:
        print("Operação inválida! Conta inexistente!")
    elif ID_para_transferencia == user_cnt['ID']:
        print("Operação inválida! Não pode transferir para a mesma conta!")
    elif valor_para_transferencia <= 0:
        print("Operação inválida! Valor inválido!")
    elif valor_para_transferencia > user_cnt['Saldo']:
        print("Operação inválida! Saldo insuficiente!")
    else:
        try:
            senha = getpass.getpass(f"Deseja levantar {valor_para_transferencia} euros? Confirme a sua senha: ")
        except Exception:
            print("Aviso: não foi possível ocultar a digitação da senha neste ambiente.")
            senha = input(f"Deseja levantar {valor_para_transferencia} euros? Confirme a sua senha: ")
        
        if str(senha) != str(user_cnt['Senha']):
            print("Senha incorreta! Ação cancelada.")
        else:
            user_cnt['Saldo'] -= valor_para_transferencia
        utilizadores[ID_para_transferencia]['Saldo'] += valor_para_transferencia
        print(f"\nTransferência realizada com sucesso em {data_hora()}!\n")
    
def levantar_dinheiro():
    valor = float(input("\nDigite o valor a levantar: \n"))

    if user_cnt['Saldo'] < valor:
        print(f"Operação negada! Saldo insuficiente!")
        input("Deseja fazer uma nova operação?")
    elif valor <= 0:
        print("Operação inválida!")
        input("Digite enter para fazer outra operação ->")
    else:
        
        try:
            senha = getpass.getpass(f"Deseja levantar {valor} euros? Confirme a sua senha: ")
        except Exception:
            print("Aviso: não foi possível ocultar a digitação da senha neste ambiente.")
            senha = input(f"Deseja levantar {valor} euros? Confirme a sua senha: ")
        
        if str(senha) != str(user_cnt['Senha']):
            print("Senha incorreta! Ação cancelada.")
        else:
            user_cnt['Saldo'] -= valor
            print(f"\nDinheiro levantado com sucesso em {data_hora()}.\n")

def dados_pessoais():
    print("\nSeus dados cadastrais:\n")
    print(f"ID: {user_cnt['ID']}")
    print(f"Nome: {user_cnt['Nome']}")
    print(f"NIF: {user_cnt['NIF']}")
    print(f"CC: {user_cnt['CC']}")
    print(f"Saldo: €{user_cnt['Saldo']:.2f}\n")

## MENU PRINCIPAL

ntentativas = 3
dadosinciais()

while True:

    print('---BEM VINDO---\n')

    ID = input("Digite o seu ID: ")
    senha = int(input ("Digite sua senha: "))

    if ID == 'admin' and senha == utilizadores[ID]['Senha']:
        menuadmin()
    elif ID in utilizadores and senha == utilizadores[ID]['Senha']:
        user_cnt = utilizadores[ID]
        user_cnt['ID']= ID
        menucliente()
    else:
        ntentativas -= 1
        print (f"\nCredenciais inválidas! Restam {ntentativas} tentativas.\n")
        if ntentativas == 0:
            print (f"\nAcesso bloqueado após 3 tentativas! Procure a administração do banco.\n")
            break



        
        


