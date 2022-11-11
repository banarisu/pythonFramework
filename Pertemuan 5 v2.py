'''
Database nya pake MySQL, dibikin di luar python
Nama db : dblibrary
Table : tbuku
    Column 1 : id (int 11, primary key, auto_increment)
    Column 2 : judul (varchar 40, utf8mb4_general_ci)
    Column 3 : penulis (varchar 25, utf8mb4_general_ci)
    Column 4 : penerbit (varchar 30, utf8mb4_general_ci)
Values nya :
    (1, "Pemrograman Web With Flask", "Wurries", "Vanda Publisher")
'''
from flask import Flask, render_template, \
    request, redirect, url_for
import pymysql.cursors, os
application = Flask(__name__)
conn = cursor = None

def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", \
                           port=3306, \
                           user="root", \
                           passwd="", \
                           db="dblibrary")
    cursor = conn.cursor()

def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@application.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM tbuku"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('pert5/pert5v2.html', container=container)

if __name__ == '__main__':
    application.run(debug=True)


