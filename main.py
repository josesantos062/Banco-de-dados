import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

## ESCREVENDO O COMANDO PARA EXECUTAR A TABELA DE USUARIOS
tabela_sql = '''
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
    )'''

## EXECUTANDO O COMANDO
cursor.execute(tabela_sql)

## SUBINDO ALTERAÇOES NO BANCO  DE DADOS
conexao.commit()

## FECHANDO A CONEXÃO COM O BANCO DE DADOS
conexao.close()

print('Banco de dados criado com sucesso!!')
