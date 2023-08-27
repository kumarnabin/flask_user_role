import os

from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename

from config import app

file_routes = Blueprint('file_routes', __name__)


@file_routes.route('/file/upload')
def upload_file1():
    return render_template('upload.html')


@file_routes.route('/file/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return 'file uploaded successfully'
