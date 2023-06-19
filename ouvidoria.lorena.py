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