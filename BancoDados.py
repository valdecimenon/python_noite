#BancoDados.py
#Usando sqlite3 (banco de dados do Android)

import sqlite3

#cria conexão com o banco de dados
con = sqlite3.connect('bancodados.db')

#cria um cursor
cur = con.cursor()

def criarTabela():
    #define a estrutura da tabela no banco de dados
    sql = 'create table if not exists contato ('\
          '   id    integer primary key autoincrement, '\
          '   nome  varchar(60), '\
          '   email varchar(100), '\
          '   telefone varchar(14) '\
          ')'
    #executa o comando sql
    cur.execute(sql)


def inserirDados():
    sql  = 'insert into contato (nome, email, telefone) values (?, ?, ?)'
    reg1 = ('Joao da Silva',  'joao@gmail.com', '(42)3224-0705')
    reg2 = ('Maria da Silva', 'maria@gmail.com', '(42)3224-1234')

    #insere registros
    cur.execute(sql, reg1)
    cur.execute(sql, reg2)

    #confirma a transação (usar sempre que fizer atualização no banco)
    con.commit()

def listarDados():
    cur.execute('select * from contato')

    #recupera os resultados, no formato:
    #[
    #   (id, nome, email, telefone)
    #   (id, nome, email, telefone)
    #]
    registros = cur.fetchall() #fetch = buscar

    #mostra todos os registros
    for reg in registros:
        print('ID: %-5d  Nome: %-20s Email: %-20s Telefone: %-20s' % reg)

    #fecha a conexao
        con.close()


if (__name__ == '__main__'):
    criarTabela()
    #inserirDados()
    listarDados()

