from flask_table import *

class USB(object):
    def __init__(self, id, FormStandart, SpeedStandart, ChargingStandart, company, year):
        self.id = id
        self.FormStandart = FormStandart
        self.SpeedStandart = SpeedStandart
        self.ChargingStandart = ChargingStandart
        self.year = year.date
        self.company = company

class USBTable(Table):
    id = Col('Id')
    FormStandart = Col('FormStandart')
    SpeedStandart = Col('SpeedStandart')
    ChargingStandart = Col('SpeedStandart')
    company = Col('Company')
    year = Col('Year')