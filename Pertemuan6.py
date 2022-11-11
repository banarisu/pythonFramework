from flask import Flask, render_template,\
    request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

application = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:''@localhost/dblibrary'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(application)

class Buku(db.Model):
    __tablename__ = 'tbuku'
    id = db.Column(db.String(4), primary_key = True)
    judul = db.Column(db.String(40), unique = True)
    penulis = db.Column(db.String(25))
    penerbit = db.Column(db.String(40))

    def __init__(self, id, judul, penulis, penerbit):
        self.id = id
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit

    def __repr__(self):
        return '[%s, %s, %s, %s]' % \
               (self.id, self.judul, self.penulis, self.penerbit)

@application.route('/')
def index():
    return render_template('pert6/pert6.html', container=Buku.query.all())

if __name__ == '__main__':
    application.run(debug=True)