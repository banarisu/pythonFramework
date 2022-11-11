from flask import Flask, render_template
from flask_table import Table, Col

app = Flask(__name__)

class MemberTable(Table):
    nama = Col('Nama')
    nim = Col('NIM')
    kel = Col('Kelompok')

class Member(object):
    def __init__(self, nama, nim, kel):
        self.nama = nama
        self.nim = nim
        self.kel = kel

anggota = [Member('Okky Fenardi', '31180013', 'Kelompok 5'),
           Member('Marco Antonio', '31190011', 'Kelompok 5'),
           Member('Derrent Antonio', '31190087', 'Kelompok 5')]

table = MemberTable(anggota)

@app.route('/')
def index():
    result = "<br/><b> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp Tabel anggota kelompok</b><br/><br/>" + table.__html__()
    return result

if __name__ == '__main__':
    app.run(debug=True)