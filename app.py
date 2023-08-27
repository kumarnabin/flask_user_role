from config import app
from auth_routes import auth_routes
from home_routes import home_routes
from role_routes import role_routes
from file_routes import file_routes

app.register_blueprint(home_routes)
app.register_blueprint(auth_routes)
app.register_blueprint(role_routes)
app.register_blueprint(file_routes)

if __name__ == '__main__':
    app.run()
