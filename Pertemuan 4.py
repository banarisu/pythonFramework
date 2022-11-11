from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        namaDepan = request.form['namaDpn']
        namaBelakang = request.form['namaBlkg']
        nama = '%s %s' %(namaDepan, namaBelakang)
        return render_template('pert4/hasilpert4.html', nama = nama)
    return render_template('pert4/pert4.html')

if __name__ == '__main__':
    app.run(debug=True)