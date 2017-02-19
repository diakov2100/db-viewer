from flask_table import *

class Fingerprint(object):
    def __init__(self,id, Technology,SensorLocation, company, year):
        self.id = id
        self.Technology = Technology
        self.SensorLocation = SensorLocation
        self.year = year.date
        self.company = company

class FingerprintTable(Table):
    id = Col('Id')
    Technology = Col('Technology')
    SensorLocation = Col('SensorLocation')
    company = Col('Company')
    year = Col('Year')