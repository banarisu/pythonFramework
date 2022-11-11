from flask import Flask, render_template, request
from modelsPert9 import UploadForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '@123456'
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/static/uploads'
app.config['MAX_CONTENT_PATH'] = 10000000

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = UploadForm(request.form)
    if request.method == 'POST':
        f = request.files['file']
        filename = app.config['UPLOAD_FOLDER'] + '/' + secure_filename(f.filename)
        try:
            f.save(filename)
            return render_template('pert9v2/upload-sukses.html', filename=secure_filename(f.filename))
        except:
            return render_template('pert9v2/upload-gagal.html', filename=secure_filename(f.filename))
    return render_template('pert9v2/form-upload.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)