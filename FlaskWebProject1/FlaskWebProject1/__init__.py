"""
The flask application package.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key='you should not pass'
app.config.from_object('config')
Bootstrap(app)
from FlaskWebProject1.sqltables.views import component_blueprint
from FlaskWebProject1.login.views import login_blueprint
from FlaskWebProject1.update.views import update_blueprint
from FlaskWebProject1.delete.views import delete_blueprint
from FlaskWebProject1.statistics import *

app.register_blueprint(component_blueprint, url_prefix='/component')
app.register_blueprint(login_blueprint)
app.register_blueprint(update_blueprint,  url_prefix='/update')
app.register_blueprint(delete_blueprint,  url_prefix='/delete')
app.register_blueprint(stat_blueprint)