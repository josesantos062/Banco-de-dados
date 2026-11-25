import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

id_para_deletar = int(input('Informe o id que deseja deletar: '))

cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_para_deletar,))

conexao.commit()
conexao.close()

if cursor.rowcount > 0:
    print('Usuario deletado com sucesso!!')
else:
    print('Não existe esse id salvo no banco de dados!!')