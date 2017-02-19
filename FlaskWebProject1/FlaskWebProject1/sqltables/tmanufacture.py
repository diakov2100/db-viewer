from flask_table import *
from FlaskWebProject1.db_conn import *

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField, DateField
from wtforms.validators import Required

class ManufacturyTable(Table):
    id = Col('Id')
    country = Col('Country ID')
    name = Col('Name')
    year= Col('Year')
    noe=Col('Number of Employees')

class ManufacturyTableFull(ManufacturyTable):
    delete = ButtonCol('Delete', 'delete.delete_manufactury', url_kwargs=dict(id='id'))
    update = ButtonCol('Update', 'update.update_manufactury', url_kwargs=dict(id='id'))

class Manufactury(object):
    def __init__(self, name, country, year, id, noe):
        self.id = id
        self.country= country
        self.name=name
        self.year=year.date()
        self.noe=noe

class AddManufactury(FlaskForm):
    country = TextField('Country', validators = [Required()])
    name = TextField('Name', validators = [Required()])
    year= DateField('Year', validators = [Required()])
    noe=IntegerField('Number of Employees', validators = [Required()])
   
def add_manufactury(name, location, year, noe):
    conn=pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute(
               "INSERT INTO Manufacture VALUES ( %s, %s, %s, %d)",
                (name, location, year, noe)
            )
    conn.commit()
    conn.close()

def get_manufactury(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Manufacture Where Manufacture_Id=' + str(id)) 
    row = cursor.fetchone()   
    conn.close()
    return Manufactury(row[0], row[1], row[2], row[3], row[4])

def get_manufacturies():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Manufacture')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT * FROM Manufacture') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Manufactury(row[0], row[1], row[2], row[3], row[4])
        i+=1
        row = cursor.fetchone()
    conn.close()
    return items

def add_manufactury(name, location, year, noe):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO Manufacture VALUES ( %s, %d, %s, %d)",
                (name, location, year, noe))
    conn.commit()
    conn.close()

def update_manufactury_sql(id, name, location, year, noe):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("UPDATE [dbo].[Manufacture]\
        SET [Name] = %s\
        ,[Location_Id] = %d\
        ,[Year] = %s\
        ,[NumberOfEmployees] = %d\
        WHERE Manufacture_Id=" + str(id), (name, location, year, noe))
    conn.commit()
    conn.close()

def delete_manufactury_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM Manufacture WHERE Manufacture_Id=" + str(id))
    conn.commit()
    conn.close()
