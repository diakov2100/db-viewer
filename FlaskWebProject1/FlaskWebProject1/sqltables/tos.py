from flask_table import *
from FlaskWebProject1.db_conn import *

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class OS(object):
    def __init__(self, id, name, version, company, year):
        self.id = id
        self.name = name
        self.year = year.date()
        self.version = version
        self.company = company

class OSTable(Table):
    id = Col('Id')
    name = Col('Name')
    version = Col('Version')
    company = Col('Company')
    year = Col('Year')

class OSTableFull(OSTable):
    delete = ButtonCol('Delete', 'delete.delete_os', url_kwargs=dict(id='id'))
    update = ButtonCol('Update', 'update.update_os', url_kwargs=dict(id='id'))

class AddOS(FlaskForm):
    name = TextField('Name', validators = [Required()])
    version = TextField('Version', validators = [Required()])
    company = TextField('Company', validators = [Required()])
    year = TextField('Year', validators = [Required()])
    
   
def add_os(name, version, year, company):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO OS VALUES ( %s, %s, %s, %d)",
                (name, version, year, company))
    conn.commit()
    conn.close()

def get_oss():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM OS')
    num = cursor.fetchone()[0]

    cursor.execute('SELECT OS.OS_Id,  OS.Name,  OS.Version, Company.Name, OS.Year FROM [database].[dbo].[Company] JOIN OS ON  Company.Company_Id=OS.Company_Id') 
    row = cursor.fetchone()   
    items = [None] * num
    i = 0
    while row:
        items[i] = OS(row[0], row[1], row[2], row[3], row[4])
        i+=1
        row = cursor.fetchone()
    conn.close()
    return items

def get_os(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()
    cursor.execute('SELECT OS.OS_Id,  OS.Name,  OS.Version, OS.Company_Id, OS.Year From OS Where OS_Id=' + str(id)) 
    row = cursor.fetchone()   
    return OS(row[0], row[1], row[2], row[3], row[4])


def update_os_sql(id, name, version, year, company):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("UPDATE [dbo].[OS]\
        SET [Name] = %s\
      ,[Version] = %s\
      ,[Year] = %s\
      ,[Company_Id] = %d\
      From OS Where OS_Id=" + str(id), (name, version, year, company))
    conn.commit()
    conn.close()

def delete_os_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM OS WHERE OS_Id=" + str(id))
    conn.commit()
    conn.close()

