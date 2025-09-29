from back.services.SettingsServices import SettingServices

class SettingsController:
    """
    SettingsController handles the interaction between the application and the settings service.
    Methods
    -------
    __init__():
        Initializes the SettingsController and its associated SettingServices.
    createSettings(distanciaTotal, velocidad, refresco_ms, salto_altura, color, x0, x1, y1):
        Creates new settings with the provided parameters.
    updateSettings(newdistanciaTotal, newvelocidad, newrefresco_ms, newsalto_altura, newcolor, newx0, newx1, newy1):
        Updates the existing settings with the new provided parameters.
    """
    def __init__(self):
        self.service= SettingServices()
    
    def createSettings(self, distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1):
        return self.service.createSettings(distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1)
    
    def updateSettings(self,newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1):
        return self.service.updateSettings(newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1)