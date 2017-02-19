from datetime import datetime
from flask import Blueprint, render_template, flash, json, redirect, request, Flask, session
from flask_bootstrap import Bootstrap
from FlaskWebProject1 import app
from FlaskWebProject1.sqltables.tcompany import *
from FlaskWebProject1.sqltables.tlocation import *
from FlaskWebProject1.sqltables.tmanufacture import *
from FlaskWebProject1.sqltables.tos import *
from FlaskWebProject1.sqltables.tmodel import *

from FlaskWebProject1.forms import *

delete_blueprint = Blueprint('delete', __name__, template_folder='templates')

@delete_blueprint.route('/model/<int:id>', methods = ['GET', 'POST'])
def delete_model(id):
        try:
            delete_model_sql(id)
        except Exception:
            flash('Exception: Delete Error')
        return redirect('/model')

@delete_blueprint.route('/location/<int:id>', methods = ['GET', 'POST'])
def delete_location(id):
        try:
            delete_location_sql(id)
        except Exception:
            flash('Exception: Delete Error')
        return redirect('/location')

@delete_blueprint.route('/manufactury/<int:id>', methods = ['GET', 'POST'])
def delete_manufactury(id):
        try:
            delete_manufactury_sql(id)
        except Exception:
            flash('Exception: Delete Error')
        return redirect('/manufactury')

@delete_blueprint.route('/company/<int:id>', methods = ['GET', 'POST'])
def delete_company(id):
        try:
            delete_company_sql(id)
        except Exception:
            flash('Exception: Delete Error')
        return redirect('/company')

@delete_blueprint.route('/os/<int:id>', methods = ['GET', 'POST'])
def delete_os(id):
        try:
            delete_os_sql(id)
        except Exception:
            flash('Exception: Delete Error')
        return redirect('/os')