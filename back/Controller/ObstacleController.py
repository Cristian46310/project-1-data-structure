from back.services.ObstacleServices import ObstacleServices
class ObstacleController:
    """
    Controller class for managing obstacle-related operations.
    This class acts as an interface between the application and the ObstacleServices,
    providing methods to create and delete obstacles.
    Methods
    -------
    __init__():
        Initializes the ObstacleController and its associated service.
    createObstacle(id, x, y, tipo, x1):
        Creates a new obstacle with the specified parameters.
    deleteObstacle(id):
        Deletes the obstacle identified by the given id.
    """
    def __init__(self):
        self.service= ObstacleServices()
    

    def createObstacle(self,id,x,y,tipo,x1):
        return self.service.createObstacle(id,x,y,tipo,x1)
    
    def deleteObstacle(self,id):
        return self.service.deleteObstacle(id)
