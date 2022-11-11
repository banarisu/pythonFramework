'''import sqlite3

con = sqlite3.connect('testdb.sql')
cursor = con.cursor()
cursor.execute(
    CREATE TABLE tbuku(
    id CHAR(4) NOT NULL PRIMARY KEY,
    judul VARCHAR(40),
    penulis VARCHAR(25),
    penerbit VARCHAR(30)
    )
)

cursor.execute('INSERT INTO tbuku VALUES(?,?,?,?)',
               ('A01', 'Pemrograman Python', 'Blessy Jennifer', 'Vanda Press'))
cursor.execute('INSERT into tbuku VALUES(?,?,?,?)',
               ('A02', 'Pemrograman Flask', 'Brino Ferdinand', 'Vanda Press'))
con.commit()
cursor.close()
con.close()'''

from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def index():
    import sqlite3, os
    databaseName = os.getcwd() + '/db_pert5.db'
    con = sqlite3.connect(databaseName)
    cursor = con.cursor()
    container = []
    for id, judul, penulis, penerbit in \
    cursor.execute('Select * from tbuku'):
         container.append((id, judul, penulis, penerbit))
    cursor.close()
    con.close()
    return render_template('pert5/pert5.html', container=container)

if __name__ == '__main__':
    application.run(debug=True)