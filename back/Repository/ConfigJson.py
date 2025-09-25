import json
import os
from back.models.Configuraciones import Configuracion

class ConfigJson:
    def __init__(self):
        self.RUTA_DE_CONFIG="back/Data/Config.json"
    
    def readJsonSettings(self):
        if not os.path.exists (self.RUTA_DE_CONFIG) or os.path.getsize(self.RUTA_DE_CONFIG)==0:
            print("No hay datos existentes dentro de archivo")
            return None
        else:
            with open(self.RUTA_DE_CONFIG, 'r') as file:
                config = json.load(file)
                return config
    
    def saveSettings(self, data):
        with open(self.RUTA_DE_CONFIG, 'w') as file:
            json.dump(data, file, indent=4)

    
    def createSettings(self, settings):
        newSetting= settings.toDict()
        if not os.path.exists(self.RUTA_DE_CONFIG) or os.path.getsize(self.RUTA_DE_CONFIG) == 0:
            settings=[]
        else:
            with open(self.RUTA_DE_CONFIG, 'r') as file:
                settings = json.load(file)
        settings.append(newSetting)
        self.saveSettings(settings)

    def updateSettings(self, newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1):
        if not os.path.exists(self.RUTA_DE_CONFIG) or os.path.getsize(self.RUTA_DE_CONFIG)==0:
            print("No hay datos en el archivo")
        else:
            with open(self.RUTA_DE_CONFIG,'r')as file:
                settings=json.load(file)
            if settings:
                settings[0]['distanciaTotal']=newdistanciaTotal
                settings[0]['velocidad']=newvelocidad
                settings[0]['refresco_ms']=newrefresco_ms
                settings[0]['salto_altura']=newsalto_altura
                settings[0]['color']=newcolor
                settings[0]['x0']=newx0
                settings[0]['x1']=newx1
                settings[0]['y1']=newy1
                settings[0]['y2']=newy1
            self.saveSettings(settings)
        