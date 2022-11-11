from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('pert3/index.html')

if __name__ == '__main__':
    app.run(debug=True)