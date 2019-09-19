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
    try:
        filename = filename.split('/')[-1]
        filename = filename.split('.')[0] + '.svg'
        filename = os.path.join('output/',filename)
    except Exception as ex: # 에러 종류Exception:
        print(ex)

    return render_template('coloring.html', file_name = filename)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)