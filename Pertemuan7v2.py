from flask import Flask, render_template, session, \
    request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
@app.route('/')
def index():
    session['var'] = 100
    msg = 'Session "var" telah dibuat'
    return render_template('pert7v2/pert7v2.html', msg = msg)

@app.route('/ubahSession')
def ubahSession():
    session['var'] = 200
    msg = 'Nilai session "var" telah berubah'
    return render_template('pert7v2/pert7v2.html', msg = msg)

@app.route('/hapusSession')
def hapusSession():
    if 'var' in session.keys():
        msg = 'Session "var" telah dihapus'
        session.pop('var', None)
    else:
        msg = 'Session "var" tidak ada'
    return render_template('pert7v2/pert7v2.html', msg = msg)

@app.route('/sessi1')
def sessi1():
    if 'var' in session.keys():
        var = session['var']
    else:
        var = None
    return render_template('pert7v2/sessi1.html', var = var)

@app.route('/sessi2')
def sessi2():
    if 'var' in session.keys():
        var = session['var']
    else:
        var = None
    return render_template('pert7v2/sessi2.html', var = var)

if __name__ == "__main__":
    app.run(debug= True)