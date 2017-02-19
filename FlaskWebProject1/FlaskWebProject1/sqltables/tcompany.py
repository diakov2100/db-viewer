from flask_table import *
from FlaskWebProject1.db_conn import *

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class Company(object):
    def __init__(self, name, year, price,  id,  country):
        self.id = id
        self.country= country
        self.name=name
        self.year=year.date()
        self.price=price

class CompanyTable(Table):
    id = Col('Id')
    name = Col('Name')
    year= Col('Year')
    price=Col('Price')
    country = Col('Country ID')

class CompanyTableFull(CompanyTable):
    delete = ButtonCol('Delete', 'delete.delete_company', url_kwargs=dict(id='id'))
    update = ButtonCol('Update', 'update.update_company', url_kwargs=dict(id='id'))

class AddCompany(FlaskForm):
    country = TextField('Country', validators = [Required()])
    name = TextField('Name', validators = [Required()])
    year= TextField('Year', validators = [Required()])
    price=IntegerField('Price', validators = [Required()])
   
def add_company(name, location, year, price):
    conn=pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute(
               "INSERT INTO Company VALUES ( %s, %s, %s, %d)",
                (name, year, price, location)
            )
    conn.commit()
    conn.close()

def get_companies():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Company')
    num=cursor.fetchone()[0]

    cursor.execute('SELECT * FROM Company') 
    row = cursor.fetchone()   
    items=[None]*num
    i=0
    while row:
        items[i]=Company(row[0], row[1], row[2], row[3], row[4])
        i+=1
        row = cursor.fetchone()
    conn.close()
    return items

def get_company(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Company Where Company_Id=' + str(id)) 
    row = cursor.fetchone()   
    conn.close()
    return Company(row[0], row[1], row[2], row[3], row[4])


def add_manufactury(name, location, year, noe):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO Manufacture VALUES ( %s, %d, %s, %d)",
                (name, location, year, noe))
    conn.commit()
    conn.close()

def update_company_sql(id, name, location, year, price):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("UPDATE [dbo].[Company]\
        SET [Name] = %s\
        ,[Location_Id] = %d\
        ,[Year] = %s\
        ,[Price] = %d\
        WHERE Company_Id=" + str(id), (name, location, year, price))
    conn.commit()
    conn.close()

def delete_company_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM Company WHERE Company_Id=" + str(id))
    conn.commit()
    conn.close()

def delete_company_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM Company WHERE Company_Id=" + str(id))
    conn.commit()
    conn.close()