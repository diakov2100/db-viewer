from flask_table import *
from FlaskWebProject1.db_conn import *

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, IntegerField
from wtforms.validators import Required

class Model(object):
    def __init__(self, id, Name, OS, USBConnector_Id, Processor_Id, Fingerprint_Id, Camera_Id,	Screen_Id, Price, Company, Manufacture):
        self.id = id
        self.Name = Name
        self.OS = OS
        self.USBConnector_Id = USBConnector_Id
        self.Processor_Id = Processor_Id
        self.Fingerprint_Id = Fingerprint_Id
        self.Camera_Id = Camera_Id
        self.Screen_Id = Screen_Id
        self.Price = Price
        self.Company = Company
        self.Manufacture = Manufacture

class ModelTable(Table):
    id = Col('Id')
    Name = Col('Name')
    OS = Col('OS')
    USBConnector_Id = Col('USBConnector_Id')
    Processor_Id = Col('Processor_Id')
    Fingerprint_Id = Col('Fingerprint_Id')
    Camera_Id = Col('Camera_Id')
    Screen_Id = Col('Screen_Id')
    Price = Col('Price')
    Company = Col('Company')
    Manufacture = Col('Manufacture')

class ModelTableFull(ModelTable):
    delete = ButtonCol('Delete', 'delete.delete_model', url_kwargs=dict(id='id'))
    update = ButtonCol('Update', 'update.update_model', url_kwargs=dict(id='id'))

class AddModel(FlaskForm):
    name = TextField('Name', validators = [Required()])
    manufacture_Id = TextField('Manufacture', validators = [Required()])
    OS_Id = TextField('OS', validators = [Required()])
    company_Id = TextField('Company', validators = [Required()])
    USBConnector_Id = TextField('USBConnector_Id', validators = [Required()])
    processor_Id = TextField('Processor_Id', validators = [Required()])
    fingerprint_Id = TextField('Fingerprint_Id', validators = [Required()])
    camera_Id = TextField('Camera_Id', validators = [Required()])
    screen_Id = TextField('Screen_Id', validators = [Required()])
    price = IntegerField('Price', validators = [Required()])
   
def add_model(Name, Manufacture_Id, OS_Id, Company_Id, 
              USBConnector_Id, Processor_Id, 
              Fingerprint_Id, Camera_Id, Screen_Id, Price):

    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("INSERT INTO Model VALUES (%s, %d, %d, %d, %d, %d, %d, %d, %d, %d)",
                (Name, Manufacture_Id, OS_Id, Company_Id, 
              USBConnector_Id, Processor_Id, 
              Fingerprint_Id, Camera_Id, Screen_Id, Price))
    conn.commit()
    conn.close()

def get_models():
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM Model')
    num = cursor.fetchone()[0]

    cursor.execute('SELECT Model.Model_Id, Model.Name, OS.Name,\
	Model.USBConnector_Id, Model.Processor_Id, Model.Fingerprint_Id, Model.Camera_Id,\
	Screen_Id, Model.Price, Company.Name, Manufacture.Name\
    FROM Model \
    join Company on Model.Company_Id = Company.Company_Id\
    join Manufacture on Model.Manufacture_Id = Manufacture.Manufacture_Id\
    join OS on Model.OS_Id = OS.OS_Id') 
    row = cursor.fetchone()   
    items = [None] * num
    i = 0
    while row:
        items[i] = Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        i+=1
        row = cursor.fetchone()
    conn.close()
    return items

def get_model( id ):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()
    cursor.execute('SELECT Model_Id, Name, OS_Id, USBConnector_Id,\
    Processor_Id, Fingerprint_Id, Camera_Id, Screen_Id, Price,\
    Company_Id, Manufacture_Id FROM Model Where Model.Model_Id=' +str(id)) 
    row = cursor.fetchone()   
    return Model(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

def update_model_sql(id, Name, Manufacture, OS, 
                                Company, USBConnector_Id, 
                                Processor_Id, Fingerprint_Id, 
                                Camera_Id,	Screen_Id, Price):

    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("UPDATE [dbo].[Model]\
    SET [Name] = '" + Name + "'\
      ,[Manufacture_Id] = %d\
      ,[OS_Id] =  %d\
      ,[Company_Id] = %d\
      ,[USBConnector_Id] =  %d\
      ,[Processor_Id] =  %d\
      ,[Fingerprint_Id] =  %d\
      ,[Camera_Id] =  %d\
      ,[Screen_Id] =  %d\
      ,[Price] =  %d\
    WHERE Model_Id=" +str(id), (Manufacture, OS, 
                                Company, USBConnector_Id, 
                                Processor_Id, Fingerprint_Id, 
                                Camera_Id,	Screen_Id, Price))
    conn.commit()
    conn.close()

def delete_model_sql(id):
    conn = pymssql.connect(server, user, password, "database")
    cursor = conn.cursor()   
    cursor.execute("DELETE FROM Model WHERE Model_Id=" +str(id))
    conn.commit()
    conn.close()