from flask import render_template, flash, json, redirect, request, Flask, session, Blueprint
from flask_bootstrap import Bootstrap

from FlaskWebProject1 import app
from FlaskWebProject1.views import *
from FlaskWebProject1.db_conn import *

from werkzeug import generate_password_hash, check_password_hash
from datetime import datetime
from jinja2 import TemplateNotFound

login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/signUp', methods = ['GET', 'POST'])
def signUp():
    form = SignUp()
    if form.validate_on_submit():
        users_conn=pymssql.connect(server, user, password, "users")
        cursor = users_conn.cursor()
        _hashed_password = generate_password_hash(form.password.data)
        cursor.execute("INSERT INTO [dbo].[User] VALUES ( %s, %s, %s)",
                (form.username.data, form.email.data, _hashed_password))
        try:
            
            users_conn.commit()
            users_conn.close()
            return redirect('/')
        except Exception:
            flash('SignUp fail')
    return render_template('signup.html', 
        form=form,
        year=datetime.now().year,)

@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        try:
            users_conn=pymssql.connect(server, user, password, "users")
            cursor = users_conn.cursor()
            cursor.execute("SELECT Count(*) From [dbo].[User] where Username='" + str(form.username.data) + "'") 
            num=cursor.fetchone()[0]
            if (num>0):
                cursor.execute("SELECT Password From [dbo].[User] where Username='" + str(form.username.data) + "'")
                _hash=cursor.fetchone()[0]
                if check_password_hash(_hash, form.password.data  ):
                    session['logged_in'] = str(form.username.data)
                    users_conn.close()
                    return redirect('/')
                else:
                    flash('login fail')
                    users_conn.close()
            else:
                 flash('no such user')
                 users_conn.close()
        except Exception:
            flash('login aborted')
            users_conn.close()
    return render_template('login.html', 
        form=form,
        year=datetime.now().year,)
    
@login_blueprint.route("/logout")
def logout():
    session.pop('logged_in', None)
    return home()