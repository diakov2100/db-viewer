from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

component_blueprint= Blueprint('component', __name__, template_folder='templates')

from datetime import datetime
from FlaskWebProject1.sqltables.tcamera import *
from FlaskWebProject1.sqltables.tcompany import *
from FlaskWebProject1.sqltables.tlocation import *
from FlaskWebProject1.sqltables.tmanufacture import *
from FlaskWebProject1.sqltables.tos import *
from FlaskWebProject1.sqltables.tfingerprint import *
from FlaskWebProject1.sqltables.tprocessor import *
from FlaskWebProject1.sqltables.tusb import *
from FlaskWebProject1.sqltables.tscreen import *
import pymssql

server = "138.68.87.1"
user = "SA"
password = "Diakov989"


@component_blueprint.route('/')
def show():
    return render_template(
        'component.html',
        title='Component Page',
        year=datetime.now().year
    )
@component_blueprint.route('/camera')
def camera():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Camera')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT Camera.Camera_Id, Camera.maxPhotoRes, Camera.maxVideoRes, Camera.frameFreq, Camera.resolution, Company.Name, Component.year\
    FROM Camera JOIN Component on Camera.Camera_Id=Component.Component_Id\
    join Company on Company.Company_Id =Component.Component_Id') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Camera(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        i+=1
        row = cursor.fetchone()
    conn.close()

    return render_template(
        'table.html',
        title='Camera',
        table=CameraTable(items),
    )
@component_blueprint.route('/fingerprint')
def fingerprint():
    """Renders the about page."""
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Camera')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT Fingerprint.Fingerprint_Id, Fingerprint.Technology, Fingerprint.SensorLocation, Company.Name, Component.year\
    FROM Fingerprint JOIN  Component on Fingerprint.Fingerprint_Id=Component.Component_Id\
    join Company on Company.Company_Id =Component.Company_Id') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Fingerprint(row[0], row[1], row[2], row[3], row[4])
        i+=1
        row = cursor.fetchone()
    conn.close()

    return render_template(
        'table.html',
        title='Fingerprint',
        table=FingerprintTable(items),
    )
@component_blueprint.route('/processor')
def processor():
    """Renders the about page."""
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Processor')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT Processor.Processor_Id, Processor.Name, Processor.CoreCount, Processor.Architecture_nm, Company.Name, Component.year\
    FROM Processor JOIN  Component on Processor.Processor_Id=Component.Component_Id\
    join Company on Company.Company_Id =Component.Company_Id') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Processor(row[0], row[1], row[2], row[3], row[4], row[5])
        i+=1
        row = cursor.fetchone()
    conn.close()

    return render_template(
        'table.html',
        title='Processor',
        table=ProcessorTable(items),
    )
@component_blueprint.route('/usbconnector')
def usb():
    """Renders the about page."""
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM USBConnector')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT USBConnector.USBConnector_Id, USBConnector.FormStandart, USBConnector.SpeedStandart, USBConnector.ChargingStandart, Company.Name, Component.year\
    FROM USBConnector  JOIN  Component on USBConnector.USBConnector_Id=Component.Component_Id\
    join Company on Company.Company_Id =Component.Company_Id') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=USB(row[0], row[1], row[2], row[3], row[4], row[5])
        i+=1
        row = cursor.fetchone()
    conn.close()

    return render_template(
        'table.html',
        title='USB Connector',
        table=USBTable(items),
    )
@component_blueprint.route('/screen')
def screen():
    """Renders the about page."""
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Screen')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT Screen.Screen_Id, Screen.Resolution, Screen.Diagonal, Screen.Ratio, Screen.DisplayType, Screen.GlassType, Company.Name, Component.year\
    FROM Screen  JOIN  Component on Screen.Screen_Id=Component.Component_Id\
    join Company on Company.Company_Id = Component.Company_Id') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Screen(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        i+=1
        row = cursor.fetchone()
    conn.close()

    return render_template(
        'table.html',
        title='Screen',
        table=ScreenTable(items),
    )