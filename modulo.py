#Importando biblioteca de dados

from datetime import date

#Cliente cadastrados

usuarios = []

#Função Menu

def menu_cadastro():

    print('Digite 1: para CADASTRAR o usuário no aplicativo')
    print('Digite 2: para DELETAR o usuário do aplicativo.')
    print('Digite 3: para ENTRAR no aplicativo.')
    print('Digite 4: para SAIR do aplicativo.')

def menu_principal():

    print('Digite 1: para CONSULTAR saldo.')
    print('Digite 2: para DEPOSITAR.')
    print('Digite 3: para SACAR.')
    print('Digite 4: para ENCERRAR a sessão.')

def cadastrar_usuario(nome):
    if nome in usuarios:
        print('Usuário já cadastrado.')
    else:
        usuarios.append[nome]
        print(f'{nome} cadastrado com sucesso')

def deletar_usuario(nome):
    if nome in usuarios:
        del usuarios [nome]
        print(f'{nome} deletado com sucesso.')
    else:
        print(f'Usuário não encontrado')

def entrar_programa(nome):
    if nome in usuarios:
        return True
    else:
        False

def consultar_saldo(nome):
    saldo = usuarios[nome]
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    print(f'\nConsulta realizada em: {dia} de {meses[mes - 1]} de {ano}. \n')
    print(f'Saldo de {nome}: R$ {saldo: .2f}')

def depositar_valor(nome, valor):
    if valor > 0:
        usuarios[nome] += valor
        print('R$ {valor: .2f} depositado com sucesso.')
    else:
        print('Erro no depósito, refaça a operação.')

def sacar_valor(nome, valor):
    if valor > 0:
        if usuarios[nome] >= valor:
            usuarios[nome] -= valor
            print(f'R$ {valor: .2f} sacado com sucesso.')
        else:
            print('Saldo Insuficiente.')
    else:
        print('Erro no saque, refaça a operação.')