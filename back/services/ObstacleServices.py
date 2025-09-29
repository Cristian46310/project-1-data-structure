from back.models.Obstaculo import Obstaculos
from back.Repository.ObstaculoJson import ObstacleJson

class ObstacleServices:
    """
    Service class for managing obstacle-related operations.
    Methods
    -------
    __init__():
        Initializes the ObstacleServices instance and sets up the obstacle data handler.
    createObstacle(id, x, y, tipo, x1):
        Creates a new obstacle with the specified parameters and adds it to the data store.
    deleteObstacle(id):
        Deletes the obstacle with the given ID from the data store.
    """
    def __init__(self):
        self.obstacle = ObstacleJson()
    
    def createObstacle(self,id,x,y,tipo,x1):
        obstacles=Obstaculos(id,x,y,tipo,x1)
        return self.obstacle.addObstacle(obstacles)
    
    def deleteObstacle(self,id):
        return self.obstacle.deleteObstacle(id)
