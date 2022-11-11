from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    biodata = "Nama : Okky Fenardi<br/>Kelas : 7PSI1<br/>NIM : 31180013"
    return biodata

if __name__ == '__main__':
    app.run(debug=True)