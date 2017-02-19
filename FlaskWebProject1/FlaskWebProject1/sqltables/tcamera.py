from flask_table import *

class Camera(object):
    def __init__(self,id, maxPhotoRes, maxVideoRes, frameFreq, resolution ,company, year):
        self.id = id
        self.maxPhotoRes = maxPhotoRes
        self.maxVideoRes = maxVideoRes
        self.frameFreq = frameFreq
        self.resolution = resolution
        self.year = year.date
        self.company = company

class CameraTable(Table):
    id = Col('Id')
    maxPhotoRes = Col('maxPhotoRes')
    maxVideoRes = Col('maxVideoRes')
    frameFreq = Col('frameFreq')
    resolution = Col('resolution')
    company = Col('Company')
    year = Col('Year')