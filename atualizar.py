import sqlite3

# CRIANDO  A CONEXÃO COM O BANCO DE DADOS
conexao = sqlite3.connect('Meu primeiro banco')
cursor = conexao.cursor()

email_novo = input('Informe o novo email: ')
id = int(input('Informe o id para alteração: '))

try:
    conexao.execute('UPDATE usuarios SET email = ? WHERE id = ?', (email_novo,id,))

except sqlite3.IntegrityError:
    print('Email ja cadastrado!!')
except Exception as e:
    print(f'Erro detectado: {e}')

conexao.commit()
conexao.close()

if cursor.rowcount > 0:
    print('Usuario atualizado com sucesso!!')
else:
    print('Não existe esse id salvo no banco de dados!!')