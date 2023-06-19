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

    elif opcao == 3:
        print()
        titulo = input('Digite a titulo da manifestação: ')
        descricao = input('Digite a descricao da manifestação: ')
        tipo = input('Digite o tipo da manifestação (reclamação, elogio ou sugestão): ')
        autor = input('Digite o autor da manifestação: ')
        sqlInsercao = 'insert into ocorrencias (titulo,descricao,tipo,autor) values(%s,%s,%s,%s)'
        valores = [titulo, descricao, tipo, autor]
        insertNoBancoDados(conexao, sqlInsercao, valores)
        print('Reclamação cadastrada com sucesso. ')


    elif opcao == 4:
        print()
        consultaListagem = 'select count(*) from ocorrencias'
        resultado =  listarBancoDados(conexao,consultaListagem)
        quantidade =  resultado [0][0]
        print(  'Quantidade de Manifestações:', str(quantidade))

        consultareclamacoes = "select count(*) from ocorrencias where tipo = 'reclamação'"
        resultado = listarBancoDados(conexao, consultareclamacoes)
        quantidadeReclamacoes = resultado[0][0]
        print('Quantidade de reclamações:', str(quantidadeReclamacoes))

        consultarSugestoes = "select count(*) from ocorrencias where tipo = 'sugestão'"
        resultado = listarBancoDados(conexao, consultarSugestoes)
        quantidadeSugestoes = resultado[0][0]
        print('Quantidade de sugestões:', str(quantidadeSugestoes))

        consultarElogios = "select count(*) from ocorrencias where tipo = 'elogio'"
        resultado = listarBancoDados(conexao, consultarElogios)
        quantidadeElogios = resultado[0][0]
        print('Quantidade de elogios:', str(quantidadeElogios))

    elif opcao == 5:
        print()
        codigo = input('Digite o código da manifestação: ')
        consultaListagem = "select * from ocorrencias where codigo = '" + codigo + "'"
        ocorrencias = listarBancoDados(conexao, consultaListagem)
        if len(ocorrencias) == 0:
            print('Nenhuma manifestação cadastrada no sistema')
        else:
            ocorrencias = listarBancoDados(conexao, consultaListagem)
            print(len(ocorrencias))
            for ocorrencia in ocorrencias:
                print('codigo', str(ocorrencia[0]), '-', ocorrencia[1], '-', ocorrencia[2], '-', ocorrencia[3], '-',
                      ocorrencia[4])


    elif opcao == 6:
        print()
        codigo = input('Digite o código da manifestação: ')
        novoTitulo = input('Digite o titulo da nova manifestação: ')
        novaDescricao = input('Digite a nova descrição da manifestação: ')
        sqlAtualizar = 'update ocorrencias set titulo = %s, descricao = %s where codigo = %s'
        valores = [novoTitulo, novaDescricao, codigo]
        atualizarBancoDados(conexao, sqlAtualizar, valores)
        print('Alteração feita com sucesso')

    elif opcao == 7:
        print()
        codigo = input('Digite o codigo da manifestação: ')
        consultaListagem = 'delete from ocorrencias where codigo = %s '
        dados = [codigo]
        excluirBancoDados(conexao, consultaListagem, dados)
        print('Manifestação excluida com sucesso!')




