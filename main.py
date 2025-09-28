"SOLO PARA COMPROBAR COMO FUNCIONA EL BACKEND, PARA NADA MAS"


from back.Controller.ObstacleController import ObstacleController
from back.models.Obstaculo import Obstaculos
from back.utils.Arbol import ArbolAVL
import json
from back.utils.arbol23 import Tree23, Node

# Instancia del controlador
obstacle_controller = ObstacleController()

obstacle_controller.createObstacle(0, 63, 100, "persona", 73)
obstacle_controller.createObstacle(6, 51, 100, "roca", 61)
obstacle_controller.createObstacle(2, 70, 120, "cono", 80)
obstacle_controller.createObstacle(3, 90, 140, "bache", 100)

# Prueba: intentar agregar obstáculo repetido (por x)
obstacle_controller.createObstacle(4, 50, 200, "roca", 60)  # Debe mostrar mensaje de repetido

# Prueba: eliminar obstáculo
print("Eliminando obstáculo con id=2...")
obstacle_controller.deleteObstacle(3)

# # # Prueba: leer obstáculos actuales
from back.Repository.ObstaculoJson import ObstacleJson
obstacle_json = ObstacleJson()
print("Obstáculos actuales en el archivo:")
obstacle_json.readJsonObstacle()

# Crear árbol AVL y cargar obstáculos desde JSON
arbol = ArbolAVL()
arbol.insertarJson()

# Mostrar el árbol AVL en consola
print("\nÁrbol AVL actual:")
arbol.mostrarArbol()

# Consultar obstáculos dentro de un rango
x_min, x_max = 60, 100
y_min, y_max = 100, 150
resultado = arbol.consultarDistancia(x_min, x_max, y_min, y_max)
print(f"Obstáculos en el rango x=({x_min},{x_max}), y=({y_min},{y_max}):")
for obst in resultado:
    print(obst)

# Función temporal para mostrar el árbol 2-3 en consola
def mostrar_arbol_23(node, nivel=0, lado="Raiz"):
    if node is None:
        return
    print("    " * nivel + f"[{lado}] Datos: {[obj['id'] for obj in node.data]}")
    for i, child in enumerate(node.children):
        mostrar_arbol_23(child, nivel + 1, f"Hijo {i+1}")

# Leer obstáculos desde el archivo JSON
with open("back/Data/Obstacles.json", "r") as f:
    lista_obstaculos = json.load(f)

# Pruebas de inserción usando los datos del JSON
arbol = Tree23()
for obstaculo in lista_obstaculos:
    arbol.insert(obstaculo)

print("\nÁrbol 2-3 actual (desde JSON):")
mostrar_arbol_23(arbol.root)