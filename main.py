"SOLO PARA COMPROBAR COMO FUNCIONA EL BACKEND, PARA NADA MAS"


from back.Controller.ObstacleController import ObstacleController
from back.models.Obstaculo import Obstaculos
from back.utils.Arbol import ArbolAVL
import json
from back.utils.arbol23 import Tree23, Node

# # Instancia del controlador
# obstacle_controller = ObstacleController()

# obstacle_controller.createObstacle(0, 63, 100, "persona", 73)
# obstacle_controller.createObstacle(6, 51, 100, "roca", 61)
# obstacle_controller.createObstacle(2, 70, 120, "cono", 80)
# obstacle_controller.createObstacle(3, 90, 140, "bache", 100)

# # Prueba: intentar agregar obstáculo repetido (por x)
# obstacle_controller.createObstacle(4, 50, 200, "roca", 60)  # Debe mostrar mensaje de repetido

# # Prueba: eliminar obstáculo
# print("Eliminando obstáculo con id=2...")
# obstacle_controller.deleteObstacle(3)

# # # # Prueba: leer obstáculos actuales
# from back.Repository.ObstaculoJson import ObstacleJson
# obstacle_json = ObstacleJson()
# print("Obstáculos actuales en el archivo:")
# obstacle_json.readJsonObstacle()

# # Crear árbol AVL y cargar obstáculos desde JSON
# arbol = ArbolAVL()
# arbol.insertarJson()

# # Mostrar el árbol AVL en consola
# print("\nÁrbol AVL actual:")
# arbol.mostrarArbol()


# Prueba de inserción y visualización del árbol 2-3
arbol23 = Tree23()
arbol23.insertarJson()
print("\nÁrbol 2-3 actual:")
arbol23.mostrarArbol()



