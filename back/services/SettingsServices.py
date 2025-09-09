from back.models.Configuraciones import Configuracion
from back.Repository.ConfigJson import ConfigJson
class SettingServices:
    def __init__(self):
        self.config = ConfigJson()
    

    def createSettings(self, distanciaTotal,velocidad,refresco_ms,salto_altura,color):
        settings= Configuracion(distanciaTotal,velocidad,refresco_ms,salto_altura,color)
        return self.config.createSettings(settings)
    
    def updateSettings(self,newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor):
        return self.config.updateSettings(newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor)