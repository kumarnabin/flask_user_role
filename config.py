from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'application-secret-key-application-secret-key-application-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=60)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)  # Example refresh token expiration

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

app.config['UPLOAD_FOLDER']='upload-dir'


jwt = JWTManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)