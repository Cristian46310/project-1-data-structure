import json
import os
from back.models.Obstaculo import Obstaculos

class ObstacleJson:
    """
    ObstacleJson is a repository class for managing obstacle data stored in a JSON file.
    Attributes:
        RUTA_DE_OBTACLES (str): The file path to the obstacles JSON file.
    Methods:
        readJsonObstacle():
            Reads and returns the list of obstacles from the JSON file.
            Returns an empty list if the file does not exist or is empty.
        saveObstacle(data):
            Saves the provided list of obstacles to the JSON file.
        addObstacle(obstacle):
            Adds a new obstacle to the JSON file after checking for duplicate positions or IDs.
            Prints a message if the obstacle already exists.
        deleteObstacle(id):
            Deletes an obstacle with the specified ID from the JSON file.
            Prints a message if the file does not contain any data.
    """
    def __init__(self):
        self.RUTA_DE_OBTACLES = "back/Data/Obstacles.json"

    def readJsonObstacle(self):
        if not os.path.exists (self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES)==0:
            print("No hay datos existentes dentro de archivo")
            return []
        else:
            with open(self.RUTA_DE_OBTACLES, 'r') as file:
                Obstacles = json.load(file)
                return Obstacles        
    
    def saveObstacle(self, data):
        with open(self.RUTA_DE_OBTACLES, 'w') as file:
            json.dump(data, file, indent=4)
    

    def addObstacle(self, obstacle):
        ObstacleExist=self.readJsonObstacle()
        newObstacle = obstacle.toDict()   
        if not os.path.exists(self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES) == 0:
            obstacles = []
        else:
            with open(self.RUTA_DE_OBTACLES, 'r') as file:
                    obstacles = json.load(file)
        for obs in ObstacleExist:
            if (obs['x1'] == newObstacle['x1'] and obs['x0'] == newObstacle['x0']) :
                print(f"{newObstacle['id']} ya existe en esa posición x")
            if obs['id'] == newObstacle['id']:
                print(f"id {newObstacle['id']} del obstáculo ya existe")
                return
        obstacles.append(newObstacle)
        self.saveObstacle(obstacles)
    

    def deleteObstacle(self,id):
        if not os.path.exists(self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES)==0:
            print("No hay datos en el archivo")
        else:
            with open(self.RUTA_DE_OBTACLES,'r')as file:
                Obstacles=json.load(file)
        validObstacle=[Obstacle for Obstacle in Obstacles if Obstacle['id']!=id]
        self.saveObstacle(validObstacle)





        