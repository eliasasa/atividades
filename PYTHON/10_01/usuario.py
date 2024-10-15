from dbaula import Database

class usuario:
    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.conectar()

    def criar_user(self, nome, email):
        query = 'INSERT INTO usuario (nome, email) VALUES (?, ?)'
        self.db.executar(query, (nome,email))
        self.db.commit()
    
    def listar (self):
        query = 'SELECT * FROM USUARIO'
        self.db.executar(query)
        dados = self.db.f_all()
        return dados

    def attuser (self, id, novo_n = None, novo_e = None):
        query = 'UPDATE usuario set'
        parametros = []
        if novo_n:
            query += ' nome = ?'
            parametros.append(novo_n)
        if novo_e:
            if parametros:
                query += ','
            query += ' email = ?'
            parametros.append(novo_e)
        query += ' where id = ?'
        parametros.append(id)
        self.db.executar(query, tuple(parametros))
        self.db.commit()

usuario = usuario('DBLITE.db')

# usuario.criar_user('eliasdnv', 'leagueoflegends@hotmail.com')

usuario.attuser(2, 'bosta', None)

lista = usuario.listar()

print(lista)