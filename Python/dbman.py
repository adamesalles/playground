import sqlite3

db = sqlite3.connect('test')

c = db.cursor()

    

class Pessoa:
    def __init__(self, nome):
        c.execute("SELECT * FROM nomes")
        rows = c.fetchall()
        self.id = rows[-1][0] +1
        self.nome = nome.title()
        self.add_to_db()
    def add_to_db(self):
        c.execute(f"INSERT INTO nomes VALUES ('{self.id}', '{self.nome}')")
        db.commit()
        
times = int(input("Quantas pessoas quer adicionar? Digite: "))
for i in range(times):
    nome = input("Insira o nome da pessoa: ")
    Pessoa(nome)
    
print("Seu banco de dados: ")
c.execute("SELECT * FROM nomes")
rows = c.fetchall()
print("ID | NOME ")
for row in rows:
    print(f" {row[0]} | {row[1]}")

