from flask_table import *
from FlaskWebProject1.db_conn import *

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class LocationTable(Table):
    id = Col('Id')
    country = Col('Country')
    city = Col('City')
    post = Col('Code')

class LocationTableFull(LocationTable):
  delete = ButtonCol('Delete', 'delete.delete_location', url_kwargs=dict(id='id'))
  update = ButtonCol('Update', 'update.update_location', url_kwargs=dict(id='id'))

class Location(object):
    def __init__(self,  id, country, city, post):
        self.id = id
        self.city = city
        self.country = country 
        self.post = post
                
class AddLocation(FlaskForm):
    country = TextField('Country', validators = [Required()])
    city = TextField('City')
    post = IntegerField('Post', validators = [Required()])

def add_location(country, city, post):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO Location VALUES ( %s, %s, %d)",
                (country, city, post))
    conn.commit()
    conn.close()

def get_locations():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Location')
    num = cursor.fetchone()[0]

    cursor.execute('SELECT * FROM Location')
    row = cursor.fetchone()
    items = [None] * num
    i = 0
    while row:
        items[i] = Location(row[3], row[0], row[1], row[2])
        i+=1
        row = cursor.fetchone()
    return items

def get_location(id):
   conn = pymssql.connect(server, user, password, "database")
   cursor = conn.cursor()

   cursor.execute('SELECT * FROM Location Where Location_Id=' + str(id))
   row = cursor.fetchone()
   return Location(row[3], row[0], row[1], row[2])

def update_location_sql(id, country, city, post):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("UPDATE [dbo].[Location]\
    SET [Country] = %s\
      ,[City] = %s\
      ,[PostalCode] =%d\
    WHERE Location_Id=" + str(id), (country, city, post))
    conn.commit()
    conn.close()

def delete_location_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM Location WHERE Location_Id=" + str(id))
    conn.commit()
    conn.close()