import os
from flask import Flask, render_template, redirect, request
from flask_dropzone import Dropzone
from convert import convert_to_line
app = Flask(__name__)
dropzone = Dropzone(app)
filename = None

dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(dir_path, 'static/input')

app.config.update(
    UPLOADED_PATH=input_path,
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=1
)
app.config['DROPZONE_REDIRECT_VIEW'] = 'coloring'

app.secret_key = 'development key'


@app.route('/')
@app.route('/main', methods=['POST', 'GET'])
def main():
    global filename
    file = None
    if request.method == 'POST':
        f = request.files.get('file')
        file = f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        filename = f.filename
        convert_to_line(filename)
    return render_template('main.html')

@app.route('/github')
def github():
    return redirect('https://github.com/7-B/yoco')

@app.route('/coloring', methods=['POST', 'GET'])
def coloring():
    global filename
    filename = filename.split('.')[0] + '.svg'
    filename = os.path.join('output/',filename)
    return render_template('coloring.html', file_name = filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
