import os, sys

from werkzeug.contrib.cache import MemcachedCache

from collections import Counter as c_cnt
from werkzeug import secure_filename
from flask import Flask, request, session, g, \
        redirect, url_for, abort, render_template, flash, send_from_directory

app = Flask(__name__)
app.config.from_object('config')
cache = MemcachedCache(['127.0.0.1:11211'])

def get_files_dir(path):
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        f.extend(filenames)
    return f

def filetype(filename):
    return filename.rsplit('.', 1)[1]

def getUniqeWords(filename):
    c = c_cnt()
    print "Entering getUnqiqeWords"
    try:
        for line in open ('uploads/'+filename, 'r'):
            c.update(line.lower().split()) 
    except IOError as e:
        print "I/O error({0}): {1} {2}".format(e.errno, e.strerror,os.getcwd())
    return c.most_common(app.config['TOP_MAX'])

def allowed_file(filename):
    return '.' in filename and filetype(filename) in app.config['ALLOWED_EXTENSIONS']

@app.route('/ci/uploads/<filename>')
def uploaded_file(filename):
    print "Entering uploaded_file: " + filename 

    data_set = cache.get(filename)
    if data_set == None:
        data_set = getUniqeWords(filename)
        cache.set(filename, data_set, timeout=1)
    key, value = zip(*data_set)
    print '\', \''.join(key)
    files = get_files_dir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', f_all = files, key=key, value=value)

@app.route('/main')
def render_main(**kwargs):
    print "Entering render_main"
    return render_template('index.html', f_all = files)

@app.route('/ci', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            if filetype(filename) == 'zip':
                pass
            elif filetype(filename) == 'txt':
                pass

            #return redirect(url_for('uploaded_file',filename=filename))
    
    files = get_files_dir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', f_all = files)

@app.route('/')
def render_start():
    return redirect(url_for('upload_file'))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
