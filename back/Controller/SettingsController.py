from back.services.SettingsServices import SettingServices

class SettingsController:
    def __init__(self):
        self.service= SettingServices()
    
    def createSettings(self, distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1):
        return self.service.createSettings(distanciaTotal,velocidad,refresco_ms,salto_altura,color,x0,x1,y1)
    
    def updateSettings(self,newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1):
        return self.service.updateSettings(newdistanciaTotal,newvelocidad,newrefresco_ms,newsalto_altura,newcolor,newx0,newx1,newy1)