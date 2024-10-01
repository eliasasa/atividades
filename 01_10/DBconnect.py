import sqlite3

con = sqlite3.connect('DBLITE.db')

cursor = con.cursor()

cursor.execute('''
    create table usuario(
               id integer primary key autoincrement,
               nome text not null,
               email text not null
    )
''')

con.commit()

con.close()