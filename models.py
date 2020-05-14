from banco import bd

class Mensagem:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto

    def gravar(self): 
        sql = '''insert into mensagens (usuario, texto) values (?, ?)'''
        primeiro = self.usuario
        segundo = self.texto
        bd().execute(sql, [primeiro, segundo])
        bd().commit()
    
    @staticmethod
    def recupera_todas():
        ## Usamos o objeto retornado por bd() para realizar comandos sql
        sql = '''SELECT usuario, texto FROM mensagem ORDER BY id desc'''
        ## Montamos dicionários com os resultados da consulta para passar para a view
        cur = bd().execute(sql)
        mensagens = []
        for usuario, texto in cur.fetchall(): # fetchall() gera uma lista com os resultados
            mensagem = Mensagem(usuario, texto)
            mensagens.append(mensagem)
        return mensagens