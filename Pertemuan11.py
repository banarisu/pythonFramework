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
        db= 'db_penjualan'
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
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('pert11/index.html', container=container)

@app.route('/tambah', methods = ['GET','POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        openDb()
        sql = "INSERT INTO barang (nama_barang, harga, stok) VALUES (%s, %s, %s)"
        val = (nama, harga, stok)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('pert11/tambah.html')

@app.route('/edit/<id_barang>', methods = ['GET', 'POST'])
def edit(id_barang):
    openDb()
    cursor.execute('SELECT * FROM barang WHERE id_barang = %s', (id_barang))
    data = cursor.fetchone()
    if request.method == 'POST':
        id_barang = request.form['id_barang']
        nama = request.form['nama']
        harga = request.form['harga']
        stok = request.form['stok']
        sql = "UPDATE barang SET nama_barang = %s, harga = %s, stok = %s WHERE id_barang = %s"
        val = (nama, harga, stok, id_barang)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('pert11/edit.html', data=data)

@app.route('/hapus/<id_barang>', methods = ['GET', 'POST'])
def hapus(id_barang):
    openDb()
    cursor.execute('DELETE FROM barang WHERE id_barang = %s', (id_barang))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)