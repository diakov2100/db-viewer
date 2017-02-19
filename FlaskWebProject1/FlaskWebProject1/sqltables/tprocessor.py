from flask_table import *

class Processor(object):
    def __init__(self,id, Name, CoreCount, Architecture_nm, company, year):
        self.id = id
        self.Name = Name
        self.CoreCount = CoreCount
        self.Architecture_nm = Architecture_nm
        self.year = year.date
        self.company = company

class ProcessorTable(Table):
    id = Col('Id')
    Name = Col('Name')
    CoreCount = Col('CoreCount')
    Architecture_nm = Col('Architecture (nm)')
    company = Col('Company')
    year = Col('Year')