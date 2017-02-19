import pygal
import json
from urllib2 import urlopen  # python 2 syntax
# from urllib.request import urlopen # python 3 syntax
 
from flask import Flask
from pygal.style import DarkSolarizedStyle
 
app = Flask(__name__)
 
#----------------------------------------------------------------------
@app.route('/')
def get_weather_data(date='20140415', state='IA', city='Ames'):
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage by version in February 2012 (in %)'
    pie_chart.add('IE', [5.7, 10.2, 2.6, 1])
    pie_chart.add('Firefox', [.6, 16.8, 7.4, 2.2, 1.2, 1, 1, 1.1, 4.3, 1])
    pie_chart.add('Chrome', [.3, .9, 17.1, 15.3, .6, .5, 1.6])
    pie_chart.add('Safari', [4.4, .1])
    pie_chart.add('Opera', [.1, 1.6, .1, .5])
    pie_chart.render()
 
    html = """
        <html>
             <head>
             </head>
              <body>
                 %s
             </body>
        </html>
        """ % (pie_chart.render())
    return html
 
if __name__ == '__main__':
    app.run(debug=True)