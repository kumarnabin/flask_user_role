from flask import Blueprint, render_template

home_routes = Blueprint('home_routes', __name__)


@home_routes.route('/')
def index():
    title = 'Welcome to My Website'
    return render_template('index.html', title=title)


@home_routes.route('/table')
def table_example():
    people = [
        {'name': 'Alice', 'age': 28, 'occupation': 'Engineer'},
        {'name': 'Bob', 'age': 35, 'occupation': 'Designer'},
        {'name': 'Charlie', 'age': 42, 'occupation': 'Writer'}
    ]
    return render_template('table.html', people=people, title="Table")
