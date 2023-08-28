import json
import os

from flask import Blueprint, render_template, request, redirect, flash, send_file
from werkzeug.utils import secure_filename

from config import app, csrf
from forms import FileForm, FileApiForm

file_routes = Blueprint('file_routes', __name__)


@app.route('/images/<filename>')
def serve_image(filename):
    image_path = app.config['UPLOAD_FOLDER'] + '/' + filename
    return send_file(image_path, mimetype='image/jpeg')  # Adjust mimetype based on image type


@file_routes.route('/file/upload', methods=['GET', 'POST'])
def upload_file():
    form = FileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            f = request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            flash('File uploaded successfully!', 'success')
            flash(f.filename, 'file_name')
            return redirect("/file/upload")
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
        return redirect("/file/upload")
    return render_template('upload.html', form=form)


@file_routes.route('/api/file/upload', methods=['POST'])
@csrf.exempt
def api_upload_file():
    data = request.files  # Get JSON data from Postman

    form = FileApiForm(data=data)
    if form.validate():
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return "File uploaded successfully!"

    return form.errors
