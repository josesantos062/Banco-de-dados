import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM usuarios')

usuarios = cursor.fetchall()

for usuario in usuarios:
    print(f'ID: {usuario[0]}')
    print(f'Nome: {usuario[1]}')
    print(f'Email: {usuario[2]}')
    print('-' * 50)

conexao.commit()
conexao.close()