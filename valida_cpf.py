while True:

    usr_option = 1
    cpf = input('\nDigite seu CPF (Somente números): ')
    cpf_len = len(cpf)
    numbers_cpf = [int(digit) for digit in cpf]

    # FAZ A VERIFICAÇÃO SE O CPF CONTEM A QUANTIDADE DE DIGITOS CORRETOS
    if cpf_len == 11:

        # FAZ A CONTA PARA SABER SE O PRIMEIRO DIGITO VERIFICADOR CORRESPONDE AO CPF DIGITADO
        conta_digito_um = (numbers_cpf[0] * 10 + numbers_cpf[1] * 9 + numbers_cpf[2] * 8 + numbers_cpf[3] * 7 + numbers_cpf[4] * 6 + numbers_cpf[5] * 5 + numbers_cpf[6] * 4 + numbers_cpf[7] * 3 + numbers_cpf[8] * 2) * 10

        # FAZ A CONTA PARA SABER SE O SEGUNDO DIGITO VERIFICADOR CORRESPONDE AO CPF DIGITADO
        conta_digito_dois = (numbers_cpf[0] * 11 + numbers_cpf[1] * 10 + numbers_cpf[2] * 9 + numbers_cpf[3] * 8 + numbers_cpf[4] * 7 + numbers_cpf[5] * 6 + numbers_cpf[6] * 5 + numbers_cpf[7] * 4 + numbers_cpf[8] * 3 + numbers_cpf[9] * 2) * 10

        # FAZ A VALIDAÇÃO INICIAL PARA SABER SE TODOS DIGITOS SÃO IGUAIS PARA INVALIDÁ-LO
        if numbers_cpf[0] == numbers_cpf[1] and numbers_cpf[1] == numbers_cpf[2] and numbers_cpf[2] == numbers_cpf[3] and numbers_cpf[3] == numbers_cpf[4] and numbers_cpf[4] == numbers_cpf[5] and numbers_cpf[5] == numbers_cpf[6] and numbers_cpf[6] == numbers_cpf[7] and numbers_cpf[7] == numbers_cpf[8] and numbers_cpf[8] == numbers_cpf[9] and numbers_cpf[9] == numbers_cpf[10]:
            
            print(f'O CPF {cpf} é INVÁLIDO!')

        else:

            # CASO OS DIGITOS NÃO SEJAM TODOS IGUAIS, FAZ A VALIDAÇÃO SE O CPF É VALIDO OU NÃO
            if conta_digito_um % 11 == numbers_cpf[9] and conta_digito_dois % 11 == numbers_cpf[10]:

                print(f'O CPF {cpf} é VALIDO!')

            else:

                print(f'O CPF {cpf} é INVÁLIDO!')

    else:

        print('CPF digitado contem a quantidade errada de digitos!')

    # SE O USUARIO QUISER FAZER OUTRA CONSULTA O CODIGO RODA DENOVO, SENÃO O CODIGO ACABA
    option = int(input('\nDeseja realizar outra consulta? (1 para sim, 2 para não): '))

    if option != 1:
        break