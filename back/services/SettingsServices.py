from back.models.Configuraciones import Configuracion
from back.Repository.ConfigJson import ConfigJson
class SettingServices:
    """
    Service class for managing application settings.
    This class provides methods to create and update configuration settings using the ConfigJson handler.
    Attributes:
        config (ConfigJson): Instance responsible for handling configuration persistence.
    Methods:
        createSettings(distanciaTotal, velocidad, refresco_ms, salto_altura, color, x0, x1, y1):
            Creates a new settings configuration with the provided parameters.
        updateSettings(newdistanciaTotal, newvelocidad, newrefresco_ms, newsalto_altura, newcolor, newx0, newx1, newy1):
            Updates the existing settings configuration with new values.
    """
    def __init__(self):
        self.config = ConfigJson()
    

    def createSettings(self, distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1):
        settings= Configuracion(distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1)
        return self.config.createSettings(settings)
    
    def updateSettings(self,newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1):
        return self.config.updateSettings(newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1)