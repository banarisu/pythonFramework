from flask import Flask, render_template, \
    request, redirect, url_for
import pymysql.cursors
import os

app = Flask(__name__)

conn = cursor = None

def openDb():
    global conn, cursor
    conn = pymysql.connect(
        host= 'localhost',
        user= 'root',
        password= "",
        db= 'db_kelompok5'
    )
    cursor = conn.cursor()

def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@app.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM tugaskelompok5"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('tugas2/index.html', container=container)

@app.route('/tambah', methods = ['GET','POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        openDb()
        sql = "INSERT INTO tugaskelompok5 (nama, nim, jurusan) VALUES (%s, %s, %s)"
        val = (nama, nim, jurusan)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tugas2/tambah.html')

@app.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id):
    openDb()
    cursor.execute('SELECT * FROM tugaskelompok5 WHERE id = %s', (id))
    data = cursor.fetchone()
    if request.method == 'POST':
        id = request.form['id']
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        sql = "UPDATE tugaskelompok5 SET nama = %s, nim = %s, jurusan = %s WHERE id = %s"
        val = (nama, nim, jurusan, id)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tugas2/edit.html', data=data)

@app.route('/hapus/<id>', methods = ['GET', 'POST'])
def hapus(id):
    openDb()
    cursor.execute('DELETE FROM tugaskelompok5 WHERE id = %s', (id))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)