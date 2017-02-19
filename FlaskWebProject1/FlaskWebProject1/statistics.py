from datetime import datetime
from flask import render_template, flash, json, redirect, request, Flask, session
from flask_bootstrap import Bootstrap
from FlaskWebProject1 import app
from FlaskWebProject1.sqltables.tcompany import *
from FlaskWebProject1.sqltables.tlocation import *
from FlaskWebProject1.sqltables.tmanufacture import *
from FlaskWebProject1.sqltables.tos import *
from FlaskWebProject1.sqltables.tmodel import *
import pygal

from forms import *

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

stat_blueprint = Blueprint('stat', __name__, template_folder='templates')

@stat_blueprint.route('/statistics')
def stat():
   items = get_models()
   line_chart1 = pygal.HorizontalBar()
   line_chart1.title = 'Companies'
   line_chart2 = pygal.HorizontalBar()
   line_chart2.title = 'Manufacturies'

   pie_chart3 = pygal.Pie()
   pie_chart3.title = 'OS'
   pie_chart4 = pygal.Pie()
   pie_chart4.title = 'Countries'
   
   data1 = dict()
   data2 = dict()
   data3 = dict()
   data4 = dict()

   for item in items:
       if item.Company not in data1:
           data1[item.Company] = 0
       data1[item.Company] +=1
       if item.Manufacture not in data2:
           data2[item.Manufacture] = 0
       data2[item.Manufacture] +=1
       if item.OS not in data3:
           data3[item.OS] = 0
       data3[item.OS] +=1

   for item in data1.keys():
       line_chart1.add(item, data1[item])
   for item in data2.keys():
       line_chart2.add(item, data2[item])  
   for item in data3.keys():
       pie_chart3.add(item, data3[item])
   
    
   items = get_companies()
   for item in items:
       if item.country not in data4:
           data4[item.country] = 0
       data4[item.country] +=1
   for item in data4.keys():
       pie_chart4.add(get_location(item).country, data4[item])

   str1 = line_chart1.render_data_uri()
   str2 = line_chart2.render_data_uri()
   str3 = pie_chart3.render_data_uri()
   str4 = pie_chart4.render_data_uri()

   return render_template("stat.html", 
                          graph_data1=str1,
                          graph_data2=str2,
                          graph_data3=str3,
                          graph_data4=str4,
                          year=datetime.now().year,)
