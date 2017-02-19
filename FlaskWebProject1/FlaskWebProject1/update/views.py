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

update_blueprint = Blueprint('update', __name__, template_folder='templates')

@update_blueprint.route('/model/<int:id>', methods = ['GET', 'POST'])
def update_model(id):
    form = AddModel()
    item = get_model(id)
    fl=False
    if 'logged_in' in session:
        fl=True;
    
    if form.validate_on_submit():
        try:
            update_model_sql(id, form.name.data, form.manufacture_Id.data, 
                      form.OS_Id.data, form.company_Id.data,
                      form.USBConnector_Id.data, form.processor_Id.data,
                      form.fingerprint_Id.data, form.camera_Id.data,
                      form.screen_Id.data, form.price.data)
        except Exception:
            flash('Exception: Wrong Data')
            return redirect('/model/' + str(id))
        return redirect('/model')
    form.name.data = item.Name
    form.camera_Id.data = item.Camera_Id
    form.company_Id.data = item.Company
    form.fingerprint_Id.data = item.Fingerprint_Id
    form.manufacture_Id.data = item.Manufacture
    form.OS_Id.data = item.OS
    form.price.data = item.Price
    form.processor_Id.data = item.Processor_Id
    form.screen_Id.data = item.Screen_Id
    form.USBConnector_Id.data = item.USBConnector_Id
    
    return render_template('update.html',
        fl= fl,
        id=id,
        add_form='add_model_form.html',
        title='Models',
        year=datetime.now().year,
        form=form)

@update_blueprint.route('/location/<int:id>', methods = ['GET', 'POST'])
def update_location(id):
    form = AddLocation()
    item = get_location(id)
    fl=False
    if 'logged_in' in session:
        fl=True;
    
    if form.validate_on_submit():
        try:
            update_location_sql(id, form.country.data, 
                                form.city.data, form.post.data)
        except Exception:
            flash('Exception: Wrong Data')
            return redirect('/location/' + str(id))
        return redirect('/location')
    form.city.data = item.city
    form.country.data = item.country
    form.post.data = item.post
    return render_template(
        'update.html',
        fl= fl,
        id=id,
        add_form='add_location_form.html',
        title='Location',
        year=datetime.now().year,
        form=form)

@update_blueprint.route('/manufactury/<int:id>', methods = ['GET', 'POST'])
def update_manufactury(id):
    form = AddManufactury()
    item = get_manufactury(id)
    fl=False
    if 'logged_in' in session:
        fl=True;
    
    if form.validate_on_submit():
        try:
            update_manufactury_sql(id, form.name.data, form.country.data, form.year.data, form.noe.data)
        except Exception:
            flash('Exception: Wrong Data')
            return redirect('/manufactury/' + str(id))
        return redirect('/manufactury')
    form.name.data = item.name
    form.country.data = item.country
    form.year.data = item.year
    form.noe.data = item.noe
    return render_template(
        'update.html',
        title='Manufacture',
        id= id,
        fl= fl,
        add_form='add_manufacture_form.html',
        year=datetime.now().year,
        form = form)

@update_blueprint.route('/company/<int:id>', methods = ['GET', 'POST'])
def update_company(id):
    form = AddCompany()
    item = get_company(id)
    fl=False
    if 'logged_in' in session:
        fl=True;
    
    if form.validate_on_submit():
        try:
            update_company_sql(id, form.name.data, form.country.data, form.year.data, form.price.data)
        except Exception:
            flash('Exception: Wrong Data')
            return redirect('/company/' + str(id))
        return redirect('/company')
    form.name.data = item.name
    form.country.data = item.country
    form.year.data = item.year
    form.price.data = item.price
    return render_template('update.html',
        fl= fl,
        id=id,
        add_form='add_company_form.html',
        title='Company',
        year=datetime.now().year,
        form=form)

@update_blueprint.route('/os/<int:id>', methods = ['GET', 'POST'])
def update_os(id):
    form = AddOS()
    item = get_os(id)
    fl=False
    if 'logged_in' in session:
        fl=True;
    
    if form.validate_on_submit():
        try:
            update_os_sql(id, form.name.data, form.version.data, 
                           form.year.data, form.company.data)
        except Exception:
            flash('Exception: Wrong Data')
            return redirect('/update/os/' + str(id))
        return redirect('/os')
    form.company.data = item.company
    form.name.data = item.name
    form.version.data = item.version
    form.year.data = item.year
    return render_template('update.html',
        fl= fl,
        id=id,
        add_form='add_os_form.html',
        title='Company',
        year=datetime.now().year,
        form=form)