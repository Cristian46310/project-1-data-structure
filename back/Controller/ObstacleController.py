"ACLARACION: TODO LO DEL BACKEND, COMO CREAR, ELIMINAR O MODIFICAR JSON SE HACE DESDE CONTROLLER"
" SE LLAMARA DESDE LOS CONTROLLERS, NUNCA DIRECTAMENTE"
from back.services.ObstacleServices import ObstacleServices
class ObstacleController:
    def __init__(self):
        self.service= ObstacleServices()
    

    def createObstacle(self,id,x,y,tipo,x1):
        return self.service.createObstacle(id,x,y,tipo,x1)
    
    def deleteObstacle(self,id):
        return self.service.deleteObstacle(id)
