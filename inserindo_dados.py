import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

## PEDINDO INFORMAÇÕES QUE VÃO SER INSERIDOS AO DB!!
nome = input('Infome o seu nome: ')
email = input('Informe seu email: ')

## COMANDO QUE INSERE OS DADOS
inserindo_dados = '''INSERT INTO usuarios (nome,email) VALUES (?,?)'''

## TRATANDO O ERRO DE EMAIL JA CADASTRADO E QUALQUER ERRO
try:
    ## EXECUTANDO O COMANDO
    cursor.execute(inserindo_dados, (nome,email,))
    ## SALVANDO NO BANCO DE DADOS
    conexao.commit()
    print(f'Dados do {nome} inserindo com sucesso!!')

except sqlite3.IntegrityError:
    print('Email ja cadastrado ao banco de dados!!')
except Exception as e:
    print(f'Erro encontrado: {e}')

## FECHANDO A CONEXÃO DO BANCO
conexao.close()
