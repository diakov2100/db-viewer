from flask_table import *

class Screen(object):
    def __init__(self, id, Resolution, Diagonal, Ratio, DisplayType, GlassType, company, year):
        self.id = id
        self.Resolution=Resolution
        self.Diagonal=Diagonal
        self.Ratio=Ratio
        self.DisplayType=DisplayType
        self.GlassType=GlassType
        self.year = year.date
        self.company = company

class ScreenTable(Table):
    id = Col('Id')
    Resolution = Col('Resolution')
    Diagonal = Col('Diagonal')
    Ratio = Col(' Ratio')
    DisplayType = Col('DisplayType')
    GlassType = Col('GlassType')
    company = Col('Company')
    year = Col('Year')