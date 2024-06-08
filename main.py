#Importa o módulo

import os
from modulo import *

#Programa principal

if __name__ == '__main__':

    while True:
        
        print(f'{'*'*30} APLICATIVO DO BANCO {'*'*30}\n')

        menu_cadastro()
        print()

        opcao = int(input('Informe a opção desejada: '))

        match opcao:
            case 1:
                nome = str(input('Nome completo: '))
                cadastrar_usuario
                continue
            case 2:
                nome = str(input('Informe o nome a ser deletado: '))
                deletar_usuario
                continue
            case 3:
                entrar_programa
                menu_principal
                opcao = int(input('Informe a opção desejada: '))
