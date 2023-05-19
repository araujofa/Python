class Pessoas:
    cliente1 = {
        'nome' : 'FABIO',
        'idade' : 20,
        'email' : 'fas@hotmail.com'
    }

    cliente2 = {
        'nome' : 'JANE',
        'idade' : 19,
        'email' : 'jd@hotmail.com'
    }

p = Pessoas

nomeDigitado = input('\n DIGITE SEU NOME: ').upper()

def valida():
    if nomeDigitado in p.cliente1:
        print('\n SEU NOME JA ESTA CADASTRADO \n')
    else:
        print('\n SEU NOME NAO ESTA CADASTRADO, DESEJA CADASTRAR? [y/n]\n')

valida()