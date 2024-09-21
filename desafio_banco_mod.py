import datetime  # Importa o módulo datetime para trabalhar com data e hora

# Menu de opções que será apresentado ao usuário
menu = """
        $======= Jequié bank =======$
  "Security and tecnology in the same place!"

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=> """

# Variáveis do sistema
saldo = 0  # Saldo inicial da conta
limite = 500  # Limite máximo para saque em uma única transação
extrato = ""  # String para armazenar o histórico de transações (depósitos e saques)
numero_saques = 0  # Contador de quantos saques foram realizados
LIMITE_SAQUES = 5  # Limite diário de saques
ultimo_saque = None  # Variável que armazenará a data e hora do último saque realizado
ultimo_deposito = None  # Variável que armazenará a data e hora do último depósito realizado

# Loop principal do programa que será executado até o usuário escolher a opção de sair
while True:

    # Mostra o menu e aguarda a escolha do usuário
    opcao = input(menu)

    # Se o usuário escolher a opção 1 (Depósito)
    if opcao == "1":
        valor = float(input("Por favor, insira o valor do depósito: "))  # Solicita o valor do depósito

        # Verifica se o valor é maior que zero para ser um depósito válido
        if valor > 0:
            saldo += valor  # Adiciona o valor depositado ao saldo
            data_hora_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora do depósito
            extrato += f"Depósito: R$ {valor:.2f} em {data_hora_atual}\n"  # Registra o depósito no extrato
            ultimo_deposito = data_hora_atual  # Atualiza a variável com a data e hora do último depósito

        # Caso o valor informado seja inválido (negativo ou zero)
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Se o usuário escolher a opção 2 (Saque)
    elif opcao == "2":
        valor = float(input("Por favor, insira o valor do saque: "))  # Solicita o valor do saque

        # Verificações antes de permitir o saque
        excedeu_saldo = valor > saldo  # Verifica se o valor a sacar é maior que o saldo disponível
        excedeu_limite = valor > limite  # Verifica se o valor a sacar excede o limite permitido por transação
        excedeu_saques = numero_saques >= LIMITE_SAQUES  # Verifica se o número máximo de saques diários foi atingido

        # Caso o saque não seja possível devido ao saldo insuficiente
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        # Caso o saque exceda o limite de R$500 por transação
        elif excedeu_limite:
            print("Operação falhou! Valor excede o limite de saque!!!")

        # Caso o usuário já tenha atingido o limite diário de saques
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        # Se o valor for válido e as verificações forem atendidas
        elif valor > 0:
            saldo -= valor  # Deduz o valor do saque do saldo
            data_hora_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")  # Captura data e hora do saque
            extrato += f"Saque: R$ {valor:.2f} em {data_hora_atual}\n"  # Registra o saque no extrato
            ultimo_saque = data_hora_atual  # Atualiza a variável com a data e hora do último saque
            numero_saques += 1  # Incrementa o número de saques realizados

        # Caso o valor informado para saque seja inválido
        else:
            print("Operação falhou! O valor informado é inválido.")

    # Se o usuário escolher a opção 3 (Extrato)
    elif opcao == "3":
        print("\n$================ EXTRATO ================$")
        # Se o extrato estiver vazio, exibe mensagem de que não houve movimentações, caso contrário exibe o extrato
        print("Não foram realizadas movimentações." if not extrato else extrato)
        # Exibe a data e hora do último depósito, se houver
        if ultimo_deposito:
            print(f"Último depósito realizado em: {ultimo_deposito}")
        # Exibe a data e hora do último saque, se houver
        if ultimo_saque:
            print(f"Último saque realizado em: {ultimo_saque}")
        # Exibe o saldo atual da conta
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    # Se o usuário escolher a opção 4 (Sair), o loop é interrompido e o programa finaliza
    elif opcao == "4":
        print("\nAgradecemos por acessar: ")
        print("========JEQUIÉ BANK=========")
        print("=========OBRIGADO!=========")
        print(datetime.datetime.now().strftime("   %d/%m/%Y %H:%M:%S"))
        break 
        

    # Se o usuário inserir uma opção inválida, exibe uma mensagem de erro
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
