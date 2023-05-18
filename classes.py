nomeDigitado = input('\n DIGITE SEU NOME: ').upper()

nameList = ['FABIO', 'JANE', 'JHON']

def valida():
    if nomeDigitado in nameList:
        print('\n Seu nome esta na lista, ' + nomeDigitado)
    else:
        print('\n Seu nome nao esta na lista')

valida()

class person:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def myFunc(self):
        print('\n Olá meu nome é ' + self.nome + ' e tenho ' + str(self.idade) + ' anos \n')

pessoa = person('Fabio', 20)
pessoa.myFunc()