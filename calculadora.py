while True:  # Inicia um laço infinito para a calculadora
    print("\nCalculadora")  # Exibe o título da calculadora

    try:  # Tenta executar o bloco de código a seguir, tratando possíveis erros
        # Exibe o menu de opções
        print("\nEscolha a operação desejada:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        # Lê a escolha da operação como um número inteiro
        operacao = int(input("Digite o número da operação desejada: "))

        # Verifica se a operação está entre 1 e 4 (operações matemáticas)
        if operacao in (1, 2, 3, 4):
            # Solicita os números para realizar a operação
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

        # Verifica se a operação é 5 (sair)
        elif operacao == 5:
            print("Encerrando calculadora...")  # Mensagem de encerramento
            break  # Encerra o loop e o programa

        # Caso o número da operação seja inválido
        else:
            print("Operação inválida. Tente novamente.")

        # Realiza a operação escolhida e exibe o resultado
        if operacao == 1:  # Soma
            print(f"O resultado da soma é: {num1 + num2}")
        elif operacao == 2:  # Subtração
            print(f"O resultado da subtração é: {num1 - num2}")
        elif operacao == 3:  # Multiplicação
            print(f"O resultado da multiplicação é: {num1 * num2}")
        elif operacao == 4:  # Divisão
            if num2 == 0:  # Verifica se o divisor é zero
                print("Divisão por zero não é permitida.")  # Erro de divisão por zero
            else:
                print(f"O resultado da divisão é: {num1 / num2}")  # Exibe o resultado

    except ValueError:  # Trata o erro se o usuário digitar algo que não seja um número
        print("Entrada inválida. Somente números são permitidos.")  # Mensagem de erro

