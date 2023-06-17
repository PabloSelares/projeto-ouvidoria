from operacoesbd import *
ocorrencias = []
opcao = 1
codigo = 1
conexao = abrirBancoDados('localhost', 'root', '123456', 'ouvidoria3')

while opcao != 8:
    print()
    print('Menu')
    print()
    print('1) Listagem das Manifestações', '\n2) Listagem de Manifestações por Tipo', '\n3) Criar uma nova Manifestação'
          , '\n4) Exibir quantidade de manifestações', "\n5) Pesquisar uma manifestação por código",
          '\n6) Alterar o Título e Descrição de uma Manifestação'
          , '\n7) Excluir uma Manifestação pelo Código', '\n8) Sair do Sistema.')

    print()
    opcao = int(input('Digite uma opção: '))

    if opcao == 1:
        print()
        consultaListagem = 'select * from ocorrencias'
        ocorrencias = listarBancoDados(conexao, consultaListagem)
        if len(ocorrencias) == 0:
            print('Nenhuma manifestação cadastrada no sistema')
        else:
            print('Listagem das Manifestações')
            for ocorrencia in ocorrencias:
                print('codigo' , str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[3],'-', ocorrencia[4])


    elif opcao == 2:
        print()
        tipo = input('Digite o tipo da manifestação: reclamação, elogio ou sugestão: ')
        consultaListagem = "select * from ocorrencias where tipo = '" + tipo + "'"
        ocorrencias = listarBancoDados(conexao, consultaListagem)
        if len(ocorrencias) == 0:

            print('Nenhuma manifestação cadastrada no sistema')
        else:
            print(len(ocorrencias))
            for ocorrencia in ocorrencias:
                print('codigo', str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[2])