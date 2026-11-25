import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

id = int(input('Informe o ID para busca: '))
cursor.execute('SELECT nome, email FROM usuarios WHERE id = ?', (id,))


usuario = cursor.fetchone()

if usuario:
    print(f'Usuario encotrado: {usuario[0]} | ({usuario[1]})')
else:
    print('Usuario nao existe!!')

conexao.close()