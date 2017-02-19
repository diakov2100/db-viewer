from datetime import datetime
from flask import render_template, flash, json, redirect, request, Flask, session
from flask_bootstrap import Bootstrap
from FlaskWebProject1 import app
from FlaskWebProject1.sqltables.tcompany import *
from FlaskWebProject1.sqltables.tlocation import *
from FlaskWebProject1.sqltables.tmanufacture import *
from FlaskWebProject1.sqltables.tos import *
from FlaskWebProject1.sqltables.tmodel import *

from forms import *

@app.route('/')
@app.route('/index')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='DB Viewer',
        year=datetime.now().year,)

@app.route('/location', methods = ['GET', 'POST'])
def location():
    items = get_locations()
    form = AddLocation()
    fl=False
    table=LocationTable(items)
    if 'logged_in' in session:
        table=LocationTableFull(items)
        fl=True
    if form.validate_on_submit():
        try:
            add_location(form.country.data, form.city.data, form.post.data)
            flash('Country: ' + form.country.data + ' City: ' + form.city.data + ' Post code: ' + str(form.post.data))
        except Exception:
            flash('Exception: Wrong Data')
        return redirect('/location')
    return render_template('table.html',
        title='Locations',
        table=table,
        year=datetime.now().year,
        form=form,
        fl=fl,
        add_form="add_location_form.html")

@app.route('/manufactury', methods = ['GET', 'POST'])
def manufactury():
    items = get_manufacturies()
    form = AddManufactury()
    fl=False
    if 'logged_in' in session:
        table=ManufacturyTableFull(items)
        fl=True
    else:
        table=ManufacturyTable(items)
    if form.validate_on_submit():
        try:
            add_manufactury(form.name.data, form.country.data, form.year.data, form.noe.data)
        except Exception:
            flash('Exception: Wrong Data')
        return redirect('/manufactury')
    return render_template('table.html',
        title='Manufacture',
        table=table,
        year=datetime.now().year,
        form=form,
        fl=fl,
        add_form="add_manufacture_form.html")

@app.route('/company', methods = ['GET', 'POST'])
def company():
    items = get_companies()
    fl=False
    form = AddCompany()
    if 'logged_in' in session:
        table=CompanyTableFull(items)
        fl=True
    else:
        table=CompanyTable(items)
    if form.validate_on_submit():
        try:
            add_company(form.name.data, form.country.data, form.year.data, form.price.data)
        except Exception:
            flash('Exception: Wrong Data')
        return redirect('/company')
    return render_template('table.html',
        title='Company',
        table=table,
        year=datetime.now().year,
        form=form,
        fl=fl,
        add_form="add_company_form.html")

@app.route('/os', methods = ['GET', 'POST'])
def os():
    fl=False
    form = AddOS()
    if 'logged_in' in session:
        table=OSTableFull(get_oss())
        fl=True
    else:
        table=OSTable(get_oss())
    if form.validate_on_submit():
        try:
            add_os(form.name.data, form.version.data, form.year.data, form.company.data)
        except Exception:
            flash('Exception: Wrong Data')
        return redirect('/os')
    return render_template('table.html',
        title='OS',
        table=table,
        year=datetime.now().year,
        fl=fl,
        form=form,
        add_form="add_os_form.html")

@app.route('/model', methods = ['GET', 'POST'])
def model():
    fl=False
    if 'logged_in' in session:
        table=ModelTableFull(get_models())
        fl=True
    else:
        table=ModelTable(get_models())
    form = AddModel()
    if form.validate_on_submit():
        try:
            add_model(form.name.data, form.manufacture_Id.data, 
                      form.OS_Id.data, form.company_Id.data,
                      form.USBConnector_Id.data, form.processor_Id.data,
                      form.fingerprint_Id.data, form.camera_Id.data,
                      form.screen_Id.data, form.price.data)
        except Exception:
            flash('Exception: Wrong Data')
        return redirect('/model')
    return render_template('table.html',
        title='Models',
        table=table,
        year=datetime.now().year,
        form=form,
        fl =fl,
        add_form="add_model_form.html")

