import datetime 
from datetime import date

def cadastro():
    name = input('Digite seu nome completo: ')
    nameList = name.split()
    y_id = int(input("Insira sua idade: "))
    born_year = date.today().year - y_id
    return name, nameList, born_year

name, nameList, born_year = cadastro()

print(f" Olá {name}, \n seja bem-vindo à nossa plataforma! Seu ano de Nascimento é {born_year}, caso as informações não estejam corretas siga as instruções abaixo: \n \n Digite 1 - caso infomações incorretas \n Digite - 2 caso corretas")

ques_id = int(input("Digite usa das opções: "))


if ques_id == 1:  
  cadastro()
  print(f" Olá {name}, \n seja bem-vindo à nossa plataforma! Seu ano de Nascimento é {born_year}.")

else:

  print("Tudo certo! Vamos começar")

  print(nameList[0])