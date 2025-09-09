import json
import os
from back.models.Obstaculo import Obstaculos

class ObstacleJson:
    def __init__(self):
        self.RUTA_DE_OBTACLES = "back/Data/Obstacles.json"

    def readJsonObstacle(self):
        if not os.path.exists (self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES)==0:
            print("No hay datos existentes dentro de archivo")
        else:
            with open(self.RUTA_DE_OBTACLES, 'r') as file:
                Obstacles = json.load(file)
                print(Obstacles)
        
    def save(self, data):
        with open(self.RUTA_DE_OBTACLES, 'w') as file:
            json.dump(data, file, indent=4)
    

    def addObstacle(self, obstacle):
        newObstacle = obstacle.toDict()   # ✅ usamos el objeto recibido
        
        if not os.path.exists(self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES) == 0:
            obstacles = []
        else:
            with open(self.RUTA_DE_OBTACLES, 'r') as file:
                    obstacles = json.load(file)
        obstacles.append(newObstacle)
        self.save(obstacles)
    

    def deleteObstacle(self,id):
        if not os.path.exists(self.RUTA_DE_OBTACLES) or os.path.getsize(self.RUTA_DE_OBTACLES)==0:
            print("No hay datos en el archivo")
        else:
            with open(self.RUTA_DE_OBTACLES,'r')as file:
                Obstacles=json.load(file)
        validObstacle=[Obstacle for Obstacle in Obstacles if Obstacle['id']!=id]
        self.settingsJson(validObstacle)




        