from back.services.SettingsServices import SettingServices

class SettingsController:
    def __init__(self):
        self.service= SettingServices()
    
    def createSettings(self, distanciaTotal,velocidad,refresco_ms,salto_altura,color):
        return self.service.createSettings(distanciaTotal,velocidad,refresco_ms,salto_altura,color)
    
    def updateSettings(self,newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor):
        return self.service.updateSettings(newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor)