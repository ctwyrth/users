from users_app import app
from flask import render_template, redirect, request, session
from users_app.models.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def show_users():
    users = User.get_all()
    return render_template('read_all.html', users = users)

@app.route('/create')
def create_user():
    return render_template('/create.html')

@app.route('/user/new', methods=['POST'])
def add_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    id = User.save(data)
    return redirect('/user/' + str(id))

@app.route('/user/<int:id>')
def single_user(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template('/read_one.html', user = user)

@app.route('/user/edit/<int:id>')
def edit_one(id):
    data = {
        "id": id
    }
    user = User.get_one(data)
    return render_template('edit_one.html', user = user)

@app.route('/user/edit', methods=['POST'])
def update_one():
    data = {
        "id": request.form["id"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.update(data)
    return redirect('/users')

@app.route('/user/<int:id>/delete')
def delete_one(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/users')