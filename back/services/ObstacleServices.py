from back.models.Obstaculo import Obstaculos
from back.Repository.ObstaculoJson import ObstacleJson

class ObstacleServices:
    def __init__(self):
        self.obstacle = ObstacleJson()
    
    def createObstacle(self,id,x,y,tipo,x1):
        obstacles=Obstaculos(id,x,y,tipo,x1)
        return self.obstacle.addObstacle(obstacles)
    
    def deleteObstacle(self,id):
        return self.obstacle.deleteObstacle(id)
