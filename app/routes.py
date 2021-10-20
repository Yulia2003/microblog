from flask import render_template, request, flash, redirect
from app import app
from app.forms import LoginForm

name = "введите имя"


@app.route ( '/' )
@app.route ( '/index', methods=['GET', 'POST'] )
def index():
    global name
    username = request.form.get ( "username" )
    if username == None:
        user = {'username': name}
    else:
        user = {'username': username}
        name = username
    return render_template ( 'index.html', title='Home', user=user )


@app.route ( '/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm ()
    if form.validate_on_submit ():
        flash ( 'Login requested for user {}, remember_me={}'.format (
            form.username.data, form.remember_me.data ) )
        return redirect ( '/index' )
    return render_template ( 'login.html', title='Sign In', form=form )