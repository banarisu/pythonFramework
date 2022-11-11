from flask import *
app = Flask(__name__)

@app.route('/error')
def error():
    return "<p><strong>Enter correct password</strong></p>"

@app.route('/')
def index():
    return render_template("pert7/pert7.html")

@app.route('/success', methods = ['POST'])
def success():
    if request.method == "POST":
        username = request.form['txtUsername']
        resp = make_response(render_template('pert7/success.html'))
        resp.set_cookie('username', username)
        return resp
    else:
        return redirect(url_for('error'))

@app.route('/viewprofile')
def profile():
    username = request.cookies.get('username')
    resp = make_response(render_template('pert7/profile.html',name = username))
    return resp

if __name__ == "__main__":
    app.run(debug= True)
